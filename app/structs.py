import struct

class CarDamageData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<ffffBBBBBBBBBBBBBBBBBBBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(CarDamageData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_tyresWear = [unpacked_data[0], unpacked_data[1], unpacked_data[2], unpacked_data[3]]
		self.m_tyresDamage = [unpacked_data[4], unpacked_data[5], unpacked_data[6], unpacked_data[7]]
		self.m_brakesDamage = [unpacked_data[8], unpacked_data[9], unpacked_data[10], unpacked_data[11]]
		self.m_frontLeftWingDamage = unpacked_data[12]
		self.m_frontRightWingDamage = unpacked_data[13]
		self.m_rearWingDamage = unpacked_data[14]
		self.m_floorDamage = unpacked_data[15]
		self.m_diffuserDamage = unpacked_data[16]
		self.m_sidepodDamage = unpacked_data[17]
		self.m_drsFault = unpacked_data[18]
		self.m_ersFault = unpacked_data[19]
		self.m_gearBoxDamage = unpacked_data[20]
		self.m_engineDamage = unpacked_data[21]
		self.m_engineMGUHWear = unpacked_data[22]
		self.m_engineESWear = unpacked_data[23]
		self.m_engineCEWear = unpacked_data[24]
		self.m_engineICEWear = unpacked_data[25]
		self.m_engineMGUKWear = unpacked_data[26]
		self.m_engineTCWear = unpacked_data[27]
		self.m_engineBlown = unpacked_data[28]
		self.m_engineSeized = unpacked_data[29]

	# To string
	def __str__(self):
		text = "--== <CarDamageData> ==--\n"
		text += f"m_tyresWear: {self.m_tyresWear}\n"
		text += f"m_tyresDamage: {self.m_tyresDamage}\n"
		text += f"m_brakesDamage: {self.m_brakesDamage}\n"
		text += f"m_frontLeftWingDamage: {self.m_frontLeftWingDamage}\n"
		text += f"m_frontRightWingDamage: {self.m_frontRightWingDamage}\n"
		text += f"m_rearWingDamage: {self.m_rearWingDamage}\n"
		text += f"m_floorDamage: {self.m_floorDamage}\n"
		text += f"m_diffuserDamage: {self.m_diffuserDamage}\n"
		text += f"m_sidepodDamage: {self.m_sidepodDamage}\n"
		text += f"m_drsFault: {self.m_drsFault}\n"
		text += f"m_ersFault: {self.m_ersFault}\n"
		text += f"m_gearBoxDamage: {self.m_gearBoxDamage}\n"
		text += f"m_engineDamage: {self.m_engineDamage}\n"
		text += f"m_engineMGUHWear: {self.m_engineMGUHWear}\n"
		text += f"m_engineESWear: {self.m_engineESWear}\n"
		text += f"m_engineCEWear: {self.m_engineCEWear}\n"
		text += f"m_engineICEWear: {self.m_engineICEWear}\n"
		text += f"m_engineMGUKWear: {self.m_engineMGUKWear}\n"
		text += f"m_engineTCWear: {self.m_engineTCWear}\n"
		text += f"m_engineBlown: {self.m_engineBlown}\n"
		text += f"m_engineSeized: {self.m_engineSeized}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "CarDamageData"
		dictionary["m_tyresWear"] = self.m_tyresWear
		dictionary["m_tyresDamage"] = self.m_tyresDamage
		dictionary["m_brakesDamage"] = self.m_brakesDamage
		dictionary["m_frontLeftWingDamage"] = self.m_frontLeftWingDamage
		dictionary["m_frontRightWingDamage"] = self.m_frontRightWingDamage
		dictionary["m_rearWingDamage"] = self.m_rearWingDamage
		dictionary["m_floorDamage"] = self.m_floorDamage
		dictionary["m_diffuserDamage"] = self.m_diffuserDamage
		dictionary["m_sidepodDamage"] = self.m_sidepodDamage
		dictionary["m_drsFault"] = self.m_drsFault
		dictionary["m_ersFault"] = self.m_ersFault
		dictionary["m_gearBoxDamage"] = self.m_gearBoxDamage
		dictionary["m_engineDamage"] = self.m_engineDamage
		dictionary["m_engineMGUHWear"] = self.m_engineMGUHWear
		dictionary["m_engineESWear"] = self.m_engineESWear
		dictionary["m_engineCEWear"] = self.m_engineCEWear
		dictionary["m_engineICEWear"] = self.m_engineICEWear
		dictionary["m_engineMGUKWear"] = self.m_engineMGUKWear
		dictionary["m_engineTCWear"] = self.m_engineTCWear
		dictionary["m_engineBlown"] = self.m_engineBlown
		dictionary["m_engineSeized"] = self.m_engineSeized
		return dictionary

class CarMotionData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<ffffffhhhhhhffffff"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(CarMotionData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_worldPositionX = unpacked_data[0]
		self.m_worldPositionY = unpacked_data[1]
		self.m_worldPositionZ = unpacked_data[2]
		self.m_worldVelocityX = unpacked_data[3]
		self.m_worldVelocityY = unpacked_data[4]
		self.m_worldVelocityZ = unpacked_data[5]
		self.m_worldForwardDirX = unpacked_data[6]
		self.m_worldForwardDirY = unpacked_data[7]
		self.m_worldForwardDirZ = unpacked_data[8]
		self.m_worldRightDirX = unpacked_data[9]
		self.m_worldRightDirY = unpacked_data[10]
		self.m_worldRightDirZ = unpacked_data[11]
		self.m_gForceLateral = unpacked_data[12]
		self.m_gForceLongitudinal = unpacked_data[13]
		self.m_gForceVertical = unpacked_data[14]
		self.m_yaw = unpacked_data[15]
		self.m_pitch = unpacked_data[16]
		self.m_roll = unpacked_data[17]

	# To string
	def __str__(self):
		text = "--== <CarMotionData> ==--\n"
		text += f"m_worldPositionX: {self.m_worldPositionX}\n"
		text += f"m_worldPositionY: {self.m_worldPositionY}\n"
		text += f"m_worldPositionZ: {self.m_worldPositionZ}\n"
		text += f"m_worldVelocityX: {self.m_worldVelocityX}\n"
		text += f"m_worldVelocityY: {self.m_worldVelocityY}\n"
		text += f"m_worldVelocityZ: {self.m_worldVelocityZ}\n"
		text += f"m_worldForwardDirX: {self.m_worldForwardDirX}\n"
		text += f"m_worldForwardDirY: {self.m_worldForwardDirY}\n"
		text += f"m_worldForwardDirZ: {self.m_worldForwardDirZ}\n"
		text += f"m_worldRightDirX: {self.m_worldRightDirX}\n"
		text += f"m_worldRightDirY: {self.m_worldRightDirY}\n"
		text += f"m_worldRightDirZ: {self.m_worldRightDirZ}\n"
		text += f"m_gForceLateral: {self.m_gForceLateral}\n"
		text += f"m_gForceLongitudinal: {self.m_gForceLongitudinal}\n"
		text += f"m_gForceVertical: {self.m_gForceVertical}\n"
		text += f"m_yaw: {self.m_yaw}\n"
		text += f"m_pitch: {self.m_pitch}\n"
		text += f"m_roll: {self.m_roll}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "CarMotionData"
		dictionary["m_worldPositionX"] = self.m_worldPositionX
		dictionary["m_worldPositionY"] = self.m_worldPositionY
		dictionary["m_worldPositionZ"] = self.m_worldPositionZ
		dictionary["m_worldVelocityX"] = self.m_worldVelocityX
		dictionary["m_worldVelocityY"] = self.m_worldVelocityY
		dictionary["m_worldVelocityZ"] = self.m_worldVelocityZ
		dictionary["m_worldForwardDirX"] = self.m_worldForwardDirX
		dictionary["m_worldForwardDirY"] = self.m_worldForwardDirY
		dictionary["m_worldForwardDirZ"] = self.m_worldForwardDirZ
		dictionary["m_worldRightDirX"] = self.m_worldRightDirX
		dictionary["m_worldRightDirY"] = self.m_worldRightDirY
		dictionary["m_worldRightDirZ"] = self.m_worldRightDirZ
		dictionary["m_gForceLateral"] = self.m_gForceLateral
		dictionary["m_gForceLongitudinal"] = self.m_gForceLongitudinal
		dictionary["m_gForceVertical"] = self.m_gForceVertical
		dictionary["m_yaw"] = self.m_yaw
		dictionary["m_pitch"] = self.m_pitch
		dictionary["m_roll"] = self.m_roll
		return dictionary

class CarSetupData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBffffBBBBBBBBffffBf"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(CarSetupData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_frontWing = unpacked_data[0]
		self.m_rearWing = unpacked_data[1]
		self.m_onThrottle = unpacked_data[2]
		self.m_offThrottle = unpacked_data[3]
		self.m_frontCamber = unpacked_data[4]
		self.m_rearCamber = unpacked_data[5]
		self.m_frontToe = unpacked_data[6]
		self.m_rearToe = unpacked_data[7]
		self.m_frontSuspension = unpacked_data[8]
		self.m_rearSuspension = unpacked_data[9]
		self.m_frontAntiRollBar = unpacked_data[10]
		self.m_rearAntiRollBar = unpacked_data[11]
		self.m_frontSuspensionHeight = unpacked_data[12]
		self.m_rearSuspensionHeight = unpacked_data[13]
		self.m_brakePressure = unpacked_data[14]
		self.m_brakeBias = unpacked_data[15]
		self.m_rearLeftTyrePressure = unpacked_data[16]
		self.m_rearRightTyrePressure = unpacked_data[17]
		self.m_frontLeftTyrePressure = unpacked_data[18]
		self.m_frontRightTyrePressure = unpacked_data[19]
		self.m_ballast = unpacked_data[20]
		self.m_fuelLoad = unpacked_data[21]

	# To string
	def __str__(self):
		text = "--== <CarSetupData> ==--\n"
		text += f"m_frontWing: {self.m_frontWing}\n"
		text += f"m_rearWing: {self.m_rearWing}\n"
		text += f"m_onThrottle: {self.m_onThrottle}\n"
		text += f"m_offThrottle: {self.m_offThrottle}\n"
		text += f"m_frontCamber: {self.m_frontCamber}\n"
		text += f"m_rearCamber: {self.m_rearCamber}\n"
		text += f"m_frontToe: {self.m_frontToe}\n"
		text += f"m_rearToe: {self.m_rearToe}\n"
		text += f"m_frontSuspension: {self.m_frontSuspension}\n"
		text += f"m_rearSuspension: {self.m_rearSuspension}\n"
		text += f"m_frontAntiRollBar: {self.m_frontAntiRollBar}\n"
		text += f"m_rearAntiRollBar: {self.m_rearAntiRollBar}\n"
		text += f"m_frontSuspensionHeight: {self.m_frontSuspensionHeight}\n"
		text += f"m_rearSuspensionHeight: {self.m_rearSuspensionHeight}\n"
		text += f"m_brakePressure: {self.m_brakePressure}\n"
		text += f"m_brakeBias: {self.m_brakeBias}\n"
		text += f"m_rearLeftTyrePressure: {self.m_rearLeftTyrePressure}\n"
		text += f"m_rearRightTyrePressure: {self.m_rearRightTyrePressure}\n"
		text += f"m_frontLeftTyrePressure: {self.m_frontLeftTyrePressure}\n"
		text += f"m_frontRightTyrePressure: {self.m_frontRightTyrePressure}\n"
		text += f"m_ballast: {self.m_ballast}\n"
		text += f"m_fuelLoad: {self.m_fuelLoad}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "CarSetupData"
		dictionary["m_frontWing"] = self.m_frontWing
		dictionary["m_rearWing"] = self.m_rearWing
		dictionary["m_onThrottle"] = self.m_onThrottle
		dictionary["m_offThrottle"] = self.m_offThrottle
		dictionary["m_frontCamber"] = self.m_frontCamber
		dictionary["m_rearCamber"] = self.m_rearCamber
		dictionary["m_frontToe"] = self.m_frontToe
		dictionary["m_rearToe"] = self.m_rearToe
		dictionary["m_frontSuspension"] = self.m_frontSuspension
		dictionary["m_rearSuspension"] = self.m_rearSuspension
		dictionary["m_frontAntiRollBar"] = self.m_frontAntiRollBar
		dictionary["m_rearAntiRollBar"] = self.m_rearAntiRollBar
		dictionary["m_frontSuspensionHeight"] = self.m_frontSuspensionHeight
		dictionary["m_rearSuspensionHeight"] = self.m_rearSuspensionHeight
		dictionary["m_brakePressure"] = self.m_brakePressure
		dictionary["m_brakeBias"] = self.m_brakeBias
		dictionary["m_rearLeftTyrePressure"] = self.m_rearLeftTyrePressure
		dictionary["m_rearRightTyrePressure"] = self.m_rearRightTyrePressure
		dictionary["m_frontLeftTyrePressure"] = self.m_frontLeftTyrePressure
		dictionary["m_frontRightTyrePressure"] = self.m_frontRightTyrePressure
		dictionary["m_ballast"] = self.m_ballast
		dictionary["m_fuelLoad"] = self.m_fuelLoad
		return dictionary

class CarStatusData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBBfffHHBBHBBBbfffBfffB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(CarStatusData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_tractionControl = unpacked_data[0]
		self.m_antiLockBrakes = unpacked_data[1]
		self.m_fuelMix = unpacked_data[2]
		self.m_frontBrakeBias = unpacked_data[3]
		self.m_pitLimiterStatus = unpacked_data[4]
		self.m_fuelInTank = unpacked_data[5]
		self.m_fuelCapacity = unpacked_data[6]
		self.m_fuelRemainingLaps = unpacked_data[7]
		self.m_maxRPM = unpacked_data[8]
		self.m_idleRPM = unpacked_data[9]
		self.m_maxGears = unpacked_data[10]
		self.m_drsAllowed = unpacked_data[11]
		self.m_drsActivationDistance = unpacked_data[12]
		self.m_actualTyreCompound = unpacked_data[13]
		self.m_visualTyreCompound = unpacked_data[14]
		self.m_tyresAgeLaps = unpacked_data[15]
		self.m_vehicleFiaFlags = unpacked_data[16]
		self.m_enginePowerICE = unpacked_data[17]
		self.m_enginePowerMGUK = unpacked_data[18]
		self.m_ersStoreEnergy = unpacked_data[19]
		self.m_ersDeployMode = unpacked_data[20]
		self.m_ersHarvestedThisLapMGUK = unpacked_data[21]
		self.m_ersHarvestedThisLapMGUH = unpacked_data[22]
		self.m_ersDeployedThisLap = unpacked_data[23]
		self.m_networkPaused = unpacked_data[24]

	# To string
	def __str__(self):
		text = "--== <CarStatusData> ==--\n"
		text += f"m_tractionControl: {self.m_tractionControl}\n"
		text += f"m_antiLockBrakes: {self.m_antiLockBrakes}\n"
		text += f"m_fuelMix: {self.m_fuelMix}\n"
		text += f"m_frontBrakeBias: {self.m_frontBrakeBias}\n"
		text += f"m_pitLimiterStatus: {self.m_pitLimiterStatus}\n"
		text += f"m_fuelInTank: {self.m_fuelInTank}\n"
		text += f"m_fuelCapacity: {self.m_fuelCapacity}\n"
		text += f"m_fuelRemainingLaps: {self.m_fuelRemainingLaps}\n"
		text += f"m_maxRPM: {self.m_maxRPM}\n"
		text += f"m_idleRPM: {self.m_idleRPM}\n"
		text += f"m_maxGears: {self.m_maxGears}\n"
		text += f"m_drsAllowed: {self.m_drsAllowed}\n"
		text += f"m_drsActivationDistance: {self.m_drsActivationDistance}\n"
		text += f"m_actualTyreCompound: {self.m_actualTyreCompound}\n"
		text += f"m_visualTyreCompound: {self.m_visualTyreCompound}\n"
		text += f"m_tyresAgeLaps: {self.m_tyresAgeLaps}\n"
		text += f"m_vehicleFiaFlags: {self.m_vehicleFiaFlags}\n"
		text += f"m_enginePowerICE: {self.m_enginePowerICE}\n"
		text += f"m_enginePowerMGUK: {self.m_enginePowerMGUK}\n"
		text += f"m_ersStoreEnergy: {self.m_ersStoreEnergy}\n"
		text += f"m_ersDeployMode: {self.m_ersDeployMode}\n"
		text += f"m_ersHarvestedThisLapMGUK: {self.m_ersHarvestedThisLapMGUK}\n"
		text += f"m_ersHarvestedThisLapMGUH: {self.m_ersHarvestedThisLapMGUH}\n"
		text += f"m_ersDeployedThisLap: {self.m_ersDeployedThisLap}\n"
		text += f"m_networkPaused: {self.m_networkPaused}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "CarStatusData"
		dictionary["m_tractionControl"] = self.m_tractionControl
		dictionary["m_antiLockBrakes"] = self.m_antiLockBrakes
		dictionary["m_fuelMix"] = self.m_fuelMix
		dictionary["m_frontBrakeBias"] = self.m_frontBrakeBias
		dictionary["m_pitLimiterStatus"] = self.m_pitLimiterStatus
		dictionary["m_fuelInTank"] = self.m_fuelInTank
		dictionary["m_fuelCapacity"] = self.m_fuelCapacity
		dictionary["m_fuelRemainingLaps"] = self.m_fuelRemainingLaps
		dictionary["m_maxRPM"] = self.m_maxRPM
		dictionary["m_idleRPM"] = self.m_idleRPM
		dictionary["m_maxGears"] = self.m_maxGears
		dictionary["m_drsAllowed"] = self.m_drsAllowed
		dictionary["m_drsActivationDistance"] = self.m_drsActivationDistance
		dictionary["m_actualTyreCompound"] = self.m_actualTyreCompound
		dictionary["m_visualTyreCompound"] = self.m_visualTyreCompound
		dictionary["m_tyresAgeLaps"] = self.m_tyresAgeLaps
		dictionary["m_vehicleFiaFlags"] = self.m_vehicleFiaFlags
		dictionary["m_enginePowerICE"] = self.m_enginePowerICE
		dictionary["m_enginePowerMGUK"] = self.m_enginePowerMGUK
		dictionary["m_ersStoreEnergy"] = self.m_ersStoreEnergy
		dictionary["m_ersDeployMode"] = self.m_ersDeployMode
		dictionary["m_ersHarvestedThisLapMGUK"] = self.m_ersHarvestedThisLapMGUK
		dictionary["m_ersHarvestedThisLapMGUH"] = self.m_ersHarvestedThisLapMGUH
		dictionary["m_ersDeployedThisLap"] = self.m_ersDeployedThisLap
		dictionary["m_networkPaused"] = self.m_networkPaused
		return dictionary

class CarTelemetryData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HfffBbHBBHHHHHBBBBBBBBHffffBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(CarTelemetryData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_speed = unpacked_data[0]
		self.m_throttle = unpacked_data[1]
		self.m_steer = unpacked_data[2]
		self.m_brake = unpacked_data[3]
		self.m_clutch = unpacked_data[4]
		self.m_gear = unpacked_data[5]
		self.m_engineRPM = unpacked_data[6]
		self.m_drs = unpacked_data[7]
		self.m_revLightsPercent = unpacked_data[8]
		self.m_revLightsBitValue = unpacked_data[9]
		self.m_brakesTemperature = [unpacked_data[10], unpacked_data[11], unpacked_data[12], unpacked_data[13]]
		self.m_tyresSurfaceTemperature = [unpacked_data[14], unpacked_data[15], unpacked_data[16], unpacked_data[17]]
		self.m_tyresInnerTemperature = [unpacked_data[18], unpacked_data[19], unpacked_data[20], unpacked_data[21]]
		self.m_engineTemperature = unpacked_data[22]
		self.m_tyresPressure = [unpacked_data[23], unpacked_data[24], unpacked_data[25], unpacked_data[26]]
		self.m_surfaceType = [unpacked_data[27], unpacked_data[28], unpacked_data[29], unpacked_data[30]]

	# To string
	def __str__(self):
		text = "--== <CarTelemetryData> ==--\n"
		text += f"m_speed: {self.m_speed}\n"
		text += f"m_throttle: {self.m_throttle}\n"
		text += f"m_steer: {self.m_steer}\n"
		text += f"m_brake: {self.m_brake}\n"
		text += f"m_clutch: {self.m_clutch}\n"
		text += f"m_gear: {self.m_gear}\n"
		text += f"m_engineRPM: {self.m_engineRPM}\n"
		text += f"m_drs: {self.m_drs}\n"
		text += f"m_revLightsPercent: {self.m_revLightsPercent}\n"
		text += f"m_revLightsBitValue: {self.m_revLightsBitValue}\n"
		text += f"m_brakesTemperature: {self.m_brakesTemperature}\n"
		text += f"m_tyresSurfaceTemperature: {self.m_tyresSurfaceTemperature}\n"
		text += f"m_tyresInnerTemperature: {self.m_tyresInnerTemperature}\n"
		text += f"m_engineTemperature: {self.m_engineTemperature}\n"
		text += f"m_tyresPressure: {self.m_tyresPressure}\n"
		text += f"m_surfaceType: {self.m_surfaceType}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "CarTelemetryData"
		dictionary["m_speed"] = self.m_speed
		dictionary["m_throttle"] = self.m_throttle
		dictionary["m_steer"] = self.m_steer
		dictionary["m_brake"] = self.m_brake
		dictionary["m_clutch"] = self.m_clutch
		dictionary["m_gear"] = self.m_gear
		dictionary["m_engineRPM"] = self.m_engineRPM
		dictionary["m_drs"] = self.m_drs
		dictionary["m_revLightsPercent"] = self.m_revLightsPercent
		dictionary["m_revLightsBitValue"] = self.m_revLightsBitValue
		dictionary["m_brakesTemperature"] = self.m_brakesTemperature
		dictionary["m_tyresSurfaceTemperature"] = self.m_tyresSurfaceTemperature
		dictionary["m_tyresInnerTemperature"] = self.m_tyresInnerTemperature
		dictionary["m_engineTemperature"] = self.m_engineTemperature
		dictionary["m_tyresPressure"] = self.m_tyresPressure
		dictionary["m_surfaceType"] = self.m_surfaceType
		return dictionary

class EventDataDetails:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<I"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(EventDataDetails.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.buttonStatus = unpacked_data[0]

	# To string
	def __str__(self):
		text = "--== <EventDataDetails> ==--\n"
		text += f"buttonStatus: {self.buttonStatus}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "EventDataDetails"
		dictionary["buttonStatus"] = self.buttonStatus
		return dictionary

class FinalClassificationData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(FinalClassificationData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_position = unpacked_data[0]
		self.m_numLaps = unpacked_data[1]
		self.m_gridPosition = unpacked_data[2]
		self.m_points = unpacked_data[3]
		self.m_numPitStops = unpacked_data[4]
		self.m_resultStatus = unpacked_data[5]
		self.m_bestLapTimeInMS = unpacked_data[6]
		self.m_totalRaceTime = unpacked_data[7]
		self.m_penaltiesTime = unpacked_data[8]
		self.m_numPenalties = unpacked_data[9]
		self.m_numTyreStints = unpacked_data[10]
		self.m_tyreStintsActual = [unpacked_data[11], unpacked_data[12], unpacked_data[13], unpacked_data[14], unpacked_data[15], unpacked_data[16], unpacked_data[17], unpacked_data[18]]
		self.m_tyreStintsVisual = [unpacked_data[19], unpacked_data[20], unpacked_data[21], unpacked_data[22], unpacked_data[23], unpacked_data[24], unpacked_data[25], unpacked_data[26]]
		self.m_tyreStintsEndLaps = [unpacked_data[27], unpacked_data[28], unpacked_data[29], unpacked_data[30], unpacked_data[31], unpacked_data[32], unpacked_data[33], unpacked_data[34]]

	# To string
	def __str__(self):
		text = "--== <FinalClassificationData> ==--\n"
		text += f"m_position: {self.m_position}\n"
		text += f"m_numLaps: {self.m_numLaps}\n"
		text += f"m_gridPosition: {self.m_gridPosition}\n"
		text += f"m_points: {self.m_points}\n"
		text += f"m_numPitStops: {self.m_numPitStops}\n"
		text += f"m_resultStatus: {self.m_resultStatus}\n"
		text += f"m_bestLapTimeInMS: {self.m_bestLapTimeInMS}\n"
		text += f"m_totalRaceTime: {self.m_totalRaceTime}\n"
		text += f"m_penaltiesTime: {self.m_penaltiesTime}\n"
		text += f"m_numPenalties: {self.m_numPenalties}\n"
		text += f"m_numTyreStints: {self.m_numTyreStints}\n"
		text += f"m_tyreStintsActual: {self.m_tyreStintsActual}\n"
		text += f"m_tyreStintsVisual: {self.m_tyreStintsVisual}\n"
		text += f"m_tyreStintsEndLaps: {self.m_tyreStintsEndLaps}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "FinalClassificationData"
		dictionary["m_position"] = self.m_position
		dictionary["m_numLaps"] = self.m_numLaps
		dictionary["m_gridPosition"] = self.m_gridPosition
		dictionary["m_points"] = self.m_points
		dictionary["m_numPitStops"] = self.m_numPitStops
		dictionary["m_resultStatus"] = self.m_resultStatus
		dictionary["m_bestLapTimeInMS"] = self.m_bestLapTimeInMS
		dictionary["m_totalRaceTime"] = self.m_totalRaceTime
		dictionary["m_penaltiesTime"] = self.m_penaltiesTime
		dictionary["m_numPenalties"] = self.m_numPenalties
		dictionary["m_numTyreStints"] = self.m_numTyreStints
		dictionary["m_tyreStintsActual"] = self.m_tyreStintsActual
		dictionary["m_tyreStintsVisual"] = self.m_tyreStintsVisual
		dictionary["m_tyreStintsEndLaps"] = self.m_tyreStintsEndLaps
		return dictionary

class LapData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<IIHBHBHHfffBBBBBBBBBBBBBBBHHB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(LapData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_lastLapTimeInMS = unpacked_data[0]
		self.m_currentLapTimeInMS = unpacked_data[1]
		self.m_sector1TimeInMS = unpacked_data[2]
		self.m_sector1TimeMinutes = unpacked_data[3]
		self.m_sector2TimeInMS = unpacked_data[4]
		self.m_sector2TimeMinutes = unpacked_data[5]
		self.m_deltaToCarInFrontInMS = unpacked_data[6]
		self.m_deltaToRaceLeaderInMS = unpacked_data[7]
		self.m_lapDistance = unpacked_data[8]
		self.m_totalDistance = unpacked_data[9]
		self.m_safetyCarDelta = unpacked_data[10]
		self.m_carPosition = unpacked_data[11]
		self.m_currentLapNum = unpacked_data[12]
		self.m_pitStatus = unpacked_data[13]
		self.m_numPitStops = unpacked_data[14]
		self.m_sector = unpacked_data[15]
		self.m_currentLapInvalid = unpacked_data[16]
		self.m_penalties = unpacked_data[17]
		self.m_totalWarnings = unpacked_data[18]
		self.m_cornerCuttingWarnings = unpacked_data[19]
		self.m_numUnservedDriveThroughPens = unpacked_data[20]
		self.m_numUnservedStopGoPens = unpacked_data[21]
		self.m_gridPosition = unpacked_data[22]
		self.m_driverStatus = unpacked_data[23]
		self.m_resultStatus = unpacked_data[24]
		self.m_pitLaneTimerActive = unpacked_data[25]
		self.m_pitLaneTimeInLaneInMS = unpacked_data[26]
		self.m_pitStopTimerInMS = unpacked_data[27]
		self.m_pitStopShouldServePen = unpacked_data[28]

	# To string
	def __str__(self):
		text = "--== <LapData> ==--\n"
		text += f"m_lastLapTimeInMS: {self.m_lastLapTimeInMS}\n"
		text += f"m_currentLapTimeInMS: {self.m_currentLapTimeInMS}\n"
		text += f"m_sector1TimeInMS: {self.m_sector1TimeInMS}\n"
		text += f"m_sector1TimeMinutes: {self.m_sector1TimeMinutes}\n"
		text += f"m_sector2TimeInMS: {self.m_sector2TimeInMS}\n"
		text += f"m_sector2TimeMinutes: {self.m_sector2TimeMinutes}\n"
		text += f"m_deltaToCarInFrontInMS: {self.m_deltaToCarInFrontInMS}\n"
		text += f"m_deltaToRaceLeaderInMS: {self.m_deltaToRaceLeaderInMS}\n"
		text += f"m_lapDistance: {self.m_lapDistance}\n"
		text += f"m_totalDistance: {self.m_totalDistance}\n"
		text += f"m_safetyCarDelta: {self.m_safetyCarDelta}\n"
		text += f"m_carPosition: {self.m_carPosition}\n"
		text += f"m_currentLapNum: {self.m_currentLapNum}\n"
		text += f"m_pitStatus: {self.m_pitStatus}\n"
		text += f"m_numPitStops: {self.m_numPitStops}\n"
		text += f"m_sector: {self.m_sector}\n"
		text += f"m_currentLapInvalid: {self.m_currentLapInvalid}\n"
		text += f"m_penalties: {self.m_penalties}\n"
		text += f"m_totalWarnings: {self.m_totalWarnings}\n"
		text += f"m_cornerCuttingWarnings: {self.m_cornerCuttingWarnings}\n"
		text += f"m_numUnservedDriveThroughPens: {self.m_numUnservedDriveThroughPens}\n"
		text += f"m_numUnservedStopGoPens: {self.m_numUnservedStopGoPens}\n"
		text += f"m_gridPosition: {self.m_gridPosition}\n"
		text += f"m_driverStatus: {self.m_driverStatus}\n"
		text += f"m_resultStatus: {self.m_resultStatus}\n"
		text += f"m_pitLaneTimerActive: {self.m_pitLaneTimerActive}\n"
		text += f"m_pitLaneTimeInLaneInMS: {self.m_pitLaneTimeInLaneInMS}\n"
		text += f"m_pitStopTimerInMS: {self.m_pitStopTimerInMS}\n"
		text += f"m_pitStopShouldServePen: {self.m_pitStopShouldServePen}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "LapData"
		dictionary["m_lastLapTimeInMS"] = self.m_lastLapTimeInMS
		dictionary["m_currentLapTimeInMS"] = self.m_currentLapTimeInMS
		dictionary["m_sector1TimeInMS"] = self.m_sector1TimeInMS
		dictionary["m_sector1TimeMinutes"] = self.m_sector1TimeMinutes
		dictionary["m_sector2TimeInMS"] = self.m_sector2TimeInMS
		dictionary["m_sector2TimeMinutes"] = self.m_sector2TimeMinutes
		dictionary["m_deltaToCarInFrontInMS"] = self.m_deltaToCarInFrontInMS
		dictionary["m_deltaToRaceLeaderInMS"] = self.m_deltaToRaceLeaderInMS
		dictionary["m_lapDistance"] = self.m_lapDistance
		dictionary["m_totalDistance"] = self.m_totalDistance
		dictionary["m_safetyCarDelta"] = self.m_safetyCarDelta
		dictionary["m_carPosition"] = self.m_carPosition
		dictionary["m_currentLapNum"] = self.m_currentLapNum
		dictionary["m_pitStatus"] = self.m_pitStatus
		dictionary["m_numPitStops"] = self.m_numPitStops
		dictionary["m_sector"] = self.m_sector
		dictionary["m_currentLapInvalid"] = self.m_currentLapInvalid
		dictionary["m_penalties"] = self.m_penalties
		dictionary["m_totalWarnings"] = self.m_totalWarnings
		dictionary["m_cornerCuttingWarnings"] = self.m_cornerCuttingWarnings
		dictionary["m_numUnservedDriveThroughPens"] = self.m_numUnservedDriveThroughPens
		dictionary["m_numUnservedStopGoPens"] = self.m_numUnservedStopGoPens
		dictionary["m_gridPosition"] = self.m_gridPosition
		dictionary["m_driverStatus"] = self.m_driverStatus
		dictionary["m_resultStatus"] = self.m_resultStatus
		dictionary["m_pitLaneTimerActive"] = self.m_pitLaneTimerActive
		dictionary["m_pitLaneTimeInLaneInMS"] = self.m_pitLaneTimeInLaneInMS
		dictionary["m_pitStopTimerInMS"] = self.m_pitStopTimerInMS
		dictionary["m_pitStopShouldServePen"] = self.m_pitStopShouldServePen
		return dictionary

class LapHistoryData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<IHBHBHBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(LapHistoryData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_lapTimeInMS = unpacked_data[0]
		self.m_sector1TimeInMS = unpacked_data[1]
		self.m_sector1TimeMinutes = unpacked_data[2]
		self.m_sector2TimeInMS = unpacked_data[3]
		self.m_sector1TimeMinutes = unpacked_data[4]
		self.m_sector3TimeInMS = unpacked_data[5]
		self.m_sector3TimeMinutes = unpacked_data[6]
		self.m_lapValidBitFlags = unpacked_data[7]

	# To string
	def __str__(self):
		text = "--== <LapHistoryData> ==--\n"
		text += f"m_lapTimeInMS: {self.m_lapTimeInMS}\n"
		text += f"m_sector1TimeInMS: {self.m_sector1TimeInMS}\n"
		text += f"m_sector1TimeMinutes: {self.m_sector1TimeMinutes}\n"
		text += f"m_sector2TimeInMS: {self.m_sector2TimeInMS}\n"
		text += f"m_sector1TimeMinutes: {self.m_sector1TimeMinutes}\n"
		text += f"m_sector3TimeInMS: {self.m_sector3TimeInMS}\n"
		text += f"m_sector3TimeMinutes: {self.m_sector3TimeMinutes}\n"
		text += f"m_lapValidBitFlags: {self.m_lapValidBitFlags}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "LapHistoryData"
		dictionary["m_lapTimeInMS"] = self.m_lapTimeInMS
		dictionary["m_sector1TimeInMS"] = self.m_sector1TimeInMS
		dictionary["m_sector1TimeMinutes"] = self.m_sector1TimeMinutes
		dictionary["m_sector2TimeInMS"] = self.m_sector2TimeInMS
		dictionary["m_sector1TimeMinutes"] = self.m_sector1TimeMinutes
		dictionary["m_sector3TimeInMS"] = self.m_sector3TimeInMS
		dictionary["m_sector3TimeMinutes"] = self.m_sector3TimeMinutes
		dictionary["m_lapValidBitFlags"] = self.m_lapValidBitFlags
		return dictionary

class LobbyInfoData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBccccccccccccccccccccccccccccccccccccccccccccccccBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(LobbyInfoData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_aiControlled = unpacked_data[0]
		self.m_teamId = unpacked_data[1]
		self.m_nationality = unpacked_data[2]
		self.m_platform = unpacked_data[3]
		self.m_name = b''.join(unpacked_data[4:52]).decode('utf-8').split('\x00', 1)[0]
		self.m_carNumber = unpacked_data[52]
		self.m_readyStatus = unpacked_data[53]

	# To string
	def __str__(self):
		text = "--== <LobbyInfoData> ==--\n"
		text += f"m_aiControlled: {self.m_aiControlled}\n"
		text += f"m_teamId: {self.m_teamId}\n"
		text += f"m_nationality: {self.m_nationality}\n"
		text += f"m_platform: {self.m_platform}\n"
		text += f"m_name: {self.m_name}\n"
		text += f"m_carNumber: {self.m_carNumber}\n"
		text += f"m_readyStatus: {self.m_readyStatus}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "LobbyInfoData"
		dictionary["m_aiControlled"] = self.m_aiControlled
		dictionary["m_teamId"] = self.m_teamId
		dictionary["m_nationality"] = self.m_nationality
		dictionary["m_platform"] = self.m_platform
		dictionary["m_name"] = self.m_name
		dictionary["m_carNumber"] = self.m_carNumber
		dictionary["m_readyStatus"] = self.m_readyStatus
		return dictionary

class MarshalZone:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<fb"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(MarshalZone.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_zoneStart = unpacked_data[0]
		self.m_zoneFlag = unpacked_data[1]

	# To string
	def __str__(self):
		text = "--== <MarshalZone> ==--\n"
		text += f"m_zoneStart: {self.m_zoneStart}\n"
		text += f"m_zoneFlag: {self.m_zoneFlag}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "MarshalZone"
		dictionary["m_zoneStart"] = self.m_zoneStart
		dictionary["m_zoneFlag"] = self.m_zoneFlag
		return dictionary

class PacketHeader:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketHeader.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_packetFormat = unpacked_data[0]
		self.m_gameYear = unpacked_data[1]
		self.m_gameMajorVersion = unpacked_data[2]
		self.m_gameMinorVersion = unpacked_data[3]
		self.m_packetVersion = unpacked_data[4]
		self.m_packetId = unpacked_data[5]
		self.m_sessionUID = unpacked_data[6]
		self.m_sessionTime = unpacked_data[7]
		self.m_frameIdentifier = unpacked_data[8]
		self.m_overallFrameIdentifier = unpacked_data[9]
		self.m_playerCarIndex = unpacked_data[10]
		self.m_secondaryPlayerCarIndex = unpacked_data[11]

	# To string
	def __str__(self):
		text = "--== <PacketHeader> ==--\n"
		text += f"m_packetFormat: {self.m_packetFormat}\n"
		text += f"m_gameYear: {self.m_gameYear}\n"
		text += f"m_gameMajorVersion: {self.m_gameMajorVersion}\n"
		text += f"m_gameMinorVersion: {self.m_gameMinorVersion}\n"
		text += f"m_packetVersion: {self.m_packetVersion}\n"
		text += f"m_packetId: {self.m_packetId}\n"
		text += f"m_sessionUID: {self.m_sessionUID}\n"
		text += f"m_sessionTime: {self.m_sessionTime}\n"
		text += f"m_frameIdentifier: {self.m_frameIdentifier}\n"
		text += f"m_overallFrameIdentifier: {self.m_overallFrameIdentifier}\n"
		text += f"m_playerCarIndex: {self.m_playerCarIndex}\n"
		text += f"m_secondaryPlayerCarIndex: {self.m_secondaryPlayerCarIndex}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketHeader"
		dictionary["m_packetFormat"] = self.m_packetFormat
		dictionary["m_gameYear"] = self.m_gameYear
		dictionary["m_gameMajorVersion"] = self.m_gameMajorVersion
		dictionary["m_gameMinorVersion"] = self.m_gameMinorVersion
		dictionary["m_packetVersion"] = self.m_packetVersion
		dictionary["m_packetId"] = self.m_packetId
		dictionary["m_sessionUID"] = self.m_sessionUID
		dictionary["m_sessionTime"] = self.m_sessionTime
		dictionary["m_frameIdentifier"] = self.m_frameIdentifier
		dictionary["m_overallFrameIdentifier"] = self.m_overallFrameIdentifier
		dictionary["m_playerCarIndex"] = self.m_playerCarIndex
		dictionary["m_secondaryPlayerCarIndex"] = self.m_secondaryPlayerCarIndex
		return dictionary

class PacketCarDamageData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBBffffBBBBBBBBBBBBBBBBBBBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketCarDamageData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carDamageData = [CarDamageData(unpacked_data[12:42]), CarDamageData(unpacked_data[42:72]), CarDamageData(unpacked_data[72:102]), CarDamageData(unpacked_data[102:132]), CarDamageData(unpacked_data[132:162]), CarDamageData(unpacked_data[162:192]), CarDamageData(unpacked_data[192:222]), CarDamageData(unpacked_data[222:252]), CarDamageData(unpacked_data[252:282]), CarDamageData(unpacked_data[282:312]), CarDamageData(unpacked_data[312:342]), CarDamageData(unpacked_data[342:372]), CarDamageData(unpacked_data[372:402]), CarDamageData(unpacked_data[402:432]), CarDamageData(unpacked_data[432:462]), CarDamageData(unpacked_data[462:492]), CarDamageData(unpacked_data[492:522]), CarDamageData(unpacked_data[522:552]), CarDamageData(unpacked_data[552:582]), CarDamageData(unpacked_data[582:612]), CarDamageData(unpacked_data[612:642]), CarDamageData(unpacked_data[642:672])]

	# To string
	def __str__(self):
		text = "--== <PacketCarDamageData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carDamageData: {self.m_carDamageData}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketCarDamageData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carDamageData"] = [x.to_dict() for x in self.m_carDamageData]
		return dictionary

class PacketCarSetupData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBfBBBBffffBBBBBBBBffffBf"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketCarSetupData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carSetups = [CarSetupData(unpacked_data[12:34]), CarSetupData(unpacked_data[34:56]), CarSetupData(unpacked_data[56:78]), CarSetupData(unpacked_data[78:100]), CarSetupData(unpacked_data[100:122]), CarSetupData(unpacked_data[122:144]), CarSetupData(unpacked_data[144:166]), CarSetupData(unpacked_data[166:188]), CarSetupData(unpacked_data[188:210]), CarSetupData(unpacked_data[210:232]), CarSetupData(unpacked_data[232:254]), CarSetupData(unpacked_data[254:276]), CarSetupData(unpacked_data[276:298]), CarSetupData(unpacked_data[298:320]), CarSetupData(unpacked_data[320:342]), CarSetupData(unpacked_data[342:364]), CarSetupData(unpacked_data[364:386]), CarSetupData(unpacked_data[386:408]), CarSetupData(unpacked_data[408:430]), CarSetupData(unpacked_data[430:452]), CarSetupData(unpacked_data[452:474]), CarSetupData(unpacked_data[474:496])]

	# To string
	def __str__(self):
		text = "--== <PacketCarSetupData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carSetups: {self.m_carSetups}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketCarSetupData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carSetups"] = [x.to_dict() for x in self.m_carSetups]
		return dictionary

class PacketCarStatusData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffBBBBBBfffHHBBHBBBbfffBfffB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketCarStatusData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carStatusData = [CarStatusData(unpacked_data[12:37]), CarStatusData(unpacked_data[37:62]), CarStatusData(unpacked_data[62:87]), CarStatusData(unpacked_data[87:112]), CarStatusData(unpacked_data[112:137]), CarStatusData(unpacked_data[137:162]), CarStatusData(unpacked_data[162:187]), CarStatusData(unpacked_data[187:212]), CarStatusData(unpacked_data[212:237]), CarStatusData(unpacked_data[237:262]), CarStatusData(unpacked_data[262:287]), CarStatusData(unpacked_data[287:312]), CarStatusData(unpacked_data[312:337]), CarStatusData(unpacked_data[337:362]), CarStatusData(unpacked_data[362:387]), CarStatusData(unpacked_data[387:412]), CarStatusData(unpacked_data[412:437]), CarStatusData(unpacked_data[437:462]), CarStatusData(unpacked_data[462:487]), CarStatusData(unpacked_data[487:512]), CarStatusData(unpacked_data[512:537]), CarStatusData(unpacked_data[537:562])]

	# To string
	def __str__(self):
		text = "--== <PacketCarStatusData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carStatusData: {self.m_carStatusData}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketCarStatusData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carStatusData"] = [x.to_dict() for x in self.m_carStatusData]
		return dictionary

class PacketCarTelemetryData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBHfffBbHBBHHHHHBBBBBBBBHffffBBBBBBb"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketCarTelemetryData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carTelemetryData = [CarTelemetryData(unpacked_data[12:43]), CarTelemetryData(unpacked_data[43:74]), CarTelemetryData(unpacked_data[74:105]), CarTelemetryData(unpacked_data[105:136]), CarTelemetryData(unpacked_data[136:167]), CarTelemetryData(unpacked_data[167:198]), CarTelemetryData(unpacked_data[198:229]), CarTelemetryData(unpacked_data[229:260]), CarTelemetryData(unpacked_data[260:291]), CarTelemetryData(unpacked_data[291:322]), CarTelemetryData(unpacked_data[322:353]), CarTelemetryData(unpacked_data[353:384]), CarTelemetryData(unpacked_data[384:415]), CarTelemetryData(unpacked_data[415:446]), CarTelemetryData(unpacked_data[446:477]), CarTelemetryData(unpacked_data[477:508]), CarTelemetryData(unpacked_data[508:539]), CarTelemetryData(unpacked_data[539:570]), CarTelemetryData(unpacked_data[570:601]), CarTelemetryData(unpacked_data[601:632]), CarTelemetryData(unpacked_data[632:663]), CarTelemetryData(unpacked_data[663:694])]
		self.m_mfdPanelIndex = unpacked_data[694]
		self.m_mfdPanelIndexSecondaryPlayer = unpacked_data[695]
		self.m_suggestedGear = unpacked_data[696]

	# To string
	def __str__(self):
		text = "--== <PacketCarTelemetryData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carTelemetryData: {self.m_carTelemetryData}\n"
		text += f"m_mfdPanelIndex: {self.m_mfdPanelIndex}\n"
		text += f"m_mfdPanelIndexSecondaryPlayer: {self.m_mfdPanelIndexSecondaryPlayer}\n"
		text += f"m_suggestedGear: {self.m_suggestedGear}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketCarTelemetryData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carTelemetryData"] = [x.to_dict() for x in self.m_carTelemetryData]
		dictionary["m_mfdPanelIndex"] = self.m_mfdPanelIndex
		dictionary["m_mfdPanelIndexSecondaryPlayer"] = self.m_mfdPanelIndexSecondaryPlayer
		dictionary["m_suggestedGear"] = self.m_suggestedGear
		return dictionary

class PacketEventData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBI"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketEventData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_eventStringCode = [unpacked_data[12], unpacked_data[13], unpacked_data[14], unpacked_data[15]]
		self.m_eventDetails = EventDataDetails(unpacked_data[16:17])

	# To string
	def __str__(self):
		text = "--== <PacketEventData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_eventStringCode: {self.m_eventStringCode}\n"
		text += f"m_eventDetails: {self.m_eventDetails}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketEventData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_eventStringCode"] = self.m_eventStringCode
		dictionary["m_eventDetails"] = self.m_eventDetails.to_dict()
		return dictionary

class PacketFinalClassificationData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIdBBBBBBBBBBBBBBBBBBBBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketFinalClassificationData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_numCars = unpacked_data[12]
		self.m_classificationData = [FinalClassificationData(unpacked_data[13:48]), FinalClassificationData(unpacked_data[48:83]), FinalClassificationData(unpacked_data[83:118]), FinalClassificationData(unpacked_data[118:153]), FinalClassificationData(unpacked_data[153:188]), FinalClassificationData(unpacked_data[188:223]), FinalClassificationData(unpacked_data[223:258]), FinalClassificationData(unpacked_data[258:293]), FinalClassificationData(unpacked_data[293:328]), FinalClassificationData(unpacked_data[328:363]), FinalClassificationData(unpacked_data[363:398]), FinalClassificationData(unpacked_data[398:433]), FinalClassificationData(unpacked_data[433:468]), FinalClassificationData(unpacked_data[468:503]), FinalClassificationData(unpacked_data[503:538]), FinalClassificationData(unpacked_data[538:573]), FinalClassificationData(unpacked_data[573:608]), FinalClassificationData(unpacked_data[608:643]), FinalClassificationData(unpacked_data[643:678]), FinalClassificationData(unpacked_data[678:713]), FinalClassificationData(unpacked_data[713:748]), FinalClassificationData(unpacked_data[748:783])]

	# To string
	def __str__(self):
		text = "--== <PacketFinalClassificationData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_numCars: {self.m_numCars}\n"
		text += f"m_classificationData: {self.m_classificationData}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketFinalClassificationData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_numCars"] = self.m_numCars
		dictionary["m_classificationData"] = [x.to_dict() for x in self.m_classificationData]
		return dictionary

class PacketLapData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBIIHBHBHHfffBBBBBBBBBBBBBBBHHBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketLapData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_lapData = [LapData(unpacked_data[12:41]), LapData(unpacked_data[41:70]), LapData(unpacked_data[70:99]), LapData(unpacked_data[99:128]), LapData(unpacked_data[128:157]), LapData(unpacked_data[157:186]), LapData(unpacked_data[186:215]), LapData(unpacked_data[215:244]), LapData(unpacked_data[244:273]), LapData(unpacked_data[273:302]), LapData(unpacked_data[302:331]), LapData(unpacked_data[331:360]), LapData(unpacked_data[360:389]), LapData(unpacked_data[389:418]), LapData(unpacked_data[418:447]), LapData(unpacked_data[447:476]), LapData(unpacked_data[476:505]), LapData(unpacked_data[505:534]), LapData(unpacked_data[534:563]), LapData(unpacked_data[563:592]), LapData(unpacked_data[592:621]), LapData(unpacked_data[621:650])]
		self.m_timeTrialPBCarIdx = unpacked_data[650]
		self.m_timeTrialRivalCarIdx = unpacked_data[651]

	# To string
	def __str__(self):
		text = "--== <PacketLapData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_lapData: {self.m_lapData}\n"
		text += f"m_timeTrialPBCarIdx: {self.m_timeTrialPBCarIdx}\n"
		text += f"m_timeTrialRivalCarIdx: {self.m_timeTrialRivalCarIdx}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketLapData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_lapData"] = [x.to_dict() for x in self.m_lapData]
		dictionary["m_timeTrialPBCarIdx"] = self.m_timeTrialPBCarIdx
		dictionary["m_timeTrialRivalCarIdx"] = self.m_timeTrialRivalCarIdx
		return dictionary

class PacketLobbyInfoData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketLobbyInfoData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_numPlayers = unpacked_data[12]
		self.m_lobbyPlayers = [LobbyInfoData(unpacked_data[13:67]), LobbyInfoData(unpacked_data[67:121]), LobbyInfoData(unpacked_data[121:175]), LobbyInfoData(unpacked_data[175:229]), LobbyInfoData(unpacked_data[229:283]), LobbyInfoData(unpacked_data[283:337]), LobbyInfoData(unpacked_data[337:391]), LobbyInfoData(unpacked_data[391:445]), LobbyInfoData(unpacked_data[445:499]), LobbyInfoData(unpacked_data[499:553]), LobbyInfoData(unpacked_data[553:607]), LobbyInfoData(unpacked_data[607:661]), LobbyInfoData(unpacked_data[661:715]), LobbyInfoData(unpacked_data[715:769]), LobbyInfoData(unpacked_data[769:823]), LobbyInfoData(unpacked_data[823:877]), LobbyInfoData(unpacked_data[877:931]), LobbyInfoData(unpacked_data[931:985]), LobbyInfoData(unpacked_data[985:1039]), LobbyInfoData(unpacked_data[1039:1093]), LobbyInfoData(unpacked_data[1093:1147]), LobbyInfoData(unpacked_data[1147:1201])]

	# To string
	def __str__(self):
		text = "--== <PacketLobbyInfoData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_numPlayers: {self.m_numPlayers}\n"
		text += f"m_lobbyPlayers: {self.m_lobbyPlayers}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketLobbyInfoData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_numPlayers"] = self.m_numPlayers
		dictionary["m_lobbyPlayers"] = [x.to_dict() for x in self.m_lobbyPlayers]
		return dictionary

class PacketMotionData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffffffffffhhhhhhffffff"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketMotionData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carMotionData = [CarMotionData(unpacked_data[12:30]), CarMotionData(unpacked_data[30:48]), CarMotionData(unpacked_data[48:66]), CarMotionData(unpacked_data[66:84]), CarMotionData(unpacked_data[84:102]), CarMotionData(unpacked_data[102:120]), CarMotionData(unpacked_data[120:138]), CarMotionData(unpacked_data[138:156]), CarMotionData(unpacked_data[156:174]), CarMotionData(unpacked_data[174:192]), CarMotionData(unpacked_data[192:210]), CarMotionData(unpacked_data[210:228]), CarMotionData(unpacked_data[228:246]), CarMotionData(unpacked_data[246:264]), CarMotionData(unpacked_data[264:282]), CarMotionData(unpacked_data[282:300]), CarMotionData(unpacked_data[300:318]), CarMotionData(unpacked_data[318:336]), CarMotionData(unpacked_data[336:354]), CarMotionData(unpacked_data[354:372]), CarMotionData(unpacked_data[372:390]), CarMotionData(unpacked_data[390:408])]

	# To string
	def __str__(self):
		text = "--== <PacketMotionData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carMotionData: {self.m_carMotionData}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketMotionData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carMotionData"] = [x.to_dict() for x in self.m_carMotionData]
		return dictionary

class PacketMotionExData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBfffffffffffffffffffffffffffffffffffffffffffffff"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketMotionExData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_suspensionPosition = [unpacked_data[12], unpacked_data[13], unpacked_data[14], unpacked_data[15]]
		self.m_suspensionVelocity = [unpacked_data[16], unpacked_data[17], unpacked_data[18], unpacked_data[19]]
		self.m_suspensionAcceleration = [unpacked_data[20], unpacked_data[21], unpacked_data[22], unpacked_data[23]]
		self.m_wheelSpeed = [unpacked_data[24], unpacked_data[25], unpacked_data[26], unpacked_data[27]]
		self.m_wheelSlipRatio = [unpacked_data[28], unpacked_data[29], unpacked_data[30], unpacked_data[31]]
		self.m_wheelSlipAngle = [unpacked_data[32], unpacked_data[33], unpacked_data[34], unpacked_data[35]]
		self.m_wheelLatForce = [unpacked_data[36], unpacked_data[37], unpacked_data[38], unpacked_data[39]]
		self.m_wheelLongForce = [unpacked_data[40], unpacked_data[41], unpacked_data[42], unpacked_data[43]]
		self.m_heightOfCOGAboveGround = unpacked_data[44]
		self.m_localVelocityX = unpacked_data[45]
		self.m_localVelocityY = unpacked_data[46]
		self.m_localVelocityZ = unpacked_data[47]
		self.m_angularVelocityX = unpacked_data[48]
		self.m_angularVelocityY = unpacked_data[49]
		self.m_angularVelocityZ = unpacked_data[50]
		self.m_angularAccelerationX = unpacked_data[51]
		self.m_angularAccelerationY = unpacked_data[52]
		self.m_angularAccelerationZ = unpacked_data[53]
		self.m_frontWheelsAngle = unpacked_data[54]
		self.m_wheelVertForce = [unpacked_data[55], unpacked_data[56], unpacked_data[57], unpacked_data[58]]

	# To string
	def __str__(self):
		text = "--== <PacketMotionExData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_suspensionPosition: {self.m_suspensionPosition}\n"
		text += f"m_suspensionVelocity: {self.m_suspensionVelocity}\n"
		text += f"m_suspensionAcceleration: {self.m_suspensionAcceleration}\n"
		text += f"m_wheelSpeed: {self.m_wheelSpeed}\n"
		text += f"m_wheelSlipRatio: {self.m_wheelSlipRatio}\n"
		text += f"m_wheelSlipAngle: {self.m_wheelSlipAngle}\n"
		text += f"m_wheelLatForce: {self.m_wheelLatForce}\n"
		text += f"m_wheelLongForce: {self.m_wheelLongForce}\n"
		text += f"m_heightOfCOGAboveGround: {self.m_heightOfCOGAboveGround}\n"
		text += f"m_localVelocityX: {self.m_localVelocityX}\n"
		text += f"m_localVelocityY: {self.m_localVelocityY}\n"
		text += f"m_localVelocityZ: {self.m_localVelocityZ}\n"
		text += f"m_angularVelocityX: {self.m_angularVelocityX}\n"
		text += f"m_angularVelocityY: {self.m_angularVelocityY}\n"
		text += f"m_angularVelocityZ: {self.m_angularVelocityZ}\n"
		text += f"m_angularAccelerationX: {self.m_angularAccelerationX}\n"
		text += f"m_angularAccelerationY: {self.m_angularAccelerationY}\n"
		text += f"m_angularAccelerationZ: {self.m_angularAccelerationZ}\n"
		text += f"m_frontWheelsAngle: {self.m_frontWheelsAngle}\n"
		text += f"m_wheelVertForce: {self.m_wheelVertForce}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketMotionExData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_suspensionPosition"] = self.m_suspensionPosition
		dictionary["m_suspensionVelocity"] = self.m_suspensionVelocity
		dictionary["m_suspensionAcceleration"] = self.m_suspensionAcceleration
		dictionary["m_wheelSpeed"] = self.m_wheelSpeed
		dictionary["m_wheelSlipRatio"] = self.m_wheelSlipRatio
		dictionary["m_wheelSlipAngle"] = self.m_wheelSlipAngle
		dictionary["m_wheelLatForce"] = self.m_wheelLatForce
		dictionary["m_wheelLongForce"] = self.m_wheelLongForce
		dictionary["m_heightOfCOGAboveGround"] = self.m_heightOfCOGAboveGround
		dictionary["m_localVelocityX"] = self.m_localVelocityX
		dictionary["m_localVelocityY"] = self.m_localVelocityY
		dictionary["m_localVelocityZ"] = self.m_localVelocityZ
		dictionary["m_angularVelocityX"] = self.m_angularVelocityX
		dictionary["m_angularVelocityY"] = self.m_angularVelocityY
		dictionary["m_angularVelocityZ"] = self.m_angularVelocityZ
		dictionary["m_angularAccelerationX"] = self.m_angularAccelerationX
		dictionary["m_angularAccelerationY"] = self.m_angularAccelerationY
		dictionary["m_angularAccelerationZ"] = self.m_angularAccelerationZ
		dictionary["m_frontWheelsAngle"] = self.m_frontWheelsAngle
		dictionary["m_wheelVertForce"] = self.m_wheelVertForce
		return dictionary

class ParticipantData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(ParticipantData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_aiControlled = unpacked_data[0]
		self.m_driverId = unpacked_data[1]
		self.m_networkId = unpacked_data[2]
		self.m_teamId = unpacked_data[3]
		self.m_myTeam = unpacked_data[4]
		self.m_raceNumber = unpacked_data[5]
		self.m_nationality = unpacked_data[6]
		self.m_name = b''.join(unpacked_data[7:55]).decode('utf-8').split('\x00', 1)[0]
		self.m_yourTelemetry = unpacked_data[55]
		self.m_showOnlineNames = unpacked_data[56]
		self.m_platform = unpacked_data[57]

	# To string
	def __str__(self):
		text = "--== <ParticipantData> ==--\n"
		text += f"m_aiControlled: {self.m_aiControlled}\n"
		text += f"m_driverId: {self.m_driverId}\n"
		text += f"m_networkId: {self.m_networkId}\n"
		text += f"m_teamId: {self.m_teamId}\n"
		text += f"m_myTeam: {self.m_myTeam}\n"
		text += f"m_raceNumber: {self.m_raceNumber}\n"
		text += f"m_nationality: {self.m_nationality}\n"
		text += f"m_name: {self.m_name}\n"
		text += f"m_yourTelemetry: {self.m_yourTelemetry}\n"
		text += f"m_showOnlineNames: {self.m_showOnlineNames}\n"
		text += f"m_platform: {self.m_platform}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "ParticipantData"
		dictionary["m_aiControlled"] = self.m_aiControlled
		dictionary["m_driverId"] = self.m_driverId
		dictionary["m_networkId"] = self.m_networkId
		dictionary["m_teamId"] = self.m_teamId
		dictionary["m_myTeam"] = self.m_myTeam
		dictionary["m_raceNumber"] = self.m_raceNumber
		dictionary["m_nationality"] = self.m_nationality
		dictionary["m_name"] = self.m_name
		dictionary["m_yourTelemetry"] = self.m_yourTelemetry
		dictionary["m_showOnlineNames"] = self.m_showOnlineNames
		dictionary["m_platform"] = self.m_platform
		return dictionary

class PacketParticipantsData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBBBBBBBBBccccccccccccccccccccccccccccccccccccccccccccccccBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketParticipantsData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_numActiveCars = unpacked_data[12]
		self.m_participants = [ParticipantData(unpacked_data[13:71]), ParticipantData(unpacked_data[71:129]), ParticipantData(unpacked_data[129:187]), ParticipantData(unpacked_data[187:245]), ParticipantData(unpacked_data[245:303]), ParticipantData(unpacked_data[303:361]), ParticipantData(unpacked_data[361:419]), ParticipantData(unpacked_data[419:477]), ParticipantData(unpacked_data[477:535]), ParticipantData(unpacked_data[535:593]), ParticipantData(unpacked_data[593:651]), ParticipantData(unpacked_data[651:709]), ParticipantData(unpacked_data[709:767]), ParticipantData(unpacked_data[767:825]), ParticipantData(unpacked_data[825:883]), ParticipantData(unpacked_data[883:941]), ParticipantData(unpacked_data[941:999]), ParticipantData(unpacked_data[999:1057]), ParticipantData(unpacked_data[1057:1115]), ParticipantData(unpacked_data[1115:1173]), ParticipantData(unpacked_data[1173:1231]), ParticipantData(unpacked_data[1231:1289])]

	# To string
	def __str__(self):
		text = "--== <PacketParticipantsData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_numActiveCars: {self.m_numActiveCars}\n"
		text += f"m_participants: {self.m_participants}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketParticipantsData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_numActiveCars"] = self.m_numActiveCars
		dictionary["m_participants"] = [x.to_dict() for x in self.m_participants]
		return dictionary

class WeatherForecastSample:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBbbbbB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(WeatherForecastSample.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_sessionType = unpacked_data[0]
		self.m_timeOffset = unpacked_data[1]
		self.m_weather = unpacked_data[2]
		self.m_trackTemperature = unpacked_data[3]
		self.m_trackTemperatureChange = unpacked_data[4]
		self.m_airTemperature = unpacked_data[5]
		self.m_airTemperatureChange = unpacked_data[6]
		self.m_rainPercentage = unpacked_data[7]

	# To string
	def __str__(self):
		text = "--== <WeatherForecastSample> ==--\n"
		text += f"m_sessionType: {self.m_sessionType}\n"
		text += f"m_timeOffset: {self.m_timeOffset}\n"
		text += f"m_weather: {self.m_weather}\n"
		text += f"m_trackTemperature: {self.m_trackTemperature}\n"
		text += f"m_trackTemperatureChange: {self.m_trackTemperatureChange}\n"
		text += f"m_airTemperature: {self.m_airTemperature}\n"
		text += f"m_airTemperatureChange: {self.m_airTemperatureChange}\n"
		text += f"m_rainPercentage: {self.m_rainPercentage}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "WeatherForecastSample"
		dictionary["m_sessionType"] = self.m_sessionType
		dictionary["m_timeOffset"] = self.m_timeOffset
		dictionary["m_weather"] = self.m_weather
		dictionary["m_trackTemperature"] = self.m_trackTemperature
		dictionary["m_trackTemperatureChange"] = self.m_trackTemperatureChange
		dictionary["m_airTemperature"] = self.m_airTemperature
		dictionary["m_airTemperatureChange"] = self.m_airTemperatureChange
		dictionary["m_rainPercentage"] = self.m_rainPercentage
		return dictionary

class PacketSessionData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBbbBHBbBHHBBBBBBfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbfbBBBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBBbbbbBBBIIIBBBBBBBBBBBBBBIBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketSessionData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_weather = unpacked_data[12]
		self.m_trackTemperature = unpacked_data[13]
		self.m_airTemperature = unpacked_data[14]
		self.m_totalLaps = unpacked_data[15]
		self.m_trackLength = unpacked_data[16]
		self.m_sessionType = unpacked_data[17]
		self.m_trackId = unpacked_data[18]
		self.m_formula = unpacked_data[19]
		self.m_sessionTimeLeft = unpacked_data[20]
		self.m_sessionDuration = unpacked_data[21]
		self.m_pitSpeedLimit = unpacked_data[22]
		self.m_gamePaused = unpacked_data[23]
		self.m_isSpectating = unpacked_data[24]
		self.m_spectatorCarIndex = unpacked_data[25]
		self.m_sliProNativeSupport = unpacked_data[26]
		self.m_numMarshalZones = unpacked_data[27]
		self.m_marshalZones = [MarshalZone(unpacked_data[28:30]), MarshalZone(unpacked_data[30:32]), MarshalZone(unpacked_data[32:34]), MarshalZone(unpacked_data[34:36]), MarshalZone(unpacked_data[36:38]), MarshalZone(unpacked_data[38:40]), MarshalZone(unpacked_data[40:42]), MarshalZone(unpacked_data[42:44]), MarshalZone(unpacked_data[44:46]), MarshalZone(unpacked_data[46:48]), MarshalZone(unpacked_data[48:50]), MarshalZone(unpacked_data[50:52]), MarshalZone(unpacked_data[52:54]), MarshalZone(unpacked_data[54:56]), MarshalZone(unpacked_data[56:58]), MarshalZone(unpacked_data[58:60]), MarshalZone(unpacked_data[60:62]), MarshalZone(unpacked_data[62:64]), MarshalZone(unpacked_data[64:66]), MarshalZone(unpacked_data[66:68]), MarshalZone(unpacked_data[68:70])]
		self.m_safetyCarStatus = unpacked_data[70]
		self.m_networkGame = unpacked_data[71]
		self.m_numWeatherForecastSamples = unpacked_data[72]
		self.m_weatherForecastSamples = [WeatherForecastSample(unpacked_data[73:81]), WeatherForecastSample(unpacked_data[81:89]), WeatherForecastSample(unpacked_data[89:97]), WeatherForecastSample(unpacked_data[97:105]), WeatherForecastSample(unpacked_data[105:113]), WeatherForecastSample(unpacked_data[113:121]), WeatherForecastSample(unpacked_data[121:129]), WeatherForecastSample(unpacked_data[129:137]), WeatherForecastSample(unpacked_data[137:145]), WeatherForecastSample(unpacked_data[145:153]), WeatherForecastSample(unpacked_data[153:161]), WeatherForecastSample(unpacked_data[161:169]), WeatherForecastSample(unpacked_data[169:177]), WeatherForecastSample(unpacked_data[177:185]), WeatherForecastSample(unpacked_data[185:193]), WeatherForecastSample(unpacked_data[193:201]), WeatherForecastSample(unpacked_data[201:209]), WeatherForecastSample(unpacked_data[209:217]), WeatherForecastSample(unpacked_data[217:225]), WeatherForecastSample(unpacked_data[225:233]), WeatherForecastSample(unpacked_data[233:241]), WeatherForecastSample(unpacked_data[241:249]), WeatherForecastSample(unpacked_data[249:257]), WeatherForecastSample(unpacked_data[257:265]), WeatherForecastSample(unpacked_data[265:273]), WeatherForecastSample(unpacked_data[273:281]), WeatherForecastSample(unpacked_data[281:289]), WeatherForecastSample(unpacked_data[289:297]), WeatherForecastSample(unpacked_data[297:305]), WeatherForecastSample(unpacked_data[305:313]), WeatherForecastSample(unpacked_data[313:321]), WeatherForecastSample(unpacked_data[321:329]), WeatherForecastSample(unpacked_data[329:337]), WeatherForecastSample(unpacked_data[337:345]), WeatherForecastSample(unpacked_data[345:353]), WeatherForecastSample(unpacked_data[353:361]), WeatherForecastSample(unpacked_data[361:369]), WeatherForecastSample(unpacked_data[369:377]), WeatherForecastSample(unpacked_data[377:385]), WeatherForecastSample(unpacked_data[385:393]), WeatherForecastSample(unpacked_data[393:401]), WeatherForecastSample(unpacked_data[401:409]), WeatherForecastSample(unpacked_data[409:417]), WeatherForecastSample(unpacked_data[417:425]), WeatherForecastSample(unpacked_data[425:433]), WeatherForecastSample(unpacked_data[433:441]), WeatherForecastSample(unpacked_data[441:449]), WeatherForecastSample(unpacked_data[449:457]), WeatherForecastSample(unpacked_data[457:465]), WeatherForecastSample(unpacked_data[465:473]), WeatherForecastSample(unpacked_data[473:481]), WeatherForecastSample(unpacked_data[481:489]), WeatherForecastSample(unpacked_data[489:497]), WeatherForecastSample(unpacked_data[497:505]), WeatherForecastSample(unpacked_data[505:513]), WeatherForecastSample(unpacked_data[513:521])]
		self.m_forecastAccuracy = unpacked_data[521]
		self.m_aiDifficulty = unpacked_data[522]
		self.m_seasonLinkIdentifier = unpacked_data[523]
		self.m_weekendLinkIdentifier = unpacked_data[524]
		self.m_sessionLinkIdentifier = unpacked_data[525]
		self.m_pitStopWindowIdealLap = unpacked_data[526]
		self.m_pitStopWindowLatestLap = unpacked_data[527]
		self.m_pitStopRejoinPosition = unpacked_data[528]
		self.m_steeringAssist = unpacked_data[529]
		self.m_brakingAssist = unpacked_data[530]
		self.m_gearboxAssist = unpacked_data[531]
		self.m_pitAssist = unpacked_data[532]
		self.m_pitReleaseAssist = unpacked_data[533]
		self.m_ERSAssist = unpacked_data[534]
		self.m_DRSAssist = unpacked_data[535]
		self.m_dynamicRacingLine = unpacked_data[536]
		self.m_dynamicRacingLineType = unpacked_data[537]
		self.m_gameMode = unpacked_data[538]
		self.m_ruleSet = unpacked_data[539]
		self.m_timeOfDay = unpacked_data[540]
		self.m_sessionLength = unpacked_data[541]
		self.m_speedUnitsLeadPlayer = unpacked_data[542]
		self.m_temperatureUnitsLeadPlayer = unpacked_data[543]
		self.m_speedUnitsSecondaryPlayer = unpacked_data[544]
		self.m_temperatureUnitsSecondaryPlayer = unpacked_data[545]
		self.m_numSafetyCarPeriods = unpacked_data[546]
		self.m_numVirtualSafetyCarPeriods = unpacked_data[547]
		self.m_numRedFlagPeriods = unpacked_data[548]

	# To string
	def __str__(self):
		text = "--== <PacketSessionData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_weather: {self.m_weather}\n"
		text += f"m_trackTemperature: {self.m_trackTemperature}\n"
		text += f"m_airTemperature: {self.m_airTemperature}\n"
		text += f"m_totalLaps: {self.m_totalLaps}\n"
		text += f"m_trackLength: {self.m_trackLength}\n"
		text += f"m_sessionType: {self.m_sessionType}\n"
		text += f"m_trackId: {self.m_trackId}\n"
		text += f"m_formula: {self.m_formula}\n"
		text += f"m_sessionTimeLeft: {self.m_sessionTimeLeft}\n"
		text += f"m_sessionDuration: {self.m_sessionDuration}\n"
		text += f"m_pitSpeedLimit: {self.m_pitSpeedLimit}\n"
		text += f"m_gamePaused: {self.m_gamePaused}\n"
		text += f"m_isSpectating: {self.m_isSpectating}\n"
		text += f"m_spectatorCarIndex: {self.m_spectatorCarIndex}\n"
		text += f"m_sliProNativeSupport: {self.m_sliProNativeSupport}\n"
		text += f"m_numMarshalZones: {self.m_numMarshalZones}\n"
		text += f"m_marshalZones: {self.m_marshalZones}\n"
		text += f"m_safetyCarStatus: {self.m_safetyCarStatus}\n"
		text += f"m_networkGame: {self.m_networkGame}\n"
		text += f"m_numWeatherForecastSamples: {self.m_numWeatherForecastSamples}\n"
		text += f"m_weatherForecastSamples: {self.m_weatherForecastSamples}\n"
		text += f"m_forecastAccuracy: {self.m_forecastAccuracy}\n"
		text += f"m_aiDifficulty: {self.m_aiDifficulty}\n"
		text += f"m_seasonLinkIdentifier: {self.m_seasonLinkIdentifier}\n"
		text += f"m_weekendLinkIdentifier: {self.m_weekendLinkIdentifier}\n"
		text += f"m_sessionLinkIdentifier: {self.m_sessionLinkIdentifier}\n"
		text += f"m_pitStopWindowIdealLap: {self.m_pitStopWindowIdealLap}\n"
		text += f"m_pitStopWindowLatestLap: {self.m_pitStopWindowLatestLap}\n"
		text += f"m_pitStopRejoinPosition: {self.m_pitStopRejoinPosition}\n"
		text += f"m_steeringAssist: {self.m_steeringAssist}\n"
		text += f"m_brakingAssist: {self.m_brakingAssist}\n"
		text += f"m_gearboxAssist: {self.m_gearboxAssist}\n"
		text += f"m_pitAssist: {self.m_pitAssist}\n"
		text += f"m_pitReleaseAssist: {self.m_pitReleaseAssist}\n"
		text += f"m_ERSAssist: {self.m_ERSAssist}\n"
		text += f"m_DRSAssist: {self.m_DRSAssist}\n"
		text += f"m_dynamicRacingLine: {self.m_dynamicRacingLine}\n"
		text += f"m_dynamicRacingLineType: {self.m_dynamicRacingLineType}\n"
		text += f"m_gameMode: {self.m_gameMode}\n"
		text += f"m_ruleSet: {self.m_ruleSet}\n"
		text += f"m_timeOfDay: {self.m_timeOfDay}\n"
		text += f"m_sessionLength: {self.m_sessionLength}\n"
		text += f"m_speedUnitsLeadPlayer: {self.m_speedUnitsLeadPlayer}\n"
		text += f"m_temperatureUnitsLeadPlayer: {self.m_temperatureUnitsLeadPlayer}\n"
		text += f"m_speedUnitsSecondaryPlayer: {self.m_speedUnitsSecondaryPlayer}\n"
		text += f"m_temperatureUnitsSecondaryPlayer: {self.m_temperatureUnitsSecondaryPlayer}\n"
		text += f"m_numSafetyCarPeriods: {self.m_numSafetyCarPeriods}\n"
		text += f"m_numVirtualSafetyCarPeriods: {self.m_numVirtualSafetyCarPeriods}\n"
		text += f"m_numRedFlagPeriods: {self.m_numRedFlagPeriods}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketSessionData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_weather"] = self.m_weather
		dictionary["m_trackTemperature"] = self.m_trackTemperature
		dictionary["m_airTemperature"] = self.m_airTemperature
		dictionary["m_totalLaps"] = self.m_totalLaps
		dictionary["m_trackLength"] = self.m_trackLength
		dictionary["m_sessionType"] = self.m_sessionType
		dictionary["m_trackId"] = self.m_trackId
		dictionary["m_formula"] = self.m_formula
		dictionary["m_sessionTimeLeft"] = self.m_sessionTimeLeft
		dictionary["m_sessionDuration"] = self.m_sessionDuration
		dictionary["m_pitSpeedLimit"] = self.m_pitSpeedLimit
		dictionary["m_gamePaused"] = self.m_gamePaused
		dictionary["m_isSpectating"] = self.m_isSpectating
		dictionary["m_spectatorCarIndex"] = self.m_spectatorCarIndex
		dictionary["m_sliProNativeSupport"] = self.m_sliProNativeSupport
		dictionary["m_numMarshalZones"] = self.m_numMarshalZones
		dictionary["m_marshalZones"] = [x.to_dict() for x in self.m_marshalZones]
		dictionary["m_safetyCarStatus"] = self.m_safetyCarStatus
		dictionary["m_networkGame"] = self.m_networkGame
		dictionary["m_numWeatherForecastSamples"] = self.m_numWeatherForecastSamples
		dictionary["m_weatherForecastSamples"] = [x.to_dict() for x in self.m_weatherForecastSamples]
		dictionary["m_forecastAccuracy"] = self.m_forecastAccuracy
		dictionary["m_aiDifficulty"] = self.m_aiDifficulty
		dictionary["m_seasonLinkIdentifier"] = self.m_seasonLinkIdentifier
		dictionary["m_weekendLinkIdentifier"] = self.m_weekendLinkIdentifier
		dictionary["m_sessionLinkIdentifier"] = self.m_sessionLinkIdentifier
		dictionary["m_pitStopWindowIdealLap"] = self.m_pitStopWindowIdealLap
		dictionary["m_pitStopWindowLatestLap"] = self.m_pitStopWindowLatestLap
		dictionary["m_pitStopRejoinPosition"] = self.m_pitStopRejoinPosition
		dictionary["m_steeringAssist"] = self.m_steeringAssist
		dictionary["m_brakingAssist"] = self.m_brakingAssist
		dictionary["m_gearboxAssist"] = self.m_gearboxAssist
		dictionary["m_pitAssist"] = self.m_pitAssist
		dictionary["m_pitReleaseAssist"] = self.m_pitReleaseAssist
		dictionary["m_ERSAssist"] = self.m_ERSAssist
		dictionary["m_DRSAssist"] = self.m_DRSAssist
		dictionary["m_dynamicRacingLine"] = self.m_dynamicRacingLine
		dictionary["m_dynamicRacingLineType"] = self.m_dynamicRacingLineType
		dictionary["m_gameMode"] = self.m_gameMode
		dictionary["m_ruleSet"] = self.m_ruleSet
		dictionary["m_timeOfDay"] = self.m_timeOfDay
		dictionary["m_sessionLength"] = self.m_sessionLength
		dictionary["m_speedUnitsLeadPlayer"] = self.m_speedUnitsLeadPlayer
		dictionary["m_temperatureUnitsLeadPlayer"] = self.m_temperatureUnitsLeadPlayer
		dictionary["m_speedUnitsSecondaryPlayer"] = self.m_speedUnitsSecondaryPlayer
		dictionary["m_temperatureUnitsSecondaryPlayer"] = self.m_temperatureUnitsSecondaryPlayer
		dictionary["m_numSafetyCarPeriods"] = self.m_numSafetyCarPeriods
		dictionary["m_numVirtualSafetyCarPeriods"] = self.m_numVirtualSafetyCarPeriods
		dictionary["m_numRedFlagPeriods"] = self.m_numRedFlagPeriods
		return dictionary

class TyreStintHistoryData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(TyreStintHistoryData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_endLap = unpacked_data[0]
		self.m_tyreActualCompound = unpacked_data[1]
		self.m_tyreVisualCompound = unpacked_data[2]

	# To string
	def __str__(self):
		text = "--== <TyreStintHistoryData> ==--\n"
		text += f"m_endLap: {self.m_endLap}\n"
		text += f"m_tyreActualCompound: {self.m_tyreActualCompound}\n"
		text += f"m_tyreVisualCompound: {self.m_tyreVisualCompound}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "TyreStintHistoryData"
		dictionary["m_endLap"] = self.m_endLap
		dictionary["m_tyreActualCompound"] = self.m_tyreActualCompound
		dictionary["m_tyreVisualCompound"] = self.m_tyreVisualCompound
		return dictionary

class PacketSessionHistoryData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBIHBHBHBBBBBBBBBBBBBBBBBBBBBBBBBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketSessionHistoryData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carIdx = unpacked_data[12]
		self.m_numLaps = unpacked_data[13]
		self.m_numTyreStints = unpacked_data[14]
		self.m_bestLapTimeLapNum = unpacked_data[15]
		self.m_bestSector1LapNum = unpacked_data[16]
		self.m_bestSector2LapNum = unpacked_data[17]
		self.m_bestSector3LapNum = unpacked_data[18]
		self.m_lapHistoryData = [LapHistoryData(unpacked_data[19:27]), LapHistoryData(unpacked_data[27:35]), LapHistoryData(unpacked_data[35:43]), LapHistoryData(unpacked_data[43:51]), LapHistoryData(unpacked_data[51:59]), LapHistoryData(unpacked_data[59:67]), LapHistoryData(unpacked_data[67:75]), LapHistoryData(unpacked_data[75:83]), LapHistoryData(unpacked_data[83:91]), LapHistoryData(unpacked_data[91:99]), LapHistoryData(unpacked_data[99:107]), LapHistoryData(unpacked_data[107:115]), LapHistoryData(unpacked_data[115:123]), LapHistoryData(unpacked_data[123:131]), LapHistoryData(unpacked_data[131:139]), LapHistoryData(unpacked_data[139:147]), LapHistoryData(unpacked_data[147:155]), LapHistoryData(unpacked_data[155:163]), LapHistoryData(unpacked_data[163:171]), LapHistoryData(unpacked_data[171:179]), LapHistoryData(unpacked_data[179:187]), LapHistoryData(unpacked_data[187:195]), LapHistoryData(unpacked_data[195:203]), LapHistoryData(unpacked_data[203:211]), LapHistoryData(unpacked_data[211:219]), LapHistoryData(unpacked_data[219:227]), LapHistoryData(unpacked_data[227:235]), LapHistoryData(unpacked_data[235:243]), LapHistoryData(unpacked_data[243:251]), LapHistoryData(unpacked_data[251:259]), LapHistoryData(unpacked_data[259:267]), LapHistoryData(unpacked_data[267:275]), LapHistoryData(unpacked_data[275:283]), LapHistoryData(unpacked_data[283:291]), LapHistoryData(unpacked_data[291:299]), LapHistoryData(unpacked_data[299:307]), LapHistoryData(unpacked_data[307:315]), LapHistoryData(unpacked_data[315:323]), LapHistoryData(unpacked_data[323:331]), LapHistoryData(unpacked_data[331:339]), LapHistoryData(unpacked_data[339:347]), LapHistoryData(unpacked_data[347:355]), LapHistoryData(unpacked_data[355:363]), LapHistoryData(unpacked_data[363:371]), LapHistoryData(unpacked_data[371:379]), LapHistoryData(unpacked_data[379:387]), LapHistoryData(unpacked_data[387:395]), LapHistoryData(unpacked_data[395:403]), LapHistoryData(unpacked_data[403:411]), LapHistoryData(unpacked_data[411:419]), LapHistoryData(unpacked_data[419:427]), LapHistoryData(unpacked_data[427:435]), LapHistoryData(unpacked_data[435:443]), LapHistoryData(unpacked_data[443:451]), LapHistoryData(unpacked_data[451:459]), LapHistoryData(unpacked_data[459:467]), LapHistoryData(unpacked_data[467:475]), LapHistoryData(unpacked_data[475:483]), LapHistoryData(unpacked_data[483:491]), LapHistoryData(unpacked_data[491:499]), LapHistoryData(unpacked_data[499:507]), LapHistoryData(unpacked_data[507:515]), LapHistoryData(unpacked_data[515:523]), LapHistoryData(unpacked_data[523:531]), LapHistoryData(unpacked_data[531:539]), LapHistoryData(unpacked_data[539:547]), LapHistoryData(unpacked_data[547:555]), LapHistoryData(unpacked_data[555:563]), LapHistoryData(unpacked_data[563:571]), LapHistoryData(unpacked_data[571:579]), LapHistoryData(unpacked_data[579:587]), LapHistoryData(unpacked_data[587:595]), LapHistoryData(unpacked_data[595:603]), LapHistoryData(unpacked_data[603:611]), LapHistoryData(unpacked_data[611:619]), LapHistoryData(unpacked_data[619:627]), LapHistoryData(unpacked_data[627:635]), LapHistoryData(unpacked_data[635:643]), LapHistoryData(unpacked_data[643:651]), LapHistoryData(unpacked_data[651:659]), LapHistoryData(unpacked_data[659:667]), LapHistoryData(unpacked_data[667:675]), LapHistoryData(unpacked_data[675:683]), LapHistoryData(unpacked_data[683:691]), LapHistoryData(unpacked_data[691:699]), LapHistoryData(unpacked_data[699:707]), LapHistoryData(unpacked_data[707:715]), LapHistoryData(unpacked_data[715:723]), LapHistoryData(unpacked_data[723:731]), LapHistoryData(unpacked_data[731:739]), LapHistoryData(unpacked_data[739:747]), LapHistoryData(unpacked_data[747:755]), LapHistoryData(unpacked_data[755:763]), LapHistoryData(unpacked_data[763:771]), LapHistoryData(unpacked_data[771:779]), LapHistoryData(unpacked_data[779:787]), LapHistoryData(unpacked_data[787:795]), LapHistoryData(unpacked_data[795:803]), LapHistoryData(unpacked_data[803:811]), LapHistoryData(unpacked_data[811:819])]
		self.m_tyreStintsHistoryData = [TyreStintHistoryData(unpacked_data[819:822]), TyreStintHistoryData(unpacked_data[822:825]), TyreStintHistoryData(unpacked_data[825:828]), TyreStintHistoryData(unpacked_data[828:831]), TyreStintHistoryData(unpacked_data[831:834]), TyreStintHistoryData(unpacked_data[834:837]), TyreStintHistoryData(unpacked_data[837:840]), TyreStintHistoryData(unpacked_data[840:843])]

	# To string
	def __str__(self):
		text = "--== <PacketSessionHistoryData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carIdx: {self.m_carIdx}\n"
		text += f"m_numLaps: {self.m_numLaps}\n"
		text += f"m_numTyreStints: {self.m_numTyreStints}\n"
		text += f"m_bestLapTimeLapNum: {self.m_bestLapTimeLapNum}\n"
		text += f"m_bestSector1LapNum: {self.m_bestSector1LapNum}\n"
		text += f"m_bestSector2LapNum: {self.m_bestSector2LapNum}\n"
		text += f"m_bestSector3LapNum: {self.m_bestSector3LapNum}\n"
		text += f"m_lapHistoryData: {self.m_lapHistoryData}\n"
		text += f"m_tyreStintsHistoryData: {self.m_tyreStintsHistoryData}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketSessionHistoryData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carIdx"] = self.m_carIdx
		dictionary["m_numLaps"] = self.m_numLaps
		dictionary["m_numTyreStints"] = self.m_numTyreStints
		dictionary["m_bestLapTimeLapNum"] = self.m_bestLapTimeLapNum
		dictionary["m_bestSector1LapNum"] = self.m_bestSector1LapNum
		dictionary["m_bestSector2LapNum"] = self.m_bestSector2LapNum
		dictionary["m_bestSector3LapNum"] = self.m_bestSector3LapNum
		dictionary["m_lapHistoryData"] = [x.to_dict() for x in self.m_lapHistoryData]
		dictionary["m_tyreStintsHistoryData"] = [x.to_dict() for x in self.m_tyreStintsHistoryData]
		return dictionary

class TyreSetData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<BBBBBBBhB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(TyreSetData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_actualTyreCompound = unpacked_data[0]
		self.m_visualTyreCompound = unpacked_data[1]
		self.m_wear = unpacked_data[2]
		self.m_available = unpacked_data[3]
		self.m_recommendedSession = unpacked_data[4]
		self.m_lifeSpan = unpacked_data[5]
		self.m_usableLife = unpacked_data[6]
		self.m_lapDeltaTime = unpacked_data[7]
		self.m_fitted = unpacked_data[8]

	# To string
	def __str__(self):
		text = "--== <TyreSetData> ==--\n"
		text += f"m_actualTyreCompound: {self.m_actualTyreCompound}\n"
		text += f"m_visualTyreCompound: {self.m_visualTyreCompound}\n"
		text += f"m_wear: {self.m_wear}\n"
		text += f"m_available: {self.m_available}\n"
		text += f"m_recommendedSession: {self.m_recommendedSession}\n"
		text += f"m_lifeSpan: {self.m_lifeSpan}\n"
		text += f"m_usableLife: {self.m_usableLife}\n"
		text += f"m_lapDeltaTime: {self.m_lapDeltaTime}\n"
		text += f"m_fitted: {self.m_fitted}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "TyreSetData"
		dictionary["m_actualTyreCompound"] = self.m_actualTyreCompound
		dictionary["m_visualTyreCompound"] = self.m_visualTyreCompound
		dictionary["m_wear"] = self.m_wear
		dictionary["m_available"] = self.m_available
		dictionary["m_recommendedSession"] = self.m_recommendedSession
		dictionary["m_lifeSpan"] = self.m_lifeSpan
		dictionary["m_usableLife"] = self.m_usableLife
		dictionary["m_lapDeltaTime"] = self.m_lapDeltaTime
		dictionary["m_fitted"] = self.m_fitted
		return dictionary

class PacketTyreSetsData:
	# Returns the unpack format
	@staticmethod
	def format():
		return f"<HBBBBBQfIIBBBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBBBBBBBBhBB"

	# Returns the byte size
	@staticmethod
	def size():
		return struct.calcsize(PacketTyreSetsData.format())

	# Initialize
	def __init__(self, unpacked_data):
		self.m_header = PacketHeader(unpacked_data[0:12])
		self.m_carIdx = unpacked_data[12]
		self.m_tyreSetData = [TyreSetData(unpacked_data[13:22]), TyreSetData(unpacked_data[22:31]), TyreSetData(unpacked_data[31:40]), TyreSetData(unpacked_data[40:49]), TyreSetData(unpacked_data[49:58]), TyreSetData(unpacked_data[58:67]), TyreSetData(unpacked_data[67:76]), TyreSetData(unpacked_data[76:85]), TyreSetData(unpacked_data[85:94]), TyreSetData(unpacked_data[94:103]), TyreSetData(unpacked_data[103:112]), TyreSetData(unpacked_data[112:121]), TyreSetData(unpacked_data[121:130]), TyreSetData(unpacked_data[130:139]), TyreSetData(unpacked_data[139:148]), TyreSetData(unpacked_data[148:157]), TyreSetData(unpacked_data[157:166]), TyreSetData(unpacked_data[166:175]), TyreSetData(unpacked_data[175:184]), TyreSetData(unpacked_data[184:193])]
		self.m_fittedIdx = unpacked_data[193]

	# To string
	def __str__(self):
		text = "--== <PacketTyreSetsData> ==--\n"
		text += f"m_header: {self.m_header}\n"
		text += f"m_carIdx: {self.m_carIdx}\n"
		text += f"m_tyreSetData: {self.m_tyreSetData}\n"
		text += f"m_fittedIdx: {self.m_fittedIdx}"
		return text

	# Prints data in a readable format
	def print(self):
		print(f"{self}")

	# Turns the object into a useable dictionary
	def to_dict(self):
		dictionary = {}
		dictionary["name"] = "PacketTyreSetsData"
		dictionary["m_header"] = self.m_header.to_dict()
		dictionary["m_carIdx"] = self.m_carIdx
		dictionary["m_tyreSetData"] = [x.to_dict() for x in self.m_tyreSetData]
		dictionary["m_fittedIdx"] = self.m_fittedIdx
		return dictionary

