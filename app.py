import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# votes = {"yes": 0, "no": 0, "maybe": 0}
# svg = ''

@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("change made")
def vote(data):
    # print(data)
    emit("refresh board", data['svg'], broadcast=True)
