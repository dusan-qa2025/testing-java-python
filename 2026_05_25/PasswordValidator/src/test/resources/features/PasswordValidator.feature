Feature: Validacija lozinke
  Scenario Outline:
    Given korisnik je uneo lozinku "<lozinka>"
    When sistem proverava validnost lozinke
    Then lozinka treba da bude "<rezultat>"

    Examples:
      |lozinka   |   rezultat    |
      |Password1 | validna       |
      |password1 | nevalidna     |
      |Password  | nevalidna     |
      |Pass1     | nevalidna     |