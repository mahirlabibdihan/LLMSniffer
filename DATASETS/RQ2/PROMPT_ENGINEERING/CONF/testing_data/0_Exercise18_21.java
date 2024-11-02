/**
 * Welcome to the DecimalToBinaryConverter program!
 * This program converts a decimal number to binary.
 * Author: [Your Name]
 */

import java.util.Scanner;

public class DecimalToBinaryConverter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get input from the user
        System.out.print("Enter a decimal number: ");
        int decimalNumber = scanner.nextInt();

        // Display the result
        String binaryEquivalent = dec2Bin(decimalNumber);
        System.out.println("Binary equivalent: " + binaryEquivalent);
    }

    // Recursive method to convert a decimal number to binary
    private static String dec2Bin(int value) {
        if (value == 0) {
            return "0"; // Base case: when the value is 0, return "0"
        } else if (value == 1) {
            return "1"; // Base case: when the value is 1, return "1"
        } else {
            // Recursive case: concatenate the remainder with the recursive call
            return dec2Bin(value / 2) + value % 2;
        }
    }
}