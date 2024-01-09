from flask import Flask
from threading import Thread

app = Flask('')


@app.route("/")
def home():
    return "Hey! I'm keeping alive."


def on_running():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=on_running)
    t.start()