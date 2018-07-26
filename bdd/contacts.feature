Scenario Outline: Add new user
  Given a user list
  Given a user with <firstname>, <lastname> and <company>
  When I add the user to the list
  Then the new user list is equal to the old list with added user


  Examples:

  | firstname  | lastname  | company  |
  | firstname1 | lastname1 | company1 |
  | firstname2 | lastname2 | company2 |



Scenario: Delete user
  Given a non-empty user list
  Given a random user from the list
  When I delete random user from the list
  Then the new user list is equal to the old list without deleted user


Scenario: Modify user
  Given a non-empty user list
  Given a random user from the list
  Given a new user info with <firstname>, <lastname> and <company>
  When I modify random user from the list
  Then the new user list is equal to the old list without deleted user

  Examples:

  | firstname  | lastname  | company  |
  | firstname3 | lastname3 | company3 |