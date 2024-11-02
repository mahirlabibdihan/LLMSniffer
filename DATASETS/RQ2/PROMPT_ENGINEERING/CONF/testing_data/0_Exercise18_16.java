/**
 * Welcome to the UppercaseLetterCounter program!
 * This program counts the number of uppercase letters in an array.
 * Author: [Your Name]
 */

import java.util.Scanner;

public class UppercaseLetterCounter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get input from the user
        System.out.print("Enter a list of characters separated by spaces: ");
        String inputString = scanner.nextLine();
        char[] charArray = inputString.toCharArray();

        // Display the result
        int count = countUppercaseLetters(charArray);
        System.out.println("Number of uppercase letters: " + count);
    }

    // Method to count uppercase letters in an array
    public static int count(char[] chars) {
        return count(chars, chars.length - 1);
    }

    // Recursive helper method
    private static int count(char[] chars, int high) {
        if (high < 0) {
            return 0; // Base case: reached the beginning of the array
        } else {
            int currentCount = Character.isUpperCase(chars[high]) ? 1 : 0;
            return currentCount + count(chars, high - 1);
        }
    }
}
