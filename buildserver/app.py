from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello from EnergyHub!"

    # /status returns a json object with the following key-value pairs:
    # pid - the process id of the server
    # status - the string "ok"
    @app.route("/status")
    def status():
        return {"pid": os.getpid(), "status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
