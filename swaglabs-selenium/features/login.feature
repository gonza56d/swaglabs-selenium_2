Feature: Swaglabs main page Login

    Scenario: Do a successful login
        Given the user is in saucedemo login page
        When the user types its username and password
        And clicks on login button
        Then successful login is performed and page with products is displayed
