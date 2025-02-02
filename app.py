from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import redis

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", message_queue="redis://localhost:6379")

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@socketio.on("connect")
def handle_connect():
    print("A client connected")

@socketio.on("message")
def handle_message(data):
    user = data.get("user")
    msg = data.get("msg")
    print(f"{user}: {msg}")
    emit("message", {"user": user, "msg": msg}, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    print("A client disconnected")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
