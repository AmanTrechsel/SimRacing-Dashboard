from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from threading import Lock
import os
from app import telemetry

# Create the Flask app
app = Flask(__name__)

# Create the SocketIO instance
socketio = SocketIO(app, async_mode='threading')
thread = None
thread_lock = Lock()

# Dashboard route
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Static model files route
@app.route('/models/<path:filename>')
def models(filename):
    models_dir = os.path.join(app.root_path, 'models')
    return send_from_directory(models_dir, filename)

# On connect, send the dashboard data
@socketio.on('connect')
def handle_connect():
    socketio.emit('data_update', telemetry.get_dashboard_data()) 

# Background thread to emit data updates
def background_thread():
    while True:
        socketio.emit('data_update', telemetry.get_dashboard_data())

# Start the background thread on connect
@socketio.event
def connect():
    global thread
    thread = socketio.start_background_task(background_thread)

# Start the Flask app
if __name__ == '__main__':
    socketio.run(app)
