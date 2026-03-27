public class Student {

    String ime;
    String prezime;
    String brojIndeksa;

    public Student (String ime, String prezime, String brojIndeksa) {
        this.ime = ime;
        this.prezime = prezime;
        this.brojIndeksa = brojIndeksa;
    }

    public String informacije() {
        return "Student: " + ime + " " + prezime + " " + brojIndeksa;
    }
}


