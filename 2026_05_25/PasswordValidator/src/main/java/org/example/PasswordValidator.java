package org.example;

public class PasswordValidator {
    public boolean isValid(String password) {

        if (password == null) {
            return false;
        }

        if (password.length() < 8) {
            return false;
        }
        boolean hasUppercase = false; // Da li ima veliko slovo?
        boolean hasDigit = false; // Da li sadrzi broj?

        for (char character : password.toCharArray()) {
            if (Character.isUpperCase(character)) {
                hasUppercase = true;
            }

            if (Character.isDigit(character)) {
                hasDigit = true;
            }
        }
        return hasUppercase && hasDigit;
    }
}
