Feature: Handle storing, retrieving and deleting users details

  Scenario: Retrieve a users details
    Given some users are in the system
    When I retrieve the user 'chuck'
    Then I should get a '200' response
    And the following user details are returned:
    | name |
    | Chuck Norris |

  Scenario: Retrieve another users details
    Given some users are in the system
    When I retrieve the user 'bruce'
    Then I should get a '200' response
    And the following user details are returned:
    | name |
    | Bruce Lee |

  Scenario: Add another user to the system
    When I add a new user with id 'clint' and name 'Clint Eastwood'
    Then I should get a '201' response
    When I retrieve the user 'clint'
    Then I should get a '200' response
    And the following user details are returned:
    | name |
    | Clint Eastwood |
