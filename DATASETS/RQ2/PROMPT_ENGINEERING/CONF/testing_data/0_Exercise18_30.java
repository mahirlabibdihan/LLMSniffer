import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

// Welcome to the WordFinder program!

public class WordFinder {

    public static void main(String[] args) {
        // Check for the correct number of command line arguments
        if (args.length != 2) {
            System.out.println("Usage: java WordFinder <directory> <word>");
            return;
        }

        // Extracting directory and word from command line arguments
        String directoryName = args[0];
        String wordToFind = args[1];

        // Finding and displaying occurrences of the word in files under the directory
        findOccurrences(new File(directoryName), wordToFind);
    }

    // Recursive method to find occurrences of a word in files under a directory
    public static void findOccurrences(File directory, String word) {
        // Checking if the given file is a directory
        if (directory.isDirectory()) {
            File[] files = directory.listFiles();

            // Iterating through files in the directory
            if (files != null) {
                for (File file : files) {
                    // Recursive call for each file or subdirectory
                    findOccurrences(file, word);
                }
            }
        } else {
            // If the given file is a regular file, read its content and find occurrences of the word
            try (BufferedReader reader = new BufferedReader(new FileReader(directory))) {
                String line;
                int lineNumber = 0;

                // Reading lines from the file
                while ((line = reader.readLine()) != null) {
                    lineNumber++;

                    // Checking if the line contains the word
                    if (line.contains(word)) {
                        System.out.println("File: " + directory.getAbsolutePath() +
                                ", Line: " + lineNumber + ", Occurrence: " + line);
                    }
                }
            } catch (IOException e) {
                System.err.println("Error reading file: " + directory.getAbsolutePath());
            }
        }
    }
}
