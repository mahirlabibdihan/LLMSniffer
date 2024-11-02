import java.util.Scanner;

public class ISBNChecker {

    public static void main(String[] args) {
        // Welcome message
        System.out.println("ISBN-13 Checker");

        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the first 12 digits of an ISBN-13 as a string
        System.out.print("Enter the first 12 digits of an ISBN-13 as a string: ");
        String input = scanner.nextLine();

        // Check if the input length is exactly 12
        if (input.length() == 12) {
            // Calculate the checksum using the given formula
            int checksum = calculateChecksum(input);

            // Calculate the last digit based on the checksum
            int lastDigit = (10 - checksum) % 10;

            // Display the complete ISBN-13 number
            System.out.println("The ISBN-13 number is " + input + lastDigit);
        } else {
            // Display an error message for invalid input
            System.out.println(input + " is an invalid input");
        }

        // Close the Scanner
        scanner.close();
    }

    // Function to calculate the checksum for ISBN-13
    private static int calculateChecksum(String input) {
        int sum = 0;
        for (int i = 0; i < 12; i++) {
            int digit = Character.getNumericValue(input.charAt(i));
            if (i % 2 == 0) {
                sum += digit;
            } else {
                sum += 3 * digit;
            }
        }
        return sum % 10;
    }
}