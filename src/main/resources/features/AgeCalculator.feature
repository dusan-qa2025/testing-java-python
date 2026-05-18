Feature: Age Calculator
  Scenario: Calculate age and days for valid birth date
    Given user enters birth date "15/05/2000"
    When the system calculates age information
    Then age should be greater than 0
    And number of days should be greater than 0

    Scenario: Enter future date
      Given user enters birth date "15/05/2050"
      When the system validates the date
      Then error message should be "Birth date cannot be in the future."

      Scenario: Enter invalid date format
        Given user enters birth date "2000-05-15"
        When the system validates the date
        Then error message should be "Invalid date format. Use dd/MM/yyyy."