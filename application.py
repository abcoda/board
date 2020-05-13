import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

board = []

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("change made")
def refresh(data):
    # board.append(data['change'])
    print("--- Begin ---")
    print(data['change'])
    print("--- End ---")
    emit("refresh board", data['change'], broadcast=True)
