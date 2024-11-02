import java.util.Scanner;

public class ReverseDisplayInt {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get user input
        System.out.print("Enter an integer: ");
        int inputValue = scanner.nextInt();

        // Display reversal
        reverseDisplay(inputValue);
    }

    public static void reverseDisplay(int value) {
        reverseDisplayHelper(value);
    }

    private static void reverseDisplayHelper(int value) {
        if (value > 0) {
            // Display the last digit of the value
            System.out.print(value % 10);

            // Recursively invoke with the remaining digits
            reverseDisplayHelper(value / 10);
        }
    }
}