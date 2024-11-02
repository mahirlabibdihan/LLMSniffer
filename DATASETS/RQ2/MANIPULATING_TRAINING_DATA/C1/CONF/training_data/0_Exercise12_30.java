import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CountLettersInFile {
    public static void main(String[] args) {
        // Prompt the user to enter a file name
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a file name: ");
        String fileName = scanner.nextLine();
        scanner.close();
        
        // Try to open the file and read its contents
        try {
            File file = new File(fileName);
            Scanner fileScanner = new Scanner(file);
            String fileContent = "";
            while (fileScanner.hasNextLine()) {
                fileContent += fileScanner.nextLine();
            }
            fileScanner.close();
            
            // Count the occurrences of each letter in the file
            Map<Character, Integer> letterCount = new HashMap<>();
            for (int i = 0; i < fileContent.length(); i++) {
                char c = fileContent.charAt(i);
                if (Character.isLetter(c)) {
                    c = Character.toLowerCase(c);
                    if (letterCount.containsKey(c)) {
                        letterCount.put(c, letterCount.get(c) + 1);
                    } else {
                        letterCount.put(c, 1);
                    }
                }
            }
            
            // Display the letter counts
            System.out.println("Letter counts for file " + fileName + ":");
            for (char c = 'a'; c <= 'z'; c++) {
                int count = letterCount.getOrDefault(c, 0);
                if (count > 0) {
                    System.out.println(c + ": " + count);
                }
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + fileName);
        }
    }
}