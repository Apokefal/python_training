Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with added group


  Examples:

  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |



Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete random group from the list
  Then the new group list is equal to the old list without deleted group


Scenario: Modify group
  Given a non-empty group list
  Given a random group from the list
  When I modify random group from the list
Then the new group list is equal to the old list without deleted group