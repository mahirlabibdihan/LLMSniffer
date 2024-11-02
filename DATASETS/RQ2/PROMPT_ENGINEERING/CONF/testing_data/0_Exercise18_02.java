import java.util.Scanner;

public class FibonacciCalculator {

    public static void main(String[] args) {
        // Welcome message
        System.out.println("Welcome to the Fibonacci Number Calculator!");

        // Get the index from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an index for a Fibonacci number: ");
        int index = scanner.nextInt();

        // Calculate and display the Fibonacci number at the given index
        long fibonacciNumber = calculateFibonacci(index);
        System.out.println("The Fibonacci number at index " + index + " is: " + fibonacciNumber);
    }

    // Iterative method to calculate Fibonacci number
    public static long calculateFibonacci(int n) {
        // Base cases
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        // Initialize variables for two previous Fibonacci numbers
        long f0 = 0;
        long f1 = 1;
        long currentFib = 0;

        // Calculate Fibonacci numbers iteratively
        for (int i = 2; i <= n; i++) {
            currentFib = f0 + f1;
            f0 = f1;
            f1 = currentFib;
        }

        // After the loop, currentFib is fib(n)
        return currentFib;
    }
}
