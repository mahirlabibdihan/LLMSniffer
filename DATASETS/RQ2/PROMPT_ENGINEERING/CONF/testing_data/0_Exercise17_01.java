import java.io.*;
import java.util.Random;

public class Exercise17_01 {

    public static void main(String[] args) {
        // Define the file name
        String fileName = "Exercise17_01.txt";

        // Create a File object
        File file = new File(fileName);

        // Check if the file exists
        if (file.exists()) {
            System.out.println("File already exists. Appending data...");
        } else {
            System.out.println("File does not exist. Creating a new file...");
        }

        try {
            // Create a FileWriter with append mode
            FileWriter fileWriter = new FileWriter(file, true);

            // Create a BufferedWriter for efficient writing
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

            // Create a Random object to generate random integers
            Random random = new Random();

            // Write 100 random integers to the file
            for (int i = 0; i < 100; i++) {
                int randomInt = random.nextInt(1000); // Generate a random integer between 0 and 999
                String intString = Integer.toString(randomInt); // Convert integer to String
                bufferedWriter.write(intString); // Write the integer to the file
                bufferedWriter.write(" "); // Add a space to separate integers
            }

            // Close the BufferedWriter to save changes
            bufferedWriter.close();

            System.out.println("Data appended successfully.");
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
