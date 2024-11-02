import java.util.Scanner;

public class MeanAndStdDeviation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter ten numbers
        System.out.print("Enter ten numbers: ");
        double[] numbers = new double[10];
        for (int i = 0; i < 10; i++) {
            numbers[i] = input.nextDouble();
        }

        // Calculate the mean
        double sum = 0;
        for (double number : numbers) {
            sum += number;
        }
        double mean = sum / 10;

        // Calculate the standard deviation
        double deviation = 0;
        for (double number : numbers) {
            deviation += Math.pow(number - mean, 2);
        }
        deviation = Math.sqrt(deviation / 9);

        // Display the results
        System.out.printf("The mean is %.2f\n", mean);
        System.out.printf("The standard deviation is %.5f\n", deviation);
    }
}
