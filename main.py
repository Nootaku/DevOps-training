"""Minimal HTTPS application using Flask.

Version 1.0
Latest update: 10/03/2021
"""

# Import Flask
from flask import (
    Flask,           # default flask class
    render_template  # allows us to create HTML templates
)

# Create an instance of the Flask class
app = Flask(__name__)


# Create routing for the 'root' with the route() decorator and apply a
# hello_world function on that route
@app.route('/')
def hello_world():
    """Uses the render_template function to render the file "home.html".
    All templates must be located in a folder called 'template' in the root of
    the project.
    """
    return render_template("home.html")


# As this is the main file of our minimal application, when called the service
# should run.
if __name__ == "__main__":
    app.run()
