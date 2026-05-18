# Age Calculator BDD Project

## Overview

This project is a Java application developed using:

- Java
- Maven
- Cucumber
- JUnit
- BDD (Behavior Driven Development)

The application calculates:

- User age in ytyears
- Total number of days since birth

It also validates:

- Invalid date formats
- Future date
- Invalid calendar dates

# Features

* Calculate age from birth date
* Calculate total days since birth
* Validate date format
* Prevent future date input
* Automated BDD tests with Cucumber

# Example Scenarios

**Valid birth date**
Gherkin

Scenario: Calculate age and days for valid birth date 
Given user enters birth date "15/05/2000"
When the system calculates age information
Then age should be greater than 0
And number of days should be greater than 0

**Future date validation**
Gherkin

Scenario: Enter future date
Given user enters birth date "15/05/2050"
When the system validates the date
Then error message should be "Birth date cannot be in the future."

**Invalid date format**
Gherkin

Scenario: Enter invalid date format
Given user enters birth date "2000-05-15"
When the system validates the date
Then error message should be "Invalid date format. Use dd/MM/yyyy."

     
