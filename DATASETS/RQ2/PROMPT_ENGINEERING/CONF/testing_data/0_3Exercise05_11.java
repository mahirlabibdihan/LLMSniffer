// Program to find numbers divisible by 5 or 6, but not both, in the range 100 to 200
public class DivisibleNumbersFinder {

    public static void main(String[] args) {
        // Loop through the numbers from 100 to 200
        for (int number = 100; number <= 200; number++) {
            // Check if the number is divisible by 5 or 6, but not both
            if ((number % 5 == 0 || number % 6 == 0) && !(number % 5 == 0 && number % 6 == 0)) {
                System.out.print(number + " "); // Display the number

                // Check if it's the tenth number on the line
                if (number % 10 == 0) {
                    System.out.println(); // Move to the next line
                }
            }
        }
    }
}