import java.util.Calendar;

public class ShowCurrentDateTime {
    public static void main(String[] args) {
        // Create a Calendar object to get the current date and time
        Calendar now = Calendar.getInstance();

        // Get the year, month, and day
        int year = now.get(Calendar.YEAR);
        int month = now.get(Calendar.MONTH) + 1; // January is 0, so add 1 to get the correct month
        int day = now.get(Calendar.DAY_OF_MONTH);

        // Get the hour, minute, and second
        int hour = now.get(Calendar.HOUR_OF_DAY);
        int minute = now.get(Calendar.MINUTE);
        int second = now.get(Calendar.SECOND);

        // Display the current date and time
        System.out.printf("Current date and time is %04d-%02d-%02d %02d:%02d:%02d%n", year, month, day, hour, minute, second);
    }
}