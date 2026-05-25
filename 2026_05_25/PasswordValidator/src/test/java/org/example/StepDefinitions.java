package org.example;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

public class StepDefinitions {

    private String password;
    private boolean result;

    private PasswordValidator validator = new PasswordValidator();

    @Given("korisnik je uneo lozinku {string}")
    public void korisnik_je_uneo_lozinku(String string) {
        this.password = string;
    }

    @When("sistem proverava validnost lozinke")
    public void sistem_proverava_validnost_lozinke() {
        this.result = validator.isValid(this.password);
    }

    @Then("lozinka treba da bude {string}")
    public void lozinka_treba_da_bude(String string) {
        boolean ispravno = string.equals("validna");
        Assert.assertEquals(ispravno, this.result);

        //  if (string.equals("validna")) {
        // Assert.assertTrue(this.result);
        // } else if (string.equals("nevalidna")) {
        //   Assert.assertFalse(this.result);
       // }

    }
}