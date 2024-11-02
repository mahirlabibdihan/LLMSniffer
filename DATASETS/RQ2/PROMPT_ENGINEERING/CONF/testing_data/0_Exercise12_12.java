import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class BraceStyleConverter {

    public static void main(String[] args) {
        // Check if the correct number of command-line arguments are provided
        if (args.length != 1) {
            System.out.println("Usage: java BraceStyleConverter <JavaSourceCodeFile>");
            return;
        }

        // Get the file name from the command-line argument
        String fileName = args[0];

        // Attempt to convert the Java source code file
        try {
            // Read the original Java source code
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder originalCode = new StringBuilder();

            String line;
            while ((line = reader.readLine()) != null) {
                originalCode.append(line).append("\n");
            }

            // Close the reader
            reader.close();

            // Convert the Java source code to end-of-line brace style
            String convertedCode = convertToEOLBraceStyle(originalCode.toString());

            // Write the converted code back to the file
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
            writer.write(convertedCode);

            // Close the writer
            writer.close();

            System.out.println("Java source code converted successfully.");

        } catch (IOException e) {
            // Handle IOException
            System.out.println("Error converting Java source code: " + e.getMessage());
        }
    }

    // Method to convert next-line brace style to end-of-line brace style
    private static String convertToEOLBraceStyle(String originalCode) {
        // Replace next-line braces with end-of-line braces
        return originalCode.replaceAll("\\)\\s*\\{", ") {");
    }
}
