public class DivisibleNumbersFinder {

    public static void main(String[] args) {
        // Loop through numbers from 100 to 200
        for (int i = 100; i <= 200; i++) {
            // Check if the number is divisible by 5 or 6, but not both
            if ((i % 5 == 0 && i % 6 != 0) || (i % 5 != 0 && i % 6 == 0)) {
                // Print the number
                System.out.print(i + " ");

                // Check if ten numbers have been printed and start a new line
                if (i % 10 == 0) {
                    System.out.println();
                }
            }
        }
    }
}