"""Minimal HTTPS application using Flask.

Version 1.0
Latest update: 10/03/2021
"""

# Import Flask
from flask import (
    Flask,           # default flask class
    request,
    render_template  # allows us to create HTML templates
)
import socket
from pygit2 import Repository


# Create an instance of the Flask class
app = Flask(__name__)
version = "1.0"
vue_counter = 0
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

repo = Repository('/path/to/your/git/repo')
branch = repo.head.name


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

    return render_template(
        "home.html",
        version=version,
        counter=vue_counter,
        ip=request.host
    )


@app.route("/health")
def getHealth():
    """Foo bar blah
    """
    status_code = request.status_code
    return render_template("health.html", status=status_code)


# Adding Error handlers
@app.errorhandler(404)
def invalidRoute(e):
    return render_template("404.html")

# As this is the main file of our minimal application, when called the service
# should run.
if __name__ == "__main__":
    app.run(host="127.0.0.1")
