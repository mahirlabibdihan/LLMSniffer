import java.util.Scanner;

public class PositiveNegativeAverage {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num, countPositive = 0, countNegative = 0, sum = 0, count = 0;
        double average;

        System.out.print("Enter an integer (0 to quit): ");
        num = scanner.nextInt();

        while (num != 0) {
            if (num > 0) {
                countPositive++;
                sum += num;
            } else if (num < 0) {
                countNegative++;
                sum += num;
            }
            count++;
            System.out.print("Enter an integer (0 to quit): ");
            num = scanner.nextInt();
        }

        if (count == 0) {
            System.out.println("No numbers are entered except 0");
        } else {
            average = (double) sum / (countPositive + countNegative);
            System.out.println("The number of positives is " + countPositive);
            System.out.println("The number of negatives is " + countNegative);
            System.out.println("The total is " + sum);
            System.out.printf("The average is %.2f%n", average);
        }
    }
}
