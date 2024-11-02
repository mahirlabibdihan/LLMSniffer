public class PerfectNumbers {

    public static void main(String[] args) {
        int limit = 10000;

        System.out.println("Perfect numbers less than " + limit + ":");
        for (int number = 2; number < limit; number++) {
            if (isPerfectNumber(number)) {
                System.out.println(number);
            }
        }
    }

    // Check if a number is a perfect number
    private static boolean isPerfectNumber(int number) {
        int sum = 1; // 1 is always a divisor

        for (int divisor = 2; divisor <= number / 2; divisor++) {
            if (number % divisor == 0) {
                sum += divisor;
            }
        }

        return sum == number;
    }
}