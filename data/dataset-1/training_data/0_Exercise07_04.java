import java.util.Scanner;

public class AnalyzeScores {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double[] scores = new double[100]; // array to store scores
        int count = 0; // number of scores entered
        double sum = 0; // sum of all scores entered
        
        // read scores until a negative number is entered
        System.out.print("Enter scores (negative number to end): ");
        double score = input.nextDouble();
        while (score >= 0 && count < 100) {
            scores[count] = score;
            sum += score;
            count++;
            score = input.nextDouble();
        }
        
        // calculate average score
        double average = sum / count;
        
        // count scores above and below average
        int aboveAverage = 0;
        int belowAverage = 0;
        for (int i = 0; i < count; i++) {
            if (scores[i] >= average) {
                aboveAverage++;
            } else {
                belowAverage++;
            }
        }
        
        // display results
        System.out.println("Average score: " + average);
        System.out.println("Number of scores above or equal to the average: " + aboveAverage);
        System.out.println("Number of scores below the average: " + belowAverage);
    }
}