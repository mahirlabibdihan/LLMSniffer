import java.io.*;
import java.net.URL;
import java.util.Scanner;

public class FacultySalaryAnalyzer {

    public static void main(String[] args) {
        try {
            URL url = new URL("http://cs.armstrong.edu/liang/data/Salary.txt");
            Scanner scanner = new Scanner(url.openStream());

            double totalAssistantSalary = 0;
            double totalAssociateSalary = 0;
            double totalFullSalary = 0;
            double totalFacultySalary = 0;

            int assistantCount = 0;
            int associateCount = 0;
            int fullCount = 0;
            int facultyCount = 0;

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] tokens = line.split(" ");

                if (tokens.length == 4) {
                    String rank = tokens[2];
                    double salary = Double.parseDouble(tokens[3]);

                    if ("assistant".equalsIgnoreCase(rank)) {
                        totalAssistantSalary += salary;
                        assistantCount++;
                    } else if ("associate".equalsIgnoreCase(rank)) {
                        totalAssociateSalary += salary;
                        associateCount++;
                    } else if ("full".equalsIgnoreCase(rank)) {
                        totalFullSalary += salary;
                        fullCount++;
                    }

                    totalFacultySalary += salary;
                    facultyCount++;
                }
            }

            printResults("Assistant", totalAssistantSalary, assistantCount);
            printResults("Associate", totalAssociateSalary, associateCount);
            printResults("Full", totalFullSalary, fullCount);
            printResults("Faculty", totalFacultySalary, facultyCount);

            scanner.close();

        } catch (IOException e) {
            System.out.println("Error reading data from the URL.");
        }
    }

    private static void printResults(String rank, double totalSalary, int count) {
        System.out.println("Total " + rank + " Salary: $" + totalSalary);
        System.out.println("Average " + rank + " Salary: $" + (count != 0 ? totalSalary / count : 0));
        System.out.println();
    }
}