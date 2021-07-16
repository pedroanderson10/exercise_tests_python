 Feature: Login

  Scenario: Invalid login (1a)
  Given a user is in the SGME login page
  When the user insert his invalid credentials
  Then system returns that the credentials are not valid