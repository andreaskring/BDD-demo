import flask
from app.application import app

USERS = {}


@app.route('/user/<username>')
def get_user(username):
    return flask.jsonify(USERS[username])


@app.route('/user', methods=['POST'])
def add_user():
    req = flask.request.get_json()
    USERS[req['id']] = {'name': req['name']}
    return flask.jsonify(USERS[req['id']]), 201