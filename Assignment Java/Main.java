//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    void main(String[] args) {

        Student student = new Student("Tom", "Davis", "555/55");
        System.out.println(student.informacije());

        ispit ispit = new ispit("Programiranje u Javi","10.01.2026");
        System.out.println("Predmet: " + ispit.nazivPredmeta);
        System.out.println("Datum ispita: " + ispit.datumOdrzavanja);
    }
}













