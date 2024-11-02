


public class SquareRootCalculator{
    public static void main(String[] args) {
        for (int i = 10; i < 100; i += 10) { 
            System.out.println("The result of the Babylonian sqrt method for: " + i + " = " + sqrt(i));
            System.out.println("The result of Math.sqrt(i) method for: " + i + " = " + Math.sqrt(i));
        }
    }

    public static double sqrt(long n) {
        double lastGuess = 2;
        double nextGuess = (lastGuess + n / lastGuess) / 2;

        while (!diff(nextGuess, lastGuess)) {
            lastGuess = nextGuess;
            nextGuess = (lastGuess + n / lastGuess) / 2;
        }
        return nextGuess;

    }

    static boolean diff(double a, double b) {
        return Math.abs(a - b) < 0.0001; 
    }
}
