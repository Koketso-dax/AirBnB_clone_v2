#!/usr/bin/python3
"""
starts a Flask web application
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from flask import Flask, render_template
from models import storage, state
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page with the states listed in alphabetical order
    """
    if isinstance(storage, storage.DBStorage):
        states = storage.all(state).values()
    else:
        states = sorted(list(storage.all("State")
                             .values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
