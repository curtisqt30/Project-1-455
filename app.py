from flask import Flask, render_template
from flask_socketio import SocketIO

# Initialize Flask-SocketIO
sockio = SocketIO()

# Active Users Dictionary
active_users  = {}

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    sockio.init_app(app)
    return app

@socketio.on("message")
def handle_message(data):
    user = data.get("user")
    msg = data.get("msg")
    print(f"{user}: {msg}")
    emit("message", {"user": user, "msg": msg}, broadcast=True)

@socketio.on("connect")
def handle_connect():
    print("Client connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=5000)
    
    
