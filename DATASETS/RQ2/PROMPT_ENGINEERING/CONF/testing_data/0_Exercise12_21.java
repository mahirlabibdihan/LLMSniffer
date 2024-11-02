import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SortedStringsChecker {

    public static void main(String[] args) {
        // Open the file for reading
        File file = new File("SortedStrings.txt");

        try {
            // Create a Scanner to read from the file
            Scanner scanner = new Scanner(file);

            // Initialize variables
            boolean sorted = true;
            String prevString = null;
            String firstOutOfOrder1 = null;
            String firstOutOfOrder2 = null;

            // Read each string from the file
            while (scanner.hasNext()) {
                String currentString = scanner.next();

                // Check if the strings are in increasing order
                if (prevString != null && currentString.compareTo(prevString) < 0) {
                    sorted = false;
                    firstOutOfOrder1 = prevString;
                    firstOutOfOrder2 = currentString;
                    break; // Exit the loop if out of order strings are found
                }

                // Update the previous string for the next iteration
                prevString = currentString;
            }

            // Close the scanner to free up resources
            scanner.close();

            // Display the result
            if (sorted) {
                System.out.println("The strings in the file are sorted in increasing order.");
            } else {
                System.out.println("The strings in the file are not sorted.");
                System.out.println("First out-of-order strings: " + firstOutOfOrder1 + ", " + firstOutOfOrder2);
            }

        } catch (FileNotFoundException e) {
            // Handle file not found exception
            System.out.println("Error: File 'SortedStrings.txt' not found.");
        }
    }
}