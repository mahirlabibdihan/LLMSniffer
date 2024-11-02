import java.io.*;

public class Exercise17_08 {
    public static void main(String[] args) {
        // Declare variables
        int executionCount = 0; // Initialize count to 0
        String fileName = "Exercise17_08.dat"; // Specify the file name
        
        // Try to read the count from the file
        try {
            File file = new File(fileName);
            if (file.exists()) {
                FileInputStream fileInput = new FileInputStream(file);
                ObjectInputStream objectInput = new ObjectInputStream(fileInput);
                executionCount = (int) objectInput.readObject();
                objectInput.close();
            }
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error reading the count from file: " + e.getMessage());
        }
        
        // Increase the count by 1
        executionCount++;
        
        // Display the count
        System.out.println("This program has been executed " + executionCount + " times.");
        
        // Try to write the updated count to the file
        try {
            FileOutputStream fileOutput = new FileOutputStream(fileName);
            ObjectOutputStream objectOutput = new ObjectOutputStream(fileOutput);
            objectOutput.writeObject(executionCount);
            objectOutput.close();
        } catch (IOException e) {
            System.err.println("Error writing the count to file: " + e.getMessage());
        }
    }
}