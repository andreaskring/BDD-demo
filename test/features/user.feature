Feature: Handle storing, retrieving, modifying and deleting users details

  Scenario: Retrieve a users details
    Given some users are in the system
    When I retrieve the user 'chuck'
    Then I should get a '200' response
    And the following user details are returned:
    | name |
    | Chuck Norris |

  Scenario: Add another user to the system
    When I add a new user with id 'bruce' and name 'Bruce Lee'
    Then I should get a '201' response
    When I retrieve the user 'bruce'
    Then I should get a '200' response
    And the following user details are returned:
    | name |
    | Bruce Lee |
