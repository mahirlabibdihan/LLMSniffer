import java.util.Scanner;

public class CompoundValueCalculator {
    public static void main(String[] args) {
        // Welcome message
        System.out.println("Welcome to the Compound Value Calculator Program!");

        // Get input from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the monthly saving amount (e.g., 100): ");
        double monthlySavingAmount = scanner.nextDouble();
        System.out.print("Enter the annual interest rate (e.g., 5): ");
        double annualInterestRate = scanner.nextDouble();
        System.out.print("Enter the number of months (e.g., 6): ");
        int numberOfMonths = scanner.nextInt();

        // Calculate monthly interest rate
        double monthlyInterestRate = annualInterestRate / 1200;

        // Calculate the future value of the savings account
        double futureValue = 0;
        for (int i = 1; i <= numberOfMonths; i++) {
            futureValue = (monthlySavingAmount + futureValue) * (1 + monthlyInterestRate);
        }

        // Display the result
        System.out.println("The amount in the savings account after " + numberOfMonths + " months: $" + futureValue);

        // Display a closing message
        System.out.println("\nThank you for using the Compound Value Calculator Program!");

        // Close the scanner
        scanner.close();
    }
}