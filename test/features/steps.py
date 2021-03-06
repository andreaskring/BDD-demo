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
        'bruce': {
            'name': 'Bruce Lee'
        }
    })


@step(u"When I retrieve the user '(.*)'")
def when_i_retrieve_the_user_group1(step, username):
    world.response = world.app.get('/user/{}'.format(username))


@step(u"Then I should get a '(.*)' response")
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u"And the following user details are returned:")
def and_the_following_user_details(step):
    assert_equals(step.hashes, [json.loads(world.response.data)])


@step(u"When I add a new user with id '(.*)' and name '(.*)'")
def when_i_add_a_new_user(step, id, name):
    world.response = world.app.post('/user', data=json.dumps(
        {
            'id': id,
            'name': name
        }
    ), content_type='application/json')

