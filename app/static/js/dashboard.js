// Time in seconds until warning message is displayed
const gamePacketTimeout = 10

// Variables
var lastCompoundValue = -1;
var carMesh;
var engine;
var scene;
var timeSinceLastPacket = 0;
var showAlways = false;

// Check size of window and display or hide warning message
function checkWindowSize() {
    // Get width and height of window
    var width = window.innerWidth;
    var height = window.innerHeight;

    // Check width and height
    if (width < 1300 || height < 750) {
        // Display message
        document.getElementById("fullscreen-message").style.display = "block";
    } else {
        // Hide message
        document.getElementById("fullscreen-message").style.display = "none";
    }
}

// Check time since last packet and display or hide warning message
function checkTimeSinceLastPacket() {
    // Check time since last packet
    if (timeSinceLastPacket >= gamePacketTimeout && !showAlways) {
        // Display message
        document.getElementById("fullscreen-packet-message").style.display = "block";
    } else {
        // Hide message
        document.getElementById("fullscreen-packet-message").style.display = "none";
    }
    timeSinceLastPacket += 1;
}

// Creates the scene for the simulation
function createScene() {
    var scene = new BABYLON.Scene(engine);
    scene.clearColor = new BABYLON.Color4(0, 0, 0, 0);

    var camera = new BABYLON.FollowCamera("FollowCamera", new BABYLON.Vector3(0, 10, -10), scene);
    camera.radius = 13; // how far from the object to follow
    camera.heightOffset = 5; // how high above the object to place the camera
    camera.rotationOffset = 180; // the viewing angle
    camera.cameraAcceleration = 0.005; // how fast to move
    camera.maxCameraSpeed = 10; // speed limit

    var light = new BABYLON.HemisphericLight("light", new BABYLON.Vector3(0, 1, 0), scene);
    BABYLON.SceneLoader.ImportMesh("", "models/", "scene.gltf", scene, function (meshes) {
        // Change meshes
        carMesh = meshes[0];
        camera.lockedTarget = carMesh;
    });
    return scene;
}

// Updates the car position in the simulation
function updateCarPosition(data) {
    if (carMesh) {
        var yaw = -data.yaw; 
        var pitch = -data.pitch;
        var roll = -data.roll;
        carMesh.rotationQuaternion = BABYLON.Quaternion.RotationYawPitchRoll(yaw, pitch, roll);
    }
}

// When document is ready
$(document).ready(function() {
    // Initialize BabylonJS
    var canvas = document.getElementById("renderCanvas");
    engine = new BABYLON.Engine(canvas, true);
    scene = createScene();

    // Render loop
    engine.runRenderLoop(function () {
        scene.render();
    });

    // Resize the canvas when the window is resized
    window.addEventListener("resize", function () {
        engine.resize();
    });

    // Check window size when page is loaded
    checkWindowSize();

    // Check window size when window is resized
    window.addEventListener("resize", checkWindowSize);

    // Check time since last packet every second
    window.setInterval(checkTimeSinceLastPacket, 1000);
    
    // Handle socket.io connection
    var socket = io();
    socket.on('data_update', function(data) {
        // Update the time since the last packet
        timeSinceLastPacket = 0;
        
        // Simulation
        // World Position
        if (typeof data.world_position_x !== 'undefined' && typeof data.world_position_y !== 'undefined' && typeof data.world_position_z !== 'undefined') {
            var worldPositionX = document.getElementById('world-position-x');
            worldPositionX.innerHTML = '<b>Position X:</b> ' + data.world_position_x;
            var worldPositionY = document.getElementById('world-position-y');
            worldPositionY.innerHTML = '<b>Position Y:</b> ' + data.world_position_y;
            var worldPositionZ = document.getElementById('world-position-z');
            worldPositionZ.innerHTML = '<b>Position Z:</b> ' + data.world_position_z;
        }

        // World Velocity
        if (typeof data.world_forward_dir_x !== 'undefined' && typeof data.world_forward_dir_y !== 'undefined' && typeof data.world_forward_dir_z !== 'undefined') {
            var worldVelocityX = document.getElementById('world-velocity-x');
            worldVelocityX.innerHTML = '<b>Velocity X:</b> ' + data.world_forward_dir_x;
            var worldVelocityY = document.getElementById('world-velocity-y');
            worldVelocityY.innerHTML = '<b>Velocity Y:</b> ' + data.world_forward_dir_y;
            var worldVelocityZ = document.getElementById('world-velocity-z');
            worldVelocityZ.innerHTML = '<b>Velocity Z:</b> ' + data.world_forward_dir_z;
        }

        // World Rotation
        if (typeof data.world_yaw !== 'undefined' && typeof data.world_pitch !== 'undefined' && typeof data.world_roll !== 'undefined') {
            var worldRotationYaw = document.getElementById('world-rotation-yaw');
            worldRotationYaw.innerHTML = '<b>Rotation Yaw:</b> ' + data.world_yaw;
            var worldRotationPitch = document.getElementById('world-rotation-pitch');
            worldRotationPitch.innerHTML = '<b>Rotation Pitch:</b> ' + data.world_pitch;
            var worldRotationRoll = document.getElementById('world-rotation-roll');
            worldRotationRoll.innerHTML = '<b>Rotation Roll:</b> ' + data.world_roll;
        }

        // G-Force
        if (typeof data.g_force_lateral !== 'undefined' && typeof data.g_force_longitudinal !== 'undefined' && typeof data.g_force_vertical !== 'undefined') {
            var gForceLat = document.getElementById('g-force-lat');
            gForceLat.innerHTML = '<b>G-Force Lat:</b> ' + data.g_force_lateral;
            var gForceLong = document.getElementById('g-force-long');
            gForceLong.innerHTML = '<b>G-Force Long:</b> ' + data.g_force_longitudinal;
            var gForceVert = document.getElementById('g-force-vert');
            gForceVert.innerHTML = '<b>G-Force Vert:</b> ' + data.g_force_vertical;
        }

        // Local Position
        if (typeof data.local_velocity_x !== 'undefined' && typeof data.local_velocity_y !== 'undefined' && typeof data.local_velocity_z !== 'undefined') {
            var localVelocityX = document.getElementById('local-velocity-x');
            localVelocityX.innerHTML = '<b>Velocity X:</b> ' + data.local_velocity_x;
            var localVelocityY = document.getElementById('local-velocity-y');
            localVelocityY.innerHTML = '<b>Velocity Y:</b> ' + data.local_velocity_y;
            var localVelocityZ = document.getElementById('local-velocity-z');
            localVelocityZ.innerHTML = '<b>Velocity Z:</b> ' + data.local_velocity_z;
        }

        // Front Wheels Angle
        if (typeof data.front_wheels_angle !== 'undefined') {
            var localFrontWheelsAngle = document.getElementById('local-front-wheels-angle');
            localFrontWheelsAngle.innerHTML = '<b>Wheels Angle:</b> ' + data.front_wheels_angle + '&deg;';
        }

        // Angular Velocity
        if (typeof data.angular_velocity_x !== 'undefined' && typeof data.angular_velocity_y !== 'undefined' && typeof data.angular_velocity_z !== 'undefined') {
            var angularVelocityX = document.getElementById('angular-velocity-x');
            angularVelocityX.innerHTML = '<b>Velocity X:</b> ' + data.angular_velocity_x;
            var angularVelocityY = document.getElementById('angular-velocity-y');
            angularVelocityY.innerHTML = '<b>Velocity Y:</b> ' + data.angular_velocity_y;
            var angularVelocityZ = document.getElementById('angular-velocity-z');
            angularVelocityZ.innerHTML = '<b>Velocity Z:</b> ' + data.angular_velocity_z;
        }

        // Angular Acceleration
        if (typeof data.angular_acceleration_x !== 'undefined' && typeof data.angular_acceleration_y !== 'undefined' && typeof data.angular_acceleration_z !== 'undefined') {
            var angularAccelerationX = document.getElementById('angular-acceleration-x');
            angularAccelerationX.innerHTML = '<b>Acceleration X:</b> ' + data.angular_acceleration_x;
            var angularAccelerationY = document.getElementById('angular-acceleration-y');
            angularAccelerationY.innerHTML = '<b>Acceleration Y:</b> ' + data.angular_acceleration_y;
            var angularAccelerationZ = document.getElementById('angular-acceleration-z');
            angularAccelerationZ.innerHTML = '<b>Acceleration Z:</b> ' + data.angular_acceleration_z;
        }

        // Car Position
        if (typeof data.yaw !== 'undefined' && typeof data.pitch !== 'undefined' && typeof data.roll !== 'undefined') {
            updateCarPosition(data);
        }

        // Velocity
        if (typeof data.kmh !== 'undefined') {
          var kmh = document.getElementById('kmh');
          kmh.innerHTML = data.kmh + ' KM/H';
        }
        if (typeof data.rpm !== 'undefined') {
          var rpm = document.getElementById('rpm');
          rpm.innerHTML = data.rpm + ' RPM';
        }
        if (typeof data.gear !== 'undefined') {
          var gear = document.getElementById('gear');
          var gearShow = data.gear == 0 ? 'N' : data.gear == -1 ? 'R' : data.gear;
          gear.innerHTML = gearShow;
        }

        // Fuel
        if (typeof data.fuel_percent !== 'undefined') {
          var tank = document.getElementById('fuel-tank');
          tank.innerHTML = 'Tank: ' + data.fuel_percent + '%';
        }
        if (typeof data.fuel_laps !== 'undefined') {
          var laps = document.getElementById('fuel-laps');
          laps.innerHTML = 'Laps: ' + data.fuel_laps;
        }

        // Lap Times
        if (typeof data.current_lap_time !== 'undefined') {
          var lapCurrent = document.getElementById('lap-current');
          lapCurrent.innerHTML = 'Current Lap: ' + data.current_lap_time;
        }
        if (typeof data.last_lap_time !== 'undefined') {
          var lapLast = document.getElementById('lap-last');
          lapLast.innerHTML = 'Last Lap: ' + data.last_lap_time;
        }
        if (typeof data.best_lap_time !== 'undefined') {
          var lapBest = document.getElementById('lap-best');
          lapBest.innerHTML = 'Best Lap: ' + data.best_lap_time;
        }
        if (typeof data.delta_lap_time !== 'undefined') {
          var lapDelta = document.getElementById('lap-delta');
          lapDelta.innerHTML = 'Delta Leader: ' + data.delta_lap_time;
        }

        // DRS
        if (typeof data.drs !== 'undefined') {
          var drs = document.getElementById('drs');
          drs.innerHTML = data.drs ? 'ON' : 'OFF';
          drs.className = data.drs ? 'drs-on' : 'drs-off';
        }

        // ERS
        if (typeof data.ers_mode !== 'undefined') {
          var ersMode = document.getElementById('ers-mode');
          ersMode.innerHTML = data.ers_mode;
        }
        if (typeof data.ers_energy !== 'undefined') {
          var ersEnergy = document.getElementById('ers-energy');
          ersEnergy.innerHTML = data.ers_energy + '%';
        }

        // Circuit
        if (typeof data.position !== 'undefined') {
          var trackPosition = document.getElementById('track-position');
          trackPosition.innerHTML = 'Position: ' + data.position;
        }
        if (typeof data.current_lap !== 'undefined' && typeof data.total_laps !== 'undefined') {
          var trackLap = document.getElementById('track-lap');
          trackLap.innerHTML = 'Lap: ' + data.current_lap + '/' + data.total_laps;
        }

        // Car Management
        const tyrePositions = [2, 0, 3, 1];
        if (typeof data.tyres_wear !== 'undefined') {
          var tyrePercentages = document.getElementsByClassName('tyre-percentage');
          for (let i = 0; i < tyrePercentages.length; i++) {
            tyrePercentages[i].innerHTML = data.tyres_wear[tyrePositions[i]] + '%';
          }
        }
        if (typeof data.brakes_temperature !== 'undefined') {
          var tyreBrakesTemperatures = document.getElementsByClassName('tyre-brakes-temperature');
          for (let i = 0; i < tyreBrakesTemperatures.length; i++) {
            tyreBrakesTemperatures[i].innerHTML = data.brakes_temperature[tyrePositions[i]] + '&deg;C';
          }
        }
        if (typeof data.tyres_surface_temperature !== 'undefined') {
          var tyreTemperatures = document.getElementsByClassName('tyre-temperature');
          for (let i = 0; i < tyreTemperatures.length; i++) {
            tyreTemperatures[i].innerHTML = data.tyres_surface_temperature[tyrePositions[i]] + '&deg;C';
          }
        }
        if (typeof data.tyre_compound !== 'undefined') {
            var compoundValue = data.tyre_compound;
            var tyreImages = document.getElementsByClassName('tyre-image');

            if (lastCompoundValue !== compoundValue) {
                // Loop over alle gevonden afbeeldingen
                for (var i = 0; i < tyreImages.length; i++) {
                    var tyreImage = tyreImages[i];
                    // Switch case
                    switch (compoundValue) {
                        case 19:
                            tyreImage.src = "../static/images/tyres/hard.svg";
                            break;
                        case 18:
                            tyreImage.src = "../static/images/tyres/medium.svg"; 
                            break;
                        case 17:
                            tyreImage.src = "../static/images/tyres/soft.svg"; 
                            break;
                        case 16:
                            tyreImage.src = "../static/images/tyres/intermediate.svg"; 
                            break;
                        case 15:
                            tyreImage.src = "../static/images/tyres/wet.svg"; 
                            break;
                    }
                }
                lastCompoundValue = compoundValue;
            }
        }
        
        // Weather
        if (typeof data.time_of_day !== 'undefined') {
          var timeOfDay = document.getElementById('time-of-day');
          timeOfDay.innerHTML = 'Time: ' + data.time_of_day;
        }
        if (typeof data.weather_forecast_weather !== 'undefined') {
          var weather = document.getElementById('weather');
          weather.innerHTML = data.weather_forecast_weather;
        }
        if (typeof data.weather_forecast_time_offset !== 'undefined') {
          var weatherTime = document.getElementById('weather-time');
          weatherTime.innerHTML = data.weather_forecast_time_offset + ' min';
        }
        if (typeof data.weather_forecast_air_temperature !== 'undefined') {
          var weatherAirTemperature = document.getElementById('weather-air-temperature');
          weatherAirTemperature.innerHTML = 'Air: ' + data.weather_forecast_air_temperature + '&deg;C';
        }
        if (typeof data.weather_forecast_track_temperature !== 'undefined') {
          var weatherTrackTemperature = document.getElementById('weather-track-temperature');
          weatherTrackTemperature.innerHTML = 'Track: ' + data.weather_forecast_track_temperature + '&deg;C';
        }
        if (typeof data.weather_forecast_rain_percentage !== 'undefined') {
          var weatherRainPercentage = document.getElementById('weather-rain-percentage');
          weatherRainPercentage.innerHTML = 'Rain: ' + data.weather_forecast_rain_percentage + '%';
        }
    });

    // Switch theme
    $('input[type="checkbox"]').change(function() {
        if($(this).is(":checked")) {
            $("body").addClass("light-theme").removeClass("dracula-theme");
        } else {
            $("body").addClass("dracula-theme").removeClass("light-theme");
        }
    });
});