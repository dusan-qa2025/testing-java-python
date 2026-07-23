

// jednolinijski komentar
/* viselinijski komentar
/** Javadoc komentar- svaka linija komentara pocinje *
K O M E N T A R I !!!

V E Z B A NJ E :
public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 10;
        System.out.println(x);
    }
}


int decVal = 26;
int octVal = 032;       // 2 * 8^0 + 3 * 8^1 = 2 + 24 = 26
int hexVal = 0x1a;      // 10 * 16^0 + 1 * 16^1 = 10 + 16 = 26
int binVal = 0b11010;   // 2^1 + 2^3 + 2^4 = 2 + 8 + 16 = 26


 public class MyFirstProgram {
    public static void main(String[] args) {
        System.out.println("Hello\tWorld");
        System.out.println("HelloWorld\b\b\b\b\b");
        System.out.println("Hello\nWorld");
        System.out.println("Hello\rWorld");
        System.out.println("\'HelloWorld\'");
        System.out.println("\"HelloWorld\"");
        System.out.println("This is backslash - \\");
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        Integer x = 5;
        System.out.println(x.equals(5));
    }
}


String message; //declaration
message = "Hello World"; //initialization

public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 5;
        double y = 12.1313467445;
        System.out.printf("The value of variable x is %d%nThe value of variable y is %.4f", x,y);
    }
}


public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 10;
        double y = x;
        System.out.println(y);
    }
}
public class MyFirstProgram {
    public static void main(String[] args) {
        int years = 47;
        String name = "John Lord";
        System.out.println(years);
        System.out.println(name);
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        short myValue = 130;
        System.out.println(myValue);
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        int modulo = 10 % 3; // 10 = 3*3+1
        System.out.println(modulo);
    }
}
public class MyFirstProgram {
    public static void main(String[] args) {
        int value1 = 1;
        int value2 = 2;
        boolean isEqual = value1 == value2;
        System.out.println(isEqual);
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        int value1 = 1;
        int value2 = 2;
        System.out.println((value1 == 1) && (value2 == 2));
        System.out.println((value1 == 1) || (value2 == 2));
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        boolean success = false;
        System.out.println(success);
        System.out.println(!success);
    }
}


public class MyFirstProgram {
    public static void main (String[] args) {
        int age = 20;
               String message = (age < 18) ? "You can't enter" : "Welcome";
               System.out.println(message);
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        String s1 = "String";
        String s2 = "Value";
        System.out.println(s1 + s2) ili ("String" + "Value") ili (s1 + "Value") ili ("String"+ s2);
    }
}

public class MyFirstProgram {
    public static void main(String [] args) {
        int speed = 8;
        if (speed < 10) {
            System.out.println("Too slow...");
        }
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        int speed = 8;
        if(speed < 10)
            System.out.println("Too slow... inside IF");
        System.out.println("Too slow... inside outside IF");
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        if (1 == 1) {
            System.out.println("True");
        } else {
            System.out.println("false");
        }
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {
        int speed = 99;
        if (speed < 10) {
            System.out.println("Too slow...");
        } else if (speed <= 80) {
            System.out.println("Regular speed.");
        } else if (speed < 100) {
            System.out.println("Too fast!");
        }else {
            System.out.println("Incorrect value");

        }
    }
}

public class MyFirstProgram {
    public static void main(String[] args) {v
        String message = "";
        int age = 17;
        if (age < 18) {
            message = "You can't enter";
        } else {
            message = "Welcome";
        }
        System.out.println(message);
    }
}
Praktican primer upotrebe switch naredbe:
public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 1;
        switch (x) {
            case 0:
                System.out.println("zero");
                break;
            case 1:
                System.out.println("one");
                break;
            default:
                System.out.println("unknown value");
                break;
        }
    }
}
Visestruko poklapanje kod switch naredbe:
public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 2;
        switch(x) {
            case 1:
            case 2:
                System.out.println("Yes");
                break;
            default:
                System.out.println("No");
                break;
        }
    }
}

Unapredjeni switch:
public class MyFirstProgram {
    public static void main(String[] args) {
        int x = 0;
        switch (x) {
            case 0-> System.out.println("zero");
            case 1-> System.out.println("one");
            default -> System.out.println("unknown value");
        }
    }
}

// Petlje

public class MyFirstProgram {
    public static void main(String [] args) {
        for (int i = 0; i < 5;i++) {
            System.out.println("Hello World");
        }
    }
}
// PRECICA ZA KREIRANJE FOR PETLJE: CRTL + . !!!


// FOR PETLJA UNUTAR FOR PETLJE:
*/
public class MyFirstProgram {
    public static void main(String[] args) {
        class Car {
            String make;
            String model;

            void startEngine() {
                System.out.println("Engine started...");
            }
        }
    }
}




