import java.util.Scanner;

public class MonthDaysDisplay {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Get user input for the year and the first day of the year
        System.out.print("Enter the year (e.g., 2013): ");
        int year = input.nextInt();

        System.out.print("Enter the first day of the year (0 for Sunday, 1 for Monday, ..., 6 for Saturday): ");
        int firstDay = input.nextInt();

        // Validate user input
        if (year < 0 || firstDay < 0 || firstDay > 6) {
            System.out.println("Invalid input. Please enter valid values.");
            return;
        }

        // Array to store the names of the months
        String[] months = {"January", "February", "March", "April", "May", "June", "July",
                           "August", "September", "October", "November", "December"};

        // Array to store the names of the days
        String[] days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        // Display the first day of each month
        for (int month = 1; month <= 12; month++) {
            System.out.print(months[month - 1] + " 1, " + year + " is ");
            
            // Calculate the day of the week for the first day of the month
            int dayOfWeek = (firstDay + (month - 1) * 31) % 7;
            
            System.out.println(days[dayOfWeek]);
        }

        // Close the Scanner to avoid resource leak
        input.close();
    }
}