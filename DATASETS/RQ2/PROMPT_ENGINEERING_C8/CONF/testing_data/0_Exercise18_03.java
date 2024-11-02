import java.util.Scanner;public class RecursiveGCDCalculator {    public static void main(String[] args) {        // Welcome message        System.out.println("Welcome to the Greatest Common Divisor (GCD) Calculator!");        // Get two integers from the user        Scanner scanner = new Scanner(System.in);        System.out.print("Enter the first integer: ");        int m = scanner.nextInt();        System.out.print("Enter the second integer: ");        int n = scanner.nextInt();        // Calculate and display the GCD        int gcdResult = findGCD(m, n);        System.out.println("The GCD of " + m + " and " + n + " is: " + gcdResult);    }    // Recursive method to find the GCD    public static int findGCD(int m, int n) {        // Base case: if n is 0, the GCD is m        if (n == 0) {            return m;        }        // Recursive call to find GCD using Euclidean algorithm        return findGCD(n, m % n);    }}