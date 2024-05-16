import socket
import struct

from app.structs import *

# Constants
PACKET_HEADER_SIZE = PacketHeader.size()    # Size of the packet header
BUFFER_SIZE = 4096                          # Buffer size is 4096 bytes
UDP_IP = "0.0.0.0"                          # Listen on all available network interfaces
UDP_PORT = 20777                            # Choose a port number
DEFAULT_PLAYER_INDEX = 0                    # Index of the player's car in the data arrays
PRINT_PACKETS = False                       # Print the received packets
EMPTY_VELOCITY = 0                          # Empty velocity value
EMPTY_FUEL = 0.0                            # Empty fuel value
EMPTY_FUEL_LAPS = 0.0                       # Empty fuel laps value
EMPTY_LAP_TIME = "00:00:000"                # Empty lap time string
DEFAULT_TYRE_WEAR = [0, 0, 0, 0]            # Default tyre wear data
DEFAULT_TYRE_DATA = [0, 0, 0, 0]            # Default tyre data
WEATHER_FORECAST_INDEX = 0                  # Index of the weather forecast sample

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP and port
sock.bind((UDP_IP, UDP_PORT))

# Print the port number
print("Started listening on port ", UDP_PORT)

# Variables to store the received packets
packet_header = None
packet_motion_data = None
packet_session_data = None
packet_lap_data = None
packet_event_data = None
packet_participants_data = None
packet_car_setup_data = None
packet_car_telemetry_data = None
packet_car_status_data = None
packet_final_classification_data = None
packet_lobby_info_data = None
packet_car_damage_data = None
packet_session_history_data = None
packet_tyre_sets_data = None
packet_motion_ex_data = None

last_best_lap_time = EMPTY_LAP_TIME
player_index = DEFAULT_PLAYER_INDEX

# Function to listen for incoming packets
def listen():
    # Receive data from the socket
    data, addr = sock.recvfrom(BUFFER_SIZE)

    # Define the global variables
    global packet_header
    global packet_motion_data
    global packet_session_data
    global packet_lap_data
    global packet_event_data
    global packet_participants_data
    global packet_car_setup_data
    global packet_car_telemetry_data
    global packet_car_status_data
    global packet_final_classification_data
    global packet_lobby_info_data
    global packet_car_damage_data
    global packet_session_history_data
    global packet_tyre_sets_data
    global packet_motion_ex_data

    # Check if received data has at least the size of the packet header
    if len(data) >= PACKET_HEADER_SIZE:
        # Unpack the packet header
        packet_header = PacketHeader(struct.unpack(PacketHeader.format(), data[:PACKET_HEADER_SIZE]))
        
        # PacketMotionData
        if packet_header.m_packetId == 0:
            # Check if the received data has enough size for PacketMotionData
            if len(data) >= PacketMotionData.size():
                # Unpack the PacketMotionData
                packet_motion_data = PacketMotionData(struct.unpack(PacketMotionData.format(), data[:PacketMotionData.size()]))
                return packet_motion_data

        # PacketSessionData
        elif packet_header.m_packetId == 1:
            # Check if the received data has enough size for PacketSessionData
            if len(data) >= PacketSessionData.size():
                # Unpack the PacketSessionData
                packet_session_data = PacketSessionData(struct.unpack(PacketSessionData.format(), data[:PacketSessionData.size()]))
                return packet_session_data
        
        # PacketLapData
        elif packet_header.m_packetId == 2:
            # Check if the received data has enough size for PacketLapData
            if len(data) >= PacketLapData.size():
                # Unpack the PacketLapData
                packet_lap_data = PacketLapData(struct.unpack(PacketLapData.format(), data[:PacketLapData.size()]))
                return packet_lap_data
            
        # PacketEventData
        elif packet_header.m_packetId == 3:
            # Check if the received data has enough size for PacketEventData
            if len(data) >= PacketEventData.size():
                # Unpack the PacketEventData
                packet_event_data = PacketEventData(struct.unpack(PacketEventData.format(), data[:PacketEventData.size()]))
                return packet_event_data
            
        # PacketParticipantsData
        elif packet_header.m_packetId == 4:
            # Check if the received data has enough size for PacketParticipantsData
            if len(data) >= PacketParticipantsData.size():
                # Unpack the PacketParticipantsData
                packet_participants_data = PacketParticipantsData(struct.unpack(PacketParticipantsData.format(), data[:PacketParticipantsData.size()]))
                return packet_participants_data
            
        # PacketCarSetupData
        elif packet_header.m_packetId == 5:
            # Check if the received data has enough size for PacketCarSetupData
            if len(data) >= PacketCarSetupData.size():
                # Unpack the PacketCarSetupData
                packet_car_setup_data = PacketCarSetupData(struct.unpack(PacketCarSetupData.format(), data[:PacketCarSetupData.size()]))
                return packet_car_setup_data
            
        # PacketCarTelemetryData
        elif packet_header.m_packetId == 6:
            # Check if the received data has enough size for PacketCarTelemetryData
            if len(data) >= PacketCarTelemetryData.size():
                # Unpack the PacketCarTelemetryData
                packet_car_telemetry_data = PacketCarTelemetryData(struct.unpack(PacketCarTelemetryData.format(), data[:PacketCarTelemetryData.size()]))
                return packet_car_telemetry_data
            
        # PacketCarStatusData
        elif packet_header.m_packetId == 7:
            # Check if the received data has enough size for PacketCarStatusData
            if len(data) >= PacketCarStatusData.size():
                # Unpack the PacketCarStatusData
                packet_car_status_data = PacketCarStatusData(struct.unpack(PacketCarStatusData.format(), data[:PacketCarStatusData.size()]))
                return packet_car_status_data
            
        # PacketFinalClassificationData
        elif packet_header.m_packetId == 8:
            # Check if the received data has enough size for PacketFinalClassificationData
            if len(data) >= PacketFinalClassificationData.size():
                # Unpack the PacketFinalClassificationData
                packet_final_classification_data = PacketFinalClassificationData(struct.unpack(PacketFinalClassificationData.format(), data[:PacketFinalClassificationData.size()]))
                return packet_final_classification_data
            
        # PacketLobbyInfoData
        elif packet_header.m_packetId == 9:
            # Check if the received data has enough size for PacketLobbyInfoData
            if len(data) >= PacketLobbyInfoData.size():
                # Unpack the PacketLobbyInfoData
                packet_lobby_info_data = PacketLobbyInfoData(struct.unpack(PacketLobbyInfoData.format(), data[:PacketLobbyInfoData.size()]))
                return packet_lobby_info_data

        # PacketCarDamageData    
        elif packet_header.m_packetId == 10:
            # Check if the received data has enough size for PacketCarDamageData
            if len(data) >= PacketCarDamageData.size():
                # Unpack the PacketCarDamageData
                packet_car_damage_data = PacketCarDamageData(struct.unpack(PacketCarDamageData.format(), data[:PacketCarDamageData.size()]))
                return packet_car_damage_data
            
        # PacketSessionHistoryData
        elif packet_header.m_packetId == 11:
            # Check if the received data has enough size for PacketSessionHistoryData
            if len(data) >= PacketSessionHistoryData.size():
                # Unpack the PacketSessionHistoryData
                packet_session_history_data = PacketSessionHistoryData(struct.unpack(PacketSessionHistoryData.format(), data[:PacketSessionHistoryData.size()]))
                return packet_session_history_data
            
        # PacketTyreSetsData
        elif packet_header.m_packetId == 12:
            # Check if the received data has enough size for PacketTyreSetsData
            if len(data) >= PacketTyreSetsData.size():
                # Unpack the PacketTyreSetsData
                packet_tyre_sets_data = PacketTyreSetsData(struct.unpack(PacketTyreSetsData.format(), data[:PacketTyreSetsData.size()]))
                return packet_tyre_sets_data
            
        # PacketMotionExData
        elif packet_header.m_packetId == 13:
            # Check if the received data has enough size for PacketMotionExData
            if len(data) >= PacketMotionExData.size():
                # Unpack the PacketMotionExData
                packet_motion_ex_data = PacketMotionExData(struct.unpack(PacketMotionExData.format(), data[:PacketMotionExData.size()]))
                return packet_motion_ex_data
            
        # Return the packet header if the packet ID is not recognized
        return packet_header
    
    # Return None if the received data does not have the size of the packet header
    return None

# Function to get the dashboard data
def get_dashboard_data():
    # Define the global variables
    global packet_header
    global packet_motion_data
    global packet_session_data
    global packet_lap_data
    global packet_event_data
    global packet_participants_data
    global packet_car_setup_data
    global packet_car_telemetry_data
    global packet_car_status_data
    global packet_final_classification_data
    global packet_lobby_info_data
    global packet_car_damage_data
    global packet_session_history_data
    global packet_tyre_sets_data
    global packet_motion_ex_data

    global player_index
    global last_best_lap_time

    # Listen for incoming packets
    listen()

    # Prints packet contents
    if PRINT_PACKETS:
        if (packet_header is not None):
            packet_header.print()
        if (packet_motion_data is not None):
            packet_motion_data.print()
        if (packet_session_data is not None):
            packet_session_data.print()
        if (packet_lap_data is not None):
            packet_lap_data.print()
        if (packet_event_data is not None):
            packet_event_data.print()
        if (packet_participants_data is not None):
            packet_participants_data.print()
        if (packet_car_setup_data is not None):
            packet_car_setup_data.print()
        if (packet_car_telemetry_data is not None):
            packet_car_telemetry_data.print()
        if (packet_car_status_data is not None):
            packet_car_status_data.print()
        if (packet_final_classification_data is not None):
            packet_final_classification_data.print()
        if (packet_lobby_info_data is not None):
            packet_lobby_info_data.print()
        if (packet_car_damage_data is not None):
            packet_car_damage_data.print()
        if (packet_session_history_data is not None):
            packet_session_history_data.print()
        if (packet_tyre_sets_data is not None):
            packet_tyre_sets_data.print()
        if (packet_motion_ex_data is not None):
            packet_motion_ex_data.print()

    # Find the player index
    if (packet_participants_data is not None):
        if (packet_participants_data.m_numActiveCars is not None):
            for i in range(packet_participants_data.m_numActiveCars):
                if (packet_participants_data.m_participants[i].m_aiControlled is not None and packet_participants_data.m_participants[i].m_aiControlled == 0):
                    player_index = i
                    break

    # Create object to return the dashboard data
    dashboard_data = {}

    # Simulation
    if (packet_motion_data is not None):
        if (packet_motion_data.m_carMotionData is not None):
            if (len(packet_motion_data.m_carMotionData) > player_index):
                if (packet_motion_data.m_carMotionData[player_index].m_worldPositionX is not None):
                    dashboard_data['world_position_x'] = packet_motion_data.m_carMotionData[player_index].m_worldPositionX
                if (packet_motion_data.m_carMotionData[player_index].m_worldPositionY is not None):
                    dashboard_data['world_position_y'] = packet_motion_data.m_carMotionData[player_index].m_worldPositionY
                if (packet_motion_data.m_carMotionData[player_index].m_worldPositionZ is not None):
                    dashboard_data['world_position_z'] = packet_motion_data.m_carMotionData[player_index].m_worldPositionZ
                if (packet_motion_data.m_carMotionData[player_index].m_worldForwardDirX is not None):
                    dashboard_data['world_forward_dir_x'] = packet_motion_data.m_carMotionData[player_index].m_worldForwardDirX
                if (packet_motion_data.m_carMotionData[player_index].m_worldForwardDirY is not None):
                    dashboard_data['world_forward_dir_y'] = packet_motion_data.m_carMotionData[player_index].m_worldForwardDirY
                if (packet_motion_data.m_carMotionData[player_index].m_worldForwardDirZ is not None):
                    dashboard_data['world_forward_dir_z'] = packet_motion_data.m_carMotionData[player_index].m_worldForwardDirZ
                if (packet_motion_data.m_carMotionData[player_index].m_yaw is not None):
                    dashboard_data['yaw'] = packet_motion_data.m_carMotionData[player_index].m_yaw
                    dashboard_data['world_yaw'] = packet_motion_data.m_carMotionData[player_index].m_yaw
                if (packet_motion_data.m_carMotionData[player_index].m_pitch is not None):
                    dashboard_data['pitch'] = packet_motion_data.m_carMotionData[player_index].m_pitch
                    dashboard_data['world_pitch'] = packet_motion_data.m_carMotionData[player_index].m_pitch
                if (packet_motion_data.m_carMotionData[player_index].m_roll is not None):
                    dashboard_data['roll'] = packet_motion_data.m_carMotionData[player_index].m_roll
                    dashboard_data['world_roll'] = packet_motion_data.m_carMotionData[player_index].m_roll
                if (packet_motion_data.m_carMotionData[player_index].m_gForceLateral is not None):
                    dashboard_data['g_force_lateral'] = packet_motion_data.m_carMotionData[player_index].m_gForceLateral
                if (packet_motion_data.m_carMotionData[player_index].m_gForceLongitudinal is not None):
                    dashboard_data['g_force_longitudinal'] = packet_motion_data.m_carMotionData[player_index].m_gForceLongitudinal
                if (packet_motion_data.m_carMotionData[player_index].m_gForceVertical is not None):
                    dashboard_data['g_force_vertical'] = packet_motion_data.m_carMotionData[player_index].m_gForceVertical
    if (packet_motion_ex_data is not None):
        if (packet_motion_ex_data.m_localVelocityX is not None):
            dashboard_data['local_velocity_x'] = packet_motion_ex_data.m_localVelocityX
        if (packet_motion_ex_data.m_localVelocityY is not None):
            dashboard_data['local_velocity_y'] = packet_motion_ex_data.m_localVelocityY
        if (packet_motion_ex_data.m_localVelocityZ is not None):
            dashboard_data['local_velocity_z'] = packet_motion_ex_data.m_localVelocityZ
        if (packet_motion_ex_data.m_angularVelocityX is not None):
            dashboard_data['angular_velocity_x'] = packet_motion_ex_data.m_angularVelocityX
        if (packet_motion_ex_data.m_angularVelocityY is not None):
            dashboard_data['angular_velocity_y'] = packet_motion_ex_data.m_angularVelocityY
        if (packet_motion_ex_data.m_angularVelocityZ is not None):
            dashboard_data['angular_velocity_z'] = packet_motion_ex_data.m_angularVelocityZ
        if (packet_motion_ex_data.m_angularAccelerationX is not None):
            dashboard_data['angular_acceleration_x'] = packet_motion_ex_data.m_angularAccelerationX
        if (packet_motion_ex_data.m_angularAccelerationY is not None):
            dashboard_data['angular_acceleration_y'] = packet_motion_ex_data.m_angularAccelerationY
        if (packet_motion_ex_data.m_angularAccelerationZ is not None):
            dashboard_data['angular_acceleration_z'] = packet_motion_ex_data.m_angularAccelerationZ
        if (packet_motion_ex_data.m_frontWheelsAngle is not None):
            dashboard_data['front_wheels_angle'] = packet_motion_ex_data.m_frontWheelsAngle

    # Velocity
    if (packet_car_telemetry_data is not None):
        if (packet_car_telemetry_data.m_carTelemetryData is not None):
            if (len(packet_car_telemetry_data.m_carTelemetryData) > player_index):
                if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_speed is not None):
                    dashboard_data['kmh'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_speed
                if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_engineRPM is not None):
                    dashboard_data['rpm'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_engineRPM
                if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_gear is not None):
                    dashboard_data['gear'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_gear

    # Fuel
    if (packet_car_status_data is not None):
        if (packet_car_status_data.m_carStatusData is not None):
            if (len(packet_car_status_data.m_carStatusData) > player_index):
                if (packet_car_status_data.m_carStatusData[player_index].m_fuelInTank is not None):
                    dashboard_data['fuel_current'] = packet_car_status_data.m_carStatusData[player_index].m_fuelInTank
                if (packet_car_status_data.m_carStatusData[player_index].m_fuelCapacity is not None):
                    dashboard_data['fuel_capacity'] = packet_car_status_data.m_carStatusData[player_index].m_fuelCapacity
                if (packet_car_status_data.m_carStatusData[player_index].m_fuelRemainingLaps is not None):
                    dashboard_data['fuel_laps'] = packet_car_status_data.m_carStatusData[player_index].m_fuelRemainingLaps

    # Lap Times
    if (packet_lap_data is not None):
        if (packet_lap_data.m_lapData is not None and len(packet_lap_data.m_lapData) > player_index):
            if (packet_lap_data.m_lapData[player_index].m_lastLapTimeInMS is not None):
                dashboard_data['last_lap_time'] = format_time(packet_lap_data.m_lapData[player_index].m_lastLapTimeInMS)
            if (packet_lap_data.m_lapData[player_index].m_currentLapTimeInMS is not None):
                dashboard_data['current_lap_time'] = format_time(packet_lap_data.m_lapData[player_index].m_currentLapTimeInMS)
            if (packet_lap_data.m_lapData[player_index].m_deltaToRaceLeaderInMS is not None):
                dashboard_data['delta_lap_time'] = format_time(packet_lap_data.m_lapData[player_index].m_deltaToRaceLeaderInMS)
    if (packet_final_classification_data is not None):
        if (packet_final_classification_data.m_classificationData is not None and len(packet_final_classification_data.m_classificationData) > player_index):
            if (packet_final_classification_data.m_classificationData[player_index].m_bestLapTimeInMS is not None):
                dashboard_data['best_lap_time'] = format_time(packet_final_classification_data.m_classificationData[player_index].m_bestLapTimeInMS)
    if (dashboard_data.get('best_lap_time') is None and packet_session_history_data is not None and packet_session_history_data.m_carIdx is not None and packet_session_history_data.m_carIdx is player_index):
        if (packet_session_history_data.m_lapHistoryData is not None):
            dashboard_data['best_lap_time'] = format_time(get_best_time(packet_session_history_data.m_lapHistoryData))

    # DRS
    if (packet_car_telemetry_data is not None):
      if (packet_car_telemetry_data.m_carTelemetryData is not None):
          if (len(packet_car_telemetry_data.m_carTelemetryData) > player_index):
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_drs is not None):
                  dashboard_data['drs'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_drs

    # ERS
    if (packet_car_status_data is not None):
      if (packet_car_status_data.m_carStatusData is not None):
          if (len(packet_car_status_data.m_carStatusData) > player_index):
              if (packet_car_status_data.m_carStatusData[player_index].m_ersDeployMode is not None):
                  dashboard_data['ers_mode'] = parse_ers_deploy_mode(packet_car_status_data.m_carStatusData[player_index].m_ersDeployMode)
              if (packet_car_status_data.m_carStatusData[player_index].m_ersStoreEnergy is not None):
                  dashboard_data['ers_energy'] = packet_car_status_data.m_carStatusData[player_index].m_ersStoreEnergy / 4000000 * 100
              if (packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUK is not None and packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUK > 0 and packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUH is not None and packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUH > 0 and packet_car_status_data.m_carStatusData[player_index].m_ersDeployedThisLap is not None and packet_car_status_data.m_carStatusData[player_index].m_ersDeployedThisLap > 0):
                  dashboard_data['ers_percentage'] = round((packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUK + packet_car_status_data.m_carStatusData[player_index].m_ersHarvestedThisLapMGUH) / packet_car_status_data.m_carStatusData[player_index].m_ersDeployedThisLap * 100, 2)

    # Circuit
    if (packet_session_data is not None):
        if (packet_session_data.m_trackId is not None):
            dashboard_data['track'] = get_track_name(packet_session_data.m_trackId)
        if (packet_session_data.m_totalLaps is not None):
            dashboard_data['total_laps'] = packet_session_data.m_totalLaps
    if (packet_lap_data is not None):
        if (packet_lap_data.m_lapData is not None and len(packet_lap_data.m_lapData) > player_index):
            if (packet_lap_data.m_lapData[player_index].m_currentLapNum is not None):
                dashboard_data['current_lap'] = packet_lap_data.m_lapData[player_index].m_currentLapNum
            if (packet_lap_data.m_lapData[player_index].m_carPosition is not None):
                dashboard_data['position'] = packet_lap_data.m_lapData[player_index].m_carPosition
    
    # Car Management
    if (packet_car_telemetry_data is not None):
      if (packet_car_telemetry_data.m_carTelemetryData is not None):
          if (len(packet_car_telemetry_data.m_carTelemetryData) > player_index):
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_brakesTemperature is not None):
                  dashboard_data['brakes_temperature'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_brakesTemperature
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresSurfaceTemperature is not None):
                  dashboard_data['tyres_surface_temperature'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresSurfaceTemperature
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresInnerTemperature is not None):
                  dashboard_data['tyres_inner_temperature'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresInnerTemperature
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresPressure is not None):
                  dashboard_data['tyres_pressure'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_tyresPressure
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_surfaceType is not None):
                  dashboard_data['surface_type'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_surfaceType
              if (packet_car_telemetry_data.m_carTelemetryData[player_index].m_engineTemperature is not None):
                  dashboard_data['engine_temperature'] = packet_car_telemetry_data.m_carTelemetryData[player_index].m_engineTemperature
    if (packet_car_damage_data is not None):
      if (packet_car_damage_data.m_carDamageData is not None):
          if (len(packet_car_damage_data.m_carDamageData) > player_index):
              if (packet_car_damage_data.m_carDamageData[player_index].m_engineDamage is not None):
                  dashboard_data['engine_damage'] = packet_car_damage_data.m_carDamageData[player_index].m_engineDamage
              if (packet_car_damage_data.m_carDamageData[player_index].m_gearBoxDamage is not None):
                  dashboard_data['gearbox_damage'] = packet_car_damage_data.m_carDamageData[player_index].m_gearBoxDamage
              if (packet_car_damage_data.m_carDamageData[player_index].m_tyresWear is not None and packet_car_damage_data.m_carDamageData[player_index].m_tyresWear[0] is not 100):
                  dashboard_data['tyres_wear'] = packet_car_damage_data.m_carDamageData[player_index].m_tyresWear 
              if (packet_car_damage_data.m_carDamageData[player_index].m_tyresDamage is not None and packet_car_damage_data.m_carDamageData[player_index].m_tyresDamage[0] is not 100):
                  dashboard_data['tyres_damage'] = packet_car_damage_data.m_carDamageData[player_index].m_tyresDamage

    # Tyre Compound Type
    if (packet_car_status_data is not None):
        if (packet_car_status_data.m_carStatusData is not None):
            if (len(packet_car_status_data.m_carStatusData) > player_index):
                if (packet_car_status_data.m_carStatusData[player_index].m_actualTyreCompound is not None):
                    dashboard_data['tyre_compound'] = packet_car_status_data.m_carStatusData[player_index].m_actualTyreCompound
    
    # Weather Forecast
    if (packet_session_data is not None):
        if (packet_session_data.m_weatherForecastSamples is not None):
            if (packet_session_data.m_timeOfDay is not None):
                dashboard_data['time_of_day'] = time_since_midnight(packet_session_data.m_timeOfDay)
            if (len(packet_session_data.m_weatherForecastSamples) > WEATHER_FORECAST_INDEX):
                if (packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_weather is not None):
                  dashboard_data['weather_forecast_weather'] = get_weather(packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_weather)
                if (packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_trackTemperature is not None):
                  dashboard_data['weather_forecast_track_temperature'] = packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_trackTemperature
                if (packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_airTemperature is not None):
                  dashboard_data['weather_forecast_air_temperature'] = packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_airTemperature
                if (packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_rainPercentage is not None):
                  dashboard_data['weather_forecast_rain_percentage'] = packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_rainPercentage
                if (packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_timeOffset is not None):
                  dashboard_data['weather_forecast_time_offset'] = packet_session_data.m_weatherForecastSamples[WEATHER_FORECAST_INDEX].m_timeOffset
            

    # Clean up the data
    if dashboard_data.get('fuel_current') is not None and dashboard_data.get('fuel_capacity') is not None:
        if dashboard_data.get('fuel_capacity') > 0 and dashboard_data.get('fuel_current') > 0:
            dashboard_data['fuel_percent'] = round((dashboard_data.get('fuel_current') / dashboard_data.get('fuel_capacity')) * 100, 2)
    if dashboard_data.get('fuel_laps') is not None:
        if dashboard_data.get('fuel_laps') > 0:
          dashboard_data['fuel_laps'] = round(dashboard_data.get('fuel_laps'), 2)
    if dashboard_data.get('world_position_x') is not None:
        dashboard_data['world_position_x'] = round(dashboard_data.get('world_position_x'), 2)
    if dashboard_data.get('world_position_y') is not None:
        dashboard_data['world_position_y'] = round(dashboard_data.get('world_position_y'), 2)
    if dashboard_data.get('world_position_z') is not None:
        dashboard_data['world_position_z'] = round(dashboard_data.get('world_position_z'), 2)
    if dashboard_data.get('world_forward_dir_x') is not None:
        dashboard_data['world_forward_dir_x'] = round(dashboard_data.get('world_forward_dir_x'), 2)
    if dashboard_data.get('world_forward_dir_y') is not None:
        dashboard_data['world_forward_dir_y'] = round(dashboard_data.get('world_forward_dir_y'), 2)
    if dashboard_data.get('world_forward_dir_z') is not None:
        dashboard_data['world_forward_dir_z'] = round(dashboard_data.get('world_forward_dir_z'), 2)
    if dashboard_data.get('world_yaw') is not None:
        dashboard_data['world_yaw'] = round(dashboard_data.get('world_yaw'), 2)
    if dashboard_data.get('world_pitch') is not None:
        dashboard_data['world_pitch'] = round(dashboard_data.get('world_pitch'), 2)
    if dashboard_data.get('world_roll') is not None:
        dashboard_data['world_roll'] = round(dashboard_data.get('world_roll'), 2)
    if dashboard_data.get('g_force_lateral') is not None:
        dashboard_data['g_force_lateral'] = round(dashboard_data.get('g_force_lateral'), 2)
    if dashboard_data.get('g_force_longitudinal') is not None:
        dashboard_data['g_force_longitudinal'] = round(dashboard_data.get('g_force_longitudinal'), 2)
    if dashboard_data.get('g_force_vertical') is not None:
        dashboard_data['g_force_vertical'] = round(dashboard_data.get('g_force_vertical'), 2)
    if dashboard_data.get('local_velocity_x') is not None:
        dashboard_data['local_velocity_x'] = round(dashboard_data.get('local_velocity_x'), 2)
    if dashboard_data.get('local_velocity_y') is not None:
        dashboard_data['local_velocity_y'] = round(dashboard_data.get('local_velocity_y'), 2)
    if dashboard_data.get('local_velocity_z') is not None:
        dashboard_data['local_velocity_z'] = round(dashboard_data.get('local_velocity_z'), 2)
    if dashboard_data.get('angular_velocity_x') is not None:
        dashboard_data['angular_velocity_x'] = round(dashboard_data.get('angular_velocity_x'), 2)
    if dashboard_data.get('angular_velocity_y') is not None:
        dashboard_data['angular_velocity_y'] = round(dashboard_data.get('angular_velocity_y'), 2)
    if dashboard_data.get('angular_velocity_z') is not None:
        dashboard_data['angular_velocity_z'] = round(dashboard_data.get('angular_velocity_z'), 2)
    if dashboard_data.get('angular_acceleration_x') is not None:
        dashboard_data['angular_acceleration_x'] = round(dashboard_data.get('angular_acceleration_x'), 2)
    if dashboard_data.get('angular_acceleration_y') is not None:
        dashboard_data['angular_acceleration_y'] = round(dashboard_data.get('angular_acceleration_y'), 2)
    if dashboard_data.get('angular_acceleration_z') is not None:
        dashboard_data['angular_acceleration_z'] = round(dashboard_data.get('angular_acceleration_z'), 2)
    if dashboard_data.get('front_wheels_angle') is not None:
        dashboard_data['front_wheels_angle'] = round(dashboard_data.get('front_wheels_angle') % 360, 2)
    if dashboard_data.get('ers_energy') is not None:
        dashboard_data['ers_energy'] = round(dashboard_data.get('ers_energy'), 2)
    
    # Handle empty data
    if (dashboard_data.get('kmh') is None):
        dashboard_data['kmh'] = EMPTY_VELOCITY
    if (dashboard_data.get('rpm') is None):
        dashboard_data['rpm'] = EMPTY_VELOCITY
    if (dashboard_data.get('gear') is None):
        dashboard_data['gear'] = EMPTY_VELOCITY
    if (dashboard_data.get('fuel_current') is None):
        dashboard_data['fuel_current'] = EMPTY_FUEL
    if (dashboard_data.get('fuel_capacity') is None):
        dashboard_data['fuel_capacity'] = EMPTY_FUEL
    if (dashboard_data.get('current_lap_time') is None):
        dashboard_data['current_lap_time'] = EMPTY_LAP_TIME
    if (dashboard_data.get('last_lap_time') is None):
        dashboard_data['last_lap_time'] = EMPTY_LAP_TIME
    if (dashboard_data.get('best_lap_time') is None):
        dashboard_data['best_lap_time'] = EMPTY_LAP_TIME
    else:
        last_best_lap_time = dashboard_data.get('best_lap_time')
    if last_best_lap_time is None or last_best_lap_time is EMPTY_LAP_TIME:
        last_best_lap_time = dashboard_data['last_lap_time']
    if (dashboard_data.get('delta_lap_time') is None):
        dashboard_data['delta_lap_time'] = EMPTY_LAP_TIME
    if (dashboard_data.get('best_lap_time') is EMPTY_LAP_TIME):
        dashboard_data['best_lap_time'] = last_best_lap_time
    if (dashboard_data.get('fuel_percent') is None):
        dashboard_data['fuel_percent'] = EMPTY_FUEL
    if (dashboard_data.get('fuel_laps') is None):
        dashboard_data['fuel_laps'] = EMPTY_FUEL_LAPS
    if (dashboard_data.get('drs') is None):
        dashboard_data['drs'] = False
    if (dashboard_data.get('ers_mode') is None):
        dashboard_data['ers_mode'] = "None"
    if (dashboard_data.get('ers_percentage') is None):
        dashboard_data['ers_percentage'] = EMPTY_FUEL
    if (dashboard_data.get('ers_energy') is None):
       dashboard_data['ers_energy'] = EMPTY_FUEL
    if (dashboard_data.get('track') is None):
        dashboard_data['track'] = "Unknown"
    if (dashboard_data.get('total_laps') is None):
        dashboard_data['total_laps'] = 0
    if (dashboard_data.get('current_lap') is None):
        dashboard_data['current_lap'] = 0
    if (dashboard_data.get('position') is None):
        dashboard_data['position'] = 0
    if (dashboard_data.get('world_position_x') is None):
        dashboard_data['world_position_x'] = 0
    if (dashboard_data.get('world_position_y') is None):
        dashboard_data['world_position_y'] = 0
    if (dashboard_data.get('world_position_z') is None):
        dashboard_data['world_position_z'] = 0
    if (dashboard_data.get('world_forward_dir_x') is None):
        dashboard_data['world_forward_dir_x'] = 0
    if (dashboard_data.get('world_forward_dir_y') is None):
        dashboard_data['world_forward_dir_y'] = 0
    if (dashboard_data.get('world_forward_dir_z') is None):
        dashboard_data['world_forward_dir_z'] = 0
    if (dashboard_data.get('world_yaw') is None):
        dashboard_data['world_yaw'] = 0
    if (dashboard_data.get('world_pitch') is None):
        dashboard_data['world_pitch'] = 0
    if (dashboard_data.get('world_roll') is None):
        dashboard_data['world_roll'] = 0
    if (dashboard_data.get('g_force_lateral') is None):
        dashboard_data['g_force_lateral'] = 0
    if (dashboard_data.get('g_force_longitudinal') is None):
        dashboard_data['g_force_longitudinal'] = 0
    if (dashboard_data.get('g_force_vertical') is None):
        dashboard_data['g_force_vertical'] = 0
    if (dashboard_data.get('local_velocity_x') is None):
        dashboard_data['local_velocity_x'] = 0
    if (dashboard_data.get('local_velocity_y') is None):
        dashboard_data['local_velocity_y'] = 0
    if (dashboard_data.get('local_velocity_z') is None):
        dashboard_data['local_velocity_z'] = 0
    if (dashboard_data.get('angular_velocity_x') is None):
        dashboard_data['angular_velocity_x'] = 0
    if (dashboard_data.get('angular_velocity_y') is None):
        dashboard_data['angular_velocity_y'] = 0
    if (dashboard_data.get('angular_velocity_z') is None):
        dashboard_data['angular_velocity_z'] = 0
    if (dashboard_data.get('angular_acceleration_x') is None):
        dashboard_data['angular_acceleration_x'] = 0
    if (dashboard_data.get('angular_acceleration_y') is None):
        dashboard_data['angular_acceleration_y'] = 0
    if (dashboard_data.get('angular_acceleration_z') is None):
        dashboard_data['angular_acceleration_z'] = 0
    if (dashboard_data.get('front_wheels_angle') is None):
        dashboard_data['front_wheels_angle'] = 0
    if (dashboard_data.get('tyre_compound') is None):
        dashboard_data['tyre_compound'] = "Unknown"
    if (dashboard_data.get('brakes_temperature') is None):
        dashboard_data['brakes_temperature'] = DEFAULT_TYRE_DATA
    if (dashboard_data.get('tyres_surface_temperature') is None):
        dashboard_data['tyres_surface_temperature'] = DEFAULT_TYRE_DATA
    if (dashboard_data.get('tyres_inner_temperature') is None):
        dashboard_data['tyres_inner_temperature'] = DEFAULT_TYRE_DATA
    if (dashboard_data.get('tyres_pressure') is None):
        dashboard_data['tyres_pressure'] = DEFAULT_TYRE_DATA
    if (dashboard_data.get('surface_type') is None):
        dashboard_data['surface_type'] = DEFAULT_TYRE_DATA
    if (dashboard_data.get('engine_temperature') is None):
        dashboard_data['engine_temperature'] = 0
    if (dashboard_data.get('engine_damage') is None):
        dashboard_data['engine_damage'] = 0
    if (dashboard_data.get('gearbox_damage') is None):
        dashboard_data['gearbox_damage'] = 0
    if (dashboard_data.get('tyres_wear') is None):
        dashboard_data['tyres_wear'] = DEFAULT_TYRE_WEAR
    if (dashboard_data.get('tyres_damage') is None):
        dashboard_data['tyres_damage'] = DEFAULT_TYRE_WEAR
    if (dashboard_data.get('time_of_day') is None):
        dashboard_data['time_of_day'] = "00:00"
    if (dashboard_data.get('weather_forecast_weather') is None):
        dashboard_data['weather_forecast_weather'] = "Unknown"
    if (dashboard_data.get('weather_forecast_track_temperature') is None):
        dashboard_data['weather_forecast_track_temperature'] = 0
    if (dashboard_data.get('weather_forecast_air_temperature') is None):
        dashboard_data['weather_forecast_air_temperature'] = 0
    if (dashboard_data.get('weather_forecast_rain_percentage') is None):
        dashboard_data['weather_forecast_rain_percentage'] = 0
    if (dashboard_data.get('weather_forecast_time_offset') is None):
        dashboard_data['weather_forecast_time_offset'] = 0

    # Round data
    for i in range(len(dashboard_data.get('tyres_wear'))):
        dashboard_data['tyres_wear'][i] = round(dashboard_data['tyres_wear'][i], 2)
    for i in range(len(dashboard_data.get('tyres_damage'))):
        dashboard_data['tyres_damage'][i] = round(dashboard_data['tyres_damage'][i], 2)

    # Return the dashboard data
    return dashboard_data

# Function to get the time since midnight
def time_since_midnight(time):
    hours, minutes = divmod(time, 60)
    return '{:02d}:{:02d}'.format(hours, minutes)

# Function to get the weather from the weather ID
def get_weather(weather):
    if weather == 0:
        return "Clear"
    elif weather == 1:
        return "Light Clouds"
    elif weather == 2:
        return "Overcast"
    elif weather == 3:
        return "Light Rain"
    elif weather == 4:
        return "Heavy Rain"
    elif weather == 5:
        return "Storm"
    else:
        return "Unknown"

# Function to calculate the tyre wear percentage
def tyre_percentage(tyre_wear):
    for i in range(4):
        tyre_wear[i] = round(DEFAULT_TYRE_WEAR[i] - tyre_wear[i], 2) if tyre_wear[i] is not None else DEFAULT_TYRE_WEAR[i]
    return tyre_wear

# Function to parse the ERS deploy mode
def parse_ers_deploy_mode(ers_deploy_mode):
    if ers_deploy_mode == 0:
        return "None"
    elif ers_deploy_mode == 1:
        return "Medium"
    elif ers_deploy_mode == 2:
        return "Hotlap"
    elif ers_deploy_mode == 3:
        return "Overtake"
    else:
        return "Unknown"

# Function to get the best lap time from the lap history data
def get_best_time(lap_times):
    best_time = 999999999
    for lap_time in lap_times:
        if lap_time.m_lapTimeInMS is not None:
            if lap_time.m_lapTimeInMS > 0 and lap_time.m_lapTimeInMS < best_time:
                best_time = lap_time.m_lapTimeInMS
    return best_time if best_time != 999999999 else 0

# Function to get the track name from the track ID
def get_track_name(track_id):
    if track_id == -1:
        return "Undefined"
    if track_id == 0:
        return "Melbourne"
    if track_id == 1:
        return "Paul Ricard"
    if track_id == 2:
        return "Shanghai"
    if track_id == 3:
        return "Bahrain"
    if track_id == 4:
        return "Catalunya"
    if track_id == 5:
        return "Monaco"
    if track_id == 6:
        return "Montreal"
    if track_id == 7:
        return "Silverstone"
    if track_id == 8:
        return "Hockenheim"
    if track_id == 9:
        return "Hungaroring"
    if track_id == 10:
        return "Spa"
    if track_id == 11:
        return "Monza"
    if track_id == 12:
        return "Singapore"
    if track_id == 13:
        return "Suzuka"
    if track_id == 14:
        return "Abu Dhabi"
    if track_id == 15:
        return "Texas"
    if track_id == 16:
        return "Brazil"
    if track_id == 17:
        return "Austria"
    if track_id == 18:
        return "Sochi"
    if track_id == 19:
        return "Mexico"
    if track_id == 20:
        return "Azerbaijan"
    if track_id == 21:
        return "Sakhir Short"
    if track_id == 22:
        return "Silverstone Short"
    if track_id == 23:
        return "Texas Short"
    if track_id == 24:
        return "Suzuka Short"
    if track_id == 25:
        return "Hanoi"
    if track_id == 26:
        return "Zandvoort"
    if track_id == 27:
        return "Imola"
    if track_id == 28:
        return "Portimão"
    if track_id == 29:
        return "Jeddah"
    if track_id == 30:
        return "Miami"
    if track_id == 31:
        return "Las Vegas"
    if track_id == 32:
        return "Losail"
    return "Unknown"

# Function to format the time in milliseconds as "MM:SS:mmm"
def format_time(milliseconds):
    minutes, milliseconds = divmod(milliseconds, 60000)
    seconds, milliseconds = divmod(milliseconds, 1000)
    
    # Format the result as "MM:SS:mmm"
    return '{:02d}:{:02d}:{:03d}'.format(minutes, seconds, milliseconds)

# Function to clear the buffer
def clear_buffer(socket):
    while True:
        data = None
        try:
            data = socket.recv(1024)
        except:
            break
        if data is None or len(data) == 0:
            break