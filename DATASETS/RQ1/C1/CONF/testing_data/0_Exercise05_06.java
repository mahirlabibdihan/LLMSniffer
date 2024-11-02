public class ConversionTable {
    public static void main(String[] args) {
        System.out.println("Miles Kilometers\t|\tKilometers Miles");
        System.out.println("-----------------------------------------------");

        for (int i = 1; i <= 10; i++) {
            double kilometers = i * 1.609;
            int miles = i * 5 + 15;

            System.out.printf("%d %.3f\t|\t%d %.3f\n", i, kilometers, miles, miles / 1.609);
        }
    }
}