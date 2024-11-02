import java.io.*;
import java.util.*;
import java.text.*;

public class FileDataStorer {

    public static void main(String[] args) {
        System.out.println("Starting data storage...");

        int[] intArray = {1, 2, 3, 4, 5};
        Date currentDate = new Date();
        double doubleValue = 5.5;

        try {
            // Create a file named Exercise17_05.dat
            FileOutputStream fileOutputStream = new FileOutputStream("Exercise17_05.dat");
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);

            // Write the data to the file
            objectOutputStream.writeObject(intArray);
            objectOutputStream.writeObject(currentDate);
            objectOutputStream.writeDouble(doubleValue);

            objectOutputStream.close();

            System.out.println("Data successfully stored in Exercise17_05.dat.");
        } catch (IOException e) {
            System.err.println("An error occurred while storing data: " + e.getMessage());
        }
    }
}
