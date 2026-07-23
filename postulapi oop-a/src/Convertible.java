public class Convertible extends Car{

    String roofType;
    public Convertible(String make, String model, int weight, String color, String roofType) {
        super(make, model, weight, color);
        this.roofType = roofType;
    }

    @Override
    String getInfo() {
        return "Make: " + this.getMake() + "\n" +
                "Model: " + this.getModel() + "\n" +
                "Weight: " + this.getWeight() + "\n" +
                "Color: " + this.getColor() + "\n" +
                "Roof Type: " + this.roofType;
    }
    }

/* 1@Override
String getInfo() {
    return super.getInfo() + "\n" +
            "Roof type: " + this.roofType;
}
// SKRACENA VERZIJA
 */

