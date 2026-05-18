package org.example;

import java.time.LocalDate;
import java.time.Period;
import java.time.temporal.ChronoUnit;

public class AgeCalculator {

    public int calculateAge(LocalDate birthDate) {
        return Period.between(birthDate, LocalDate.now()).getYears();
    }

    public long calculateDays(LocalDate birthDate) {
        return ChronoUnit.DAYS.between(birthDate, LocalDate.now());

    }
}
