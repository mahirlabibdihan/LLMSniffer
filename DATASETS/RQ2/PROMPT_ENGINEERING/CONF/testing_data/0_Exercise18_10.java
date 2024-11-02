/**
 * Welcome to the CharacterCounter program!
 * This program counts the occurrences of a specified letter in a string.
 * Author: [Your Name]
 */

import java.util.Scanner;

public class CharacterCounter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get input from the user
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();

        System.out.print("Enter a character to count: ");
        char targetChar = scanner.next().charAt(0);

        // Display the result
        int count = countOccurrences(inputString, targetChar);
        System.out.println("Occurrences of '" + targetChar + "' in the string: " + count);
    }

    // Recursive method to count occurrences of a specified character in a string
    private static int countOccurrences(String str, char a) {
        if (str.length() == 0) {
            return 0;
        } else {
            int currentCount = (str.charAt(0) == a) ? 1 : 0;
            return currentCount + countOccurrences(str.substring(1), a);
        }
    }
}
