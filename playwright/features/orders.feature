Feature: Order Transaction
         Tests related to Order Transactions

  Scenario Outline: Verify Order success message shown in details page
    Given place the order with <username> and <password>
    And User is on landing page
    When login in portal with <username> and <password>
    And navigate to order page
    And Select the order
    Then Order message is displayed
    Examples:
      | username                  | password |
      | rahulshetty@gmail.com     | Iamking@000|