import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class BabyNameRanking {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the year, gender, and name
        System.out.print("Enter the year (2001-2010): ");
        int year = scanner.nextInt();

        // Validate the year input
        if (year < 2001 || year > 2010) {
            System.out.println("Invalid year. Please enter a year between 2001 and 2010.");
            System.exit(0);
        }

        System.out.print("Enter the gender (M/F): ");
        char gender = scanner.next().toUpperCase().charAt(0);

        // Validate the gender input
        if (gender != 'M' && gender != 'F') {
            System.out.println("Invalid gender. Please enter 'M' or 'F'.");
            System.exit(0);
        }

        System.out.print("Enter the name: ");
        String name = scanner.next();

        // Find and display the ranking of the name for the year
        findAndDisplayRanking(year, gender, name);

        // Close the scanner
        scanner.close();
    }

    // Method to find and display the ranking of the name for the year
    private static void findAndDisplayRanking(int year, char gender, String name) {
        try {
            // Create a file object for the corresponding year
            File file = new File("babynameranking" + year + ".txt");

            // Check if the file exists
            if (!file.exists()) {
                System.out.println("Error: Data file not found for the year " + year);
                System.exit(0);
            }

            // Scanner for reading the file
            Scanner fileScanner = new Scanner(file);

            // Process each line in the file
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();

                // Split the line into tokens
                String[] tokens = line.split("\\s+");

                // Check if the gender matches and the name is found
                if (gender == 'M' && tokens[2].equals(name)) {
                    System.out.println(name + " is ranked #" + tokens[0] + " in year " + year);
                    return;
                } else if (gender == 'F' && tokens[4].equals(name)) {
                    System.out.println(name + " is ranked #" + tokens[0] + " in year " + year);
                    return;
                }
            }

            // If the name is not found
            System.out.println("The name " + name + " is not ranked in year " + year);

            // Close the file scanner
            fileScanner.close();

        } catch (FileNotFoundException e) {
            // Handle file not found exception
            System.out.println("Error: File not found - " + e.getMessage());
        }
    }
}
