"""Minimal HTTPS application using Flask.

Version 1.0
Latest update: 10/03/2021
"""

# Import Flask
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Create routing for the 'root' with the route() decorator and apply a
# hello_world function on that route
@app.route('/')
def hello_world():
    """Simple hello_world.
    """
    return 'Hello, World!'


# As this is the main file of our minimal application, when called the service
# should run.
if __name__ == "__main__":
    app.run()
