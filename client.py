import socketio
import requests

# Fetch the WebSocket URL from the server
response = requests.get('http://127.0.0.1:5000/api/socket')
data = response.json()
socket_url = data['socket_url']

# Create a Socket.IO client
sio = socketio.Client()

# Define the event handler for the 'update' event
@sio.event
def update(data):
    print("Received update:", data)

# Define the event handler for the 'connect' event
@sio.event
def connect():
    print("Connected to server")

# Define the event handler for the 'disconnect' event
@sio.event
def disconnect():
    print("Disconnected from server")

# Connect to the WebSocket server
sio.connect(socket_url)

# Keep the client running
sio.wait()
