/**
 * Welcome to the SeriesCalculator program!
 * This program calculates and displays the series m(i) for i = 1, 2, ..., 10.
 * Author: Harry Dulaney
 */

public class SeriesCalculator {

    public static void main(String[] args) {
        // Display the series for i = 1 to 10
        for (int i = 1; i <= 10; i++) {
            double result = computeSeries(i);
            System.out.println("m(" + i + ") = " + result);
        }
    }

    // Recursive method to compute the series m(i)
    private static double computeSeries(int i) {
        if (i == 1) {
            return 1.0 / 2;
        } else {
            return i / (i + 1.0) + computeSeries(i - 1);
        }
    }
}
