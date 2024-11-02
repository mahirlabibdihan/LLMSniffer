import java.util.Scanner;

public class ImprovedCalculator {

    public static void main(String[] args) {
        // Check if the correct number of command-line arguments are provided
        if (args.length != 3) {
            System.out.println("Usage: java ImprovedCalculator operand1 operator operand2");
            System.exit(0);
        }

        // Extract operands and operator from command-line arguments
        String operand1Str = args[0];
        String operator = args[1];
        String operand2Str = args[2];

        // Attempt to parse operands as doubles with exception handling
        double operand1 = parseDoubleWithException(operand1Str);
        double operand2 = parseDoubleWithException(operand2Str);

        // Perform the calculation based on the operator
        double result = calculateResult(operand1, operator, operand2);

        // Display the result
        System.out.println("Result: " + result);
    }

    // Method to parse a string as a double with exception handling
    private static double parseDoubleWithException(String str) {
        try {
            return Double.parseDouble(str);
        } catch (NumberFormatException e) {
            // Handle NumberFormatException
            System.out.println("Error: Non-numeric operand detected - " + e.getMessage());
            System.exit(0);
            return 0; // This return statement is unreachable, but added for compilation
        }
    }

    // Method to perform the calculation based on the operator
    private static double calculateResult(double operand1, String operator, double operand2) {
        switch (operator) {
            case "+":
                return operand1 + operand2;
            case "-":
                return operand1 - operand2;
            case "*":
                return operand1 * operand2;
            case "/":
                // Check for division by zero before performing the division
                if (operand2 == 0) {
                    System.out.println("Error: Cannot divide by zero");
                    System.exit(0);
                }
                return operand1 / operand2;
            default:
                System.out.println("Error: Invalid operator");
                System.exit(0);
                return 0; // This return statement is unreachable, but added for compilation
        }
    }
}
