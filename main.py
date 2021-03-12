"""Minimal HTTPS application using Flask.
For automatic Reboot of the Flask service we will use PM2.
PM2 is a node.js service that monitors the activity of the sevices.

$ pm2 start main.py --name myName --interpreter=python3.8

Version 1.0
Latest update: 10/03/2021
"""

# Import Flask
from flask import (
    Flask,            # default flask class
    request,
    render_template,  # allows us to create HTML templates
    redirect,
    url_for
)
import argparse
import socket
import os
from requests import get


# Get Argumesnts from user
parser = argparse.ArgumentParser()
parser.add_argument(
    '--port',
    type=int,
    default=4000,
    help='Port on which the service should be launched'
)
args = parser.parse_args()
port = args.port


# Create an instance of the Flask class
app = Flask(__name__)

# Variables for app
version = "2.0"
vue_counter = 0
absolute_path = os.path.dirname(os.path.realpath(__file__))


ip = get('https://api.ipify.org').text
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

with open(os.path.join(absolute_path, ".git", "HEAD")) as head:
    line = head.read()

branch = line.split("/")[-1].split("\n")[0]

status_ok = True


# Create routing for the 'root' with the route() decorator and apply a
# hello_world function on that route
@app.route('/')
def hello_world():
    """Uses the render_template function to render the file "home.html".
    All templates must be located in a folder called 'template' in the root of
    the project.
    """
    global vue_counter
    vue_counter += 1
    status = "BAD"

    if status_ok:
        status = "OK"

    return render_template(
        "home.html",
        version=version,
        counter=vue_counter,
        ip=request.host,
        aws_ip=ip,
        git=branch,
        status=status
    )


@app.route("/health")
def getHealth():
    """Foo bar blah
    """
    status_code = 500
    status_text = "Error"
    if status_ok:
        status_code = 200
        status_text = "OK"
    return render_template(
        "health.html",
        status=status_code,
        status_text=status_text
    )


@app.route("/bug")
def createBug():
    """Changing the status to 500
    """
    global status_ok
    status_ok = False
    return redirect(url_for("hello_world"))


# Adding Error handlers
@app.errorhandler(404)
def invalidRoute(e):
    """Basic error handler
    """
    return render_template("404.html")


@app.route("/reboot")
def reboot():
    """Gracefully shutting down the server.
    Documentation at:
    https://werkzeug.palletsprojects.com/en/1.0.x/serving/?highlight=server%20shutdown#shutting-down-the-server
    """
    shutdown = request.environ.get("werkzeug.server.shutdown")
    if shutdown is None:
        raise RuntimeError("Shutdown unavailable")
    else:
        shutdown()
        return "Shutting down"


# As this is the main file of our minimal application, when called the service
# should run.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
