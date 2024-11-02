import java.util.*;

public class DateDisplay {
    public static void main(String[] args) {
        // Creating a GregorianCalendar object to work with dates
        GregorianCalendar currentDate = new GregorianCalendar();

        // Fetching current year, month, and day
        int currentYear = currentDate.get(Calendar.YEAR);
        int currentMonth = currentDate.get(Calendar.MONTH) + 1; // Months are indexed from 0
        int currentDay = currentDate.get(Calendar.DAY_OF_MONTH);

        // Displaying current date
        System.out.println("Today's Date:");
        System.out.println("Year: " + currentYear);
        System.out.println("Month: " + currentMonth);
        System.out.println("Day: " + currentDay);

        // Now, let's set a specific time and display the date
        long specifiedTime = 1234567898765L;
        currentDate.setTimeInMillis(specifiedTime);

        // Fetching year, month, and day for the specified time
        int specifiedYear = currentDate.get(Calendar.YEAR);
        int specifiedMonth = currentDate.get(Calendar.MONTH) + 1;
        int specifiedDay = currentDate.get(Calendar.DAY_OF_MONTH);

        // Displaying the date for the specified time
        System.out.println("\nDate for 1234567898765 milliseconds after January 1, 1970:");
        System.out.println("Year: " + specifiedYear);
        System.out.println("Month: " + specifiedMonth);
        System.out.println("Day: " + specifiedDay);
    }
}