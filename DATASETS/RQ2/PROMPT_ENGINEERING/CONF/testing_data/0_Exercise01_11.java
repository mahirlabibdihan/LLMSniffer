public class PopulationProjection {

    public static void main(String[] args) {
        // Initialize variables
        long currentPopulation = 312032486L;
        int secondsInYear = 365 * 24 * 60 * 60;

        // Calculate the number of births, deaths, and immigrants per year
        long birthsPerYear = secondsInYear / 7;
        long deathsPerYear = secondsInYear / 13;
        long immigrantsPerYear = secondsInYear / 45;

        // Display population projection for the next five years
        System.out.println("Population Projection for the Next Five Years:");
        for (int i = 1; i <= 5; i++) {
            currentPopulation += birthsPerYear - deathsPerYear + immigrantsPerYear;
            System.out.println("Year " + i + ": " + currentPopulation);
        }
    }
}