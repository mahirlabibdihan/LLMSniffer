
public class FutureDayOfWeek {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Enter today's day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6): ");
        int today = scanner.nextInt();

        
        System.out.print("Enter the number of days elapsed since today: ");
        int elapsed = scanner.nextInt();

        
        int futureDay = (today + elapsed) % 7;

        
        System.out.print("Today is ");
        switch(today) {
            case 0: System.out.print("Sunday"); break;
            case 1: System.out.print("Monday"); break;
            case 2: System.out.print("Tuesday"); break;
            case 3: System.out.print("Wednesday"); break;
            case 4: System.out.print("Thursday"); break;
            case 5: System.out.print("Friday"); break;
            case 6: System.out.print("Saturday"); break;
        }
        System.out.print(" and the future day is ");
        switch(futureDay) {
            case 0: System.out.print("Sunday"); break;
            case 1: System.out.print("Monday"); break;
            case 2: System.out.print("Tuesday"); break;
            case 3: System.out.print("Wednesday"); break;
            case 4: System.out.print("Thursday"); break;
            case 5: System.out.print("Friday"); break;
            case 6: System.out.print("Saturday"); break;
        }
        System.out.println();

        scanner.close();
    }
}
