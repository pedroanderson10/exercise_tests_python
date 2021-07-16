Feature: Login

#  Scenario: Valid login (1a)
#    Given a user is in the LEAD platform login page
#    When the user insert his valid credentials
#    Then LEAD platform redirects the user to the home page

  Scenario: invalid login (2a)
  Given a user is in the LEAD platform login page #2
  When the user insert his invalid credentials
  Then LEAD platform returns that the credentials are not valid

