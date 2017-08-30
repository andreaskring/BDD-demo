Feature: Handle storing, retrieving and deleting customer details

Scenario: Retrieve a customers details
Given some users are in the system
When I retrieve the customer 'chuck'
Then I should get a '200' response
And the following user details are returned:
| name |
| Chuck Norris |