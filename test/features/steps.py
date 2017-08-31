import json

from lettuce import step, world, before
from nose.tools import assert_equals
from app.application import app
from app.routes import USERS


@before.all
def before_all():
    world.app = app.test_client()


@step(u"Given some users are in the system")
def given_some_users_are_in_the_system(step):
    USERS.update({
        'chuck': {
            'name': 'Chuck Norris'
        },
    })


@step(u"When I retrieve the user '(.*)'")
def when_i_retrieve_the_user(step, username):
    world.response = world.app.get('/user/{}'.format(username))


@step(u"Then I should get a '(.*)' response")
def then_i_should_get_a_xyz_response(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u"And the following user details are returned:")
def and_the_following_user_details(step):
    assert_equals(step.hashes, [json.loads(world.response.data)])
