public class Car {

    private String make;
    private String model;
    private int weight;
    private String color;

    public String getName() {
        return make + " " + model;
    }
    public String getMake() {
        return make;
    }
    public void setMake(String make) {
        this.make = make;
    }
    public String getModel() {
        return model;
    }
    public void setModel(String model) {
        this.model = model;
    }
    public int getWeight() {
        return weight;
    }
    public void setWeight(int weight) {
        if (weight < 0) {
            this.weight = 0;
        } else if (weight > 3000) {
            this.weight = 3000;
        } else {
            this.weight = weight;
        }
    }
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }
    static int noCarInTheShowroom = 12;

    public Car () {

    }
    public Car(String make, String model, int weight, String color) {
        this.make = make;
        this.model = model;
        this.weight = weight;
        this.color = color;
    }

    String getInfo() {
        return "Make: " + this.make + "\n" +
                "MOdel: " + this.model + "\n" +
                "Weight: " + this.weight + "\n" +
                "Color: " + this.color;
    }
}
