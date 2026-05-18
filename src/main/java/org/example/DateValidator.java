package org.example;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class DateValidator {

    private static final  DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    public LocalDate validateAndParse(String date) {
        try {
            LocalDate parsedDate = LocalDate.parse(date, FORMATTER);

            if (parsedDate.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Birth date cannot be in the future.");
            }
            return parsedDate;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Invalid date format. Use dd/MM/yyyy.");
        }
    }
}
