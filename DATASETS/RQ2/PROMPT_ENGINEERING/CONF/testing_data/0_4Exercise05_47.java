import java.util.Scanner;

public class ISBN13Checker {
    public static void main(String[] args) {
        // Welcome message
        System.out.println("Welcome to the ISBN-13 Checker Program!");

        // Get input from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first 12 digits of an ISBN-13 as a string: ");
        String userInput = scanner.nextLine();

        // Check if the input has exactly 12 digits
        if (userInput.length() != 12) {
            System.out.println(userInput + " is an invalid input");
        } else {
            // Convert the string to an array of integers
            int[] digits = new int[12];
            for (int i = 0; i < 12; i++) {
                digits[i] = Character.getNumericValue(userInput.charAt(i));
            }

            // Calculate the checksum
            int checksum = 10 - ((digits[0] + 3 * digits[1] + digits[2] + 3 * digits[3] +
                    digits[4] + 3 * digits[5] + digits[6] + 3 * digits[7] + digits[8] +
                    3 * digits[9] + digits[10] + 3 * digits[11]) % 10);

            // If the checksum is 10, replace it with 0
            if (checksum == 10) {
                checksum = 0;
            }

            // Display the ISBN-13 number
            System.out.println("The ISBN-13 number is " + userInput + checksum);
        }

        // Display a closing message
        System.out.println("\nThank you for using the ISBN-13 Checker Program!");
        
        // Close the scanner
        scanner.close();
    }
}