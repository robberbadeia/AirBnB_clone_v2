#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardownm(exception):
    """
    Method that remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states/", strict_slashes=False)
def states():
    """
    Method that display all states with its cities from DBStrorage
    """
    states = storage.all(State)

    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """
    Method that display info about state with id
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html")


if __name__ == "__main__":
    """Main Method"""
    app.run(host='0.0.0.0', port=5000)
