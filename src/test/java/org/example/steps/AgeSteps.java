package org.example.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
import org.example.AgeCalculator;
import org.example.DateValidator;

import java.time.LocalDate;
import static org.junit.jupiter.api.Assertions.*;

public class AgeSteps {
    private final DateValidator validator = new DateValidator();
    private final AgeCalculator calculator = new AgeCalculator();

    private String inputDate;
    private LocalDate parsedDate;
    private int age;
    private long days;
    private Exception exception;

    @Given("user enters birth date {string}")
    public void user_enters_birth_date(String birthDate) {
        this.inputDate = birthDate;
    }

    @When("the system calculates age information")
    public void the_system_calculates_age_information() {
        parsedDate = validator.validateAndParse(inputDate);
        age = calculator.calculateAge(parsedDate);
        days = calculator.calculateDays(parsedDate);
    }

    @When("the system validates the date")
    public void the_system_validatesTheDate() {
        try {
            parsedDate = validator.validateAndParse(inputDate);
        } catch (Exception e) {
            exception = e;
        }
    }

    @Then("age should be greater than 0")
    public void age_should_be_greater_than_zero() {
        assertTrue(age > 0);
    }

    @And("number of days should be greater than 0")
    public void number_of_days_should_be_greater_than_zero() {
        assertTrue(days > 0);
    }

    @Then("error message should be {string}")
    public void error_message_should_be(String expectedMessage) {
        assertNotNull(exception);
        assertEquals(expectedMessage, exception.getMessage());
    }
}



