public class AverageSpeed {
    public static void main(String[] args) {
        double distanceInKm = 14.0;
        double timeInMinutes = 45.5; 
        double timeInHours = timeInMinutes / 60.0;
        double distanceInMiles = distanceInKm / 1.6;
        double speedInMph = distanceInMiles / timeInHours;

        System.out.println("Average speed in miles per hour: " + speedInMph);
    }
}