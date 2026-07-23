//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
 /*public class Main{
void main(String[] args) {
    Car myCar = new Car("Honda", "Accord", 1590, "black");
    System.out.println(myCar.getInfo());
}
}



public class Main {
    public static void main(String[] args) {

        Convertible convertible1 = new Convertible("Honda", "S2000", 1274, "silver", "Vinyl, soft-top");

        System.out.println(convertible1.getName());
    }
}

  */

public class Main {
    public static void main(String[] args) {

        System.out.println(Math.abs(-17));
        System.out.println(Math.min(17, 23));
        System.out.println(Math.max(17, 23));
        System.out.println(Math.sqrt(16));
        System.out.println(Math.pow(4, 2));
        System.out.println(Math.signum(-17));
        System.out.println(Math.random());


        String s4 = new String("Hello");
        String s5 = new String("Hello");

        System.out.println(s4 == s5);
        // iako su iste vrednosti, na izlazu se dobija false jer su na razlicitim lokacijama untutar memorije!!!

        String myString = "My ";
        String myString1 = "string";

        System.out.println(myString.concat(myString1));
        StringBuilder sb = new StringBuilder();

        sb.append("My ");
        sb.append("string");

        System.out.println(sb);
        // dva razlicita nacina za nadovezivanje stringova!
    }
}
