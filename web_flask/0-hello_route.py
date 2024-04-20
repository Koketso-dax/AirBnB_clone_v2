#!/usr/bin/python3
"""
Create basic Flask route.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Function to display Hello World.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Run the Flask application on 0.0.0.0, port 5000
    """
    app.run(host='0.0.0.0', port=5000)
