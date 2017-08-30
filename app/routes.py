import flask
from app.application import app

USERS = {}


@app.route('/user/<username>')
def get_user(username):
    return flask.jsonify({'name': 'Chuck Norris'})