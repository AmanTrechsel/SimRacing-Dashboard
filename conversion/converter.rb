# Initialize global values
@final_data = "import struct\n\n"
@structs = {}

# Method to convert data type to corresponding format character
def data_type_to_format_char(data_type)
  case data_type
  when "uint8_t"
    return 'B'
  when "uint16_t"
    return 'H'
  when "uint32_t"
    return 'I'
  when "uint64_t"
    return 'Q'
  when "int8_t"
    return 'b'
  when "char"
    return 'c'
  when "int16_t"
    return 'h'
  when "int32_t"
    return 'i'
  when "int64_t"
    return 'q'
  when "float"
    return 'f'
  when "double"
    return 'd'
  else
    return "{#{data_type}.format()}"
  end
end

# Method to return default value based on data type and whether it's an array
def default_value(data_type, is_array = false)
  if is_array
    return "[]"
  else
    case data_type
    when "uint8_t", "uint16_t", "uint32_t", "uint64_t", "int8_t", "int16_t", "int32_t", "int64_t"
      return 0
    when "float", "double"
      return 0.0
    when "char"
      return "''"
    else
      return "#{data_type}()"
    end
  end
end

# Method to parse a struct from a given file path
def parse_struct(file_path)
  File.open(file_path, 'r') do |input_file|
    file_name = File.basename(file_path, ".h").split('/')[-1]
    # Skip if struct already parsed
    return if @structs[file_name] != nil
    python_data = "class #{file_name}:\n\t# Returns the unpack format\n\t@staticmethod\n\tdef format():\n\t\treturn f\"<"
    variables = []
    format_string = ""
    # Read struct data
    input_file.each_line do |line|
      words = line.split(' ')
      if words.length == 2
        if (words[1].include?("[") && words[1].include?("]") && words[1].split('[').length == 2)
          variables.push([words[0], words[1].split('[')[0], words[1].split('[')[1].gsub(']', '').to_i])
        else
          variables.push(words)
        end
      end
    end
    variables.each do |variable|
      if variable[2] != nil && variable[2] > 0
        variable[2].times do |i|
          format_string += data_type_to_format_char(variable[0])
        end
      else
        format_string += data_type_to_format_char(variable[0])
      end
    end
    python_data += "#{format_string}\"\n\n\t# Returns the byte size\n\t@staticmethod\n\tdef size():\n\t\treturn struct.calcsize(#{file_name}.format())\n\n\t# Initialize\n\tdef __init__(self, unpacked_data):"
    # Implement variables
    offset = 0
    variables.each_with_index do |variable, i|
      # Check if the variable is another class
      if data_type_to_format_char(variable[0]).start_with?("{")
        struct = variable[0].split('.')[0].gsub('}', '').gsub('{', '')
        parse_struct("./headers/#{struct}.h") if @structs[struct] == nil
        struct = @structs[struct]
        array_size = variable[2] != nil ? variable[2] : 0
        if array_size == 0
          python_data += "\n\t\tself.#{variable[1].chomp} = #{struct[0]}(unpacked_data[#{i + offset}:#{i + offset + struct[3]}])"
          offset += struct[3] - 1
        else
          python_data += "\n\t\tself.#{variable[1].chomp} = ["
          array_size.times do |j|
            python_data += "#{struct[0]}(unpacked_data[#{i + offset + struct[3] * j}:#{i + offset + struct[3] * (j+1)}])"
            python_data += ", " if j < array_size - 1
          end
          offset += struct[3] * array_size - 1
          python_data += "]"
        end
      else
        # Check if it's an array or string
        if variable[2] != nil && variable[2] > 0
          # Differentiate between string and array
          if variable[0] == "char"
            end_value = i + offset + variable[2]
            python_data += "\n\t\tself.#{variable[1].chomp} = b''.join(unpacked_data[#{i + offset}:#{end_value}]).decode('utf-8').split('\\x00', 1)[0]"
          else
            python_data += "\n\t\tself.#{variable[1].chomp} = ["
            variable[2].times do |j|
              python_data += "unpacked_data[#{i + offset + j}]"
              python_data += ", " if j < variable[2] - 1
            end
            python_data += "]"
          end
          offset += variable[2] - 1
        else
          python_data += "\n\t\tself.#{variable[1].chomp} = unpacked_data[#{i + offset}]"
        end
      end
    end
    # To String
    python_data += "\n\n\t# To string\n\tdef __str__(self):\n\t\ttext = \"--== <#{file_name}> ==--\\n\"\n"
    variables.each_with_index do |variable, i|
      python_data += "\t\ttext += f\"#{variable[1]}: {self.#{variable[1].chomp}}#{i < variables.length - 1 ? "\\n" : ""}\"\n"
    end
    python_data += "\t\treturn text\n\n\t# Prints data in a readable format\n\tdef print(self):\n\t\tprint(f\"{self}\")\n"
    # To Dictionary
    python_data += "\n\t# Turns the object into a useable dictionary\n\tdef to_dict(self):\n\t\tdictionary = {}\n\t\tdictionary[\"name\"] = \"#{file_name}\"\n"
    variables.each_with_index do |variable, i|
      if data_type_to_format_char(variable[0]).start_with?("{")
        if variable[2] != nil && variable[2] > 0
          python_data += "\t\tdictionary[\"#{variable[1]}\"] = [x.to_dict() for x in self.#{variable[1].chomp}]\n"
        else
          python_data += "\t\tdictionary[\"#{variable[1]}\"] = self.#{variable[1].chomp}.to_dict()\n"
        end
      else
        python_data += "\t\tdictionary[\"#{variable[1]}\"] = self.#{variable[1].chomp}\n"
      end
    end
    python_data += "\t\treturn dictionary"
    # Store data
    @structs[file_name] = [file_name, variables, format_string, variables.length + offset]
    @final_data += python_data + "\n\n"
  end
end

# Iterate through header files in the 'headers' directory
Dir.foreach('./headers') do |file|
  next if file == '.' or file == '..'
  if File.extname(file) == '.h'
    parse_struct("./headers/#{file}")
  end
end

# Replace format placeholders with actual format strings
@structs.each_pair do |key, value|
  @final_data.gsub!("{#{key}.format()}", "#{value[2]}")
end

# Write the final data to a Python file
File.open("../app/structs.py", 'w') do |output_file|
  output_file.write(@final_data)
end