/**
 * This is a BMI calculator class. It calculates BMI based on name, age, weight,
 * feet, and inches.
 */
public class BMI {
    private String name; // The name of the person
    private int age; // The age of the person
    private double weight; // The weight of the person in pounds
    private double feet; // The height of the person in feet
    private double inches; // The height of the person in inches

    /**
     * This is a constructor for creating a BMI object with all the specified details.
     *
     * @param name   - The name of the person.
     * @param age    - The age of the person.
     * @param weight - The weight of the person in pounds.
     * @param feet   - The height of the person in feet.
     * @param inches - The height of the person in inches.
     */
    public BMI(String name, int age, double weight, double feet, double inches) {
        this.name = name;
        this.age = age;
        this.weight = weight;
        this.feet = feet;
        this.inches = inches;
    }

    /**
     * This method calculates the BMI (Body Mass Index) based on the provided
     * weight, feet, and inches, and returns the result.
     *
     * @return The calculated BMI.
     */
    public double calculateBMI() {
        double heightInInches = (feet * 12) + inches;
        double bmi = (weight / (heightInInches * heightInInches)) * 703;
        return bmi;
    }

    /**
     * This method returns the name of the person.
     *
     * @return The name of the person.
     */
    public String getName() {
        return name;
    }

    /**
     * This method returns the age of the person.
     *
     * @return The age of the person.
     */
    public int getAge() {
        return age;
    }

    /**
     * This method returns the weight of the person in pounds.
     *
     * @return The weight of the person in pounds.
     */
    public double getWeight() {
        return weight;
    }

    /**
     * This method returns the height of the person in feet and inches.
     *
     * @return The height of the person in feet and inches.
     */
    public String getHeight() {
        return feet + " feet " + inches + " inches";
    }
}