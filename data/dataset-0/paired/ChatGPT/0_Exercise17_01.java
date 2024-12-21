import java.io.*;
import java.util.Random;

public class Exercise17_01 {
    public static void main(String[] args) {
        try {
            // Open the file for appending or create a new file if it doesn't exist
            FileWriter fileWriter = new FileWriter("Exercise17_01.txt", true);

            // Write 100 random integers to the file, separated by spaces
            Random random = new Random();
            for (int i = 0; i < 100; i++) {
                int num = random.nextInt(100);
                fileWriter.write(num + " ");
            }

            // Close the file writer
            fileWriter.close();

            System.out.println("Data written to file.");
        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }
    }
}
