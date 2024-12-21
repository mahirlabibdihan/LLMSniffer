public class LunarCalendar {
    public static int getDaysInMonth(int month, int year) {
        if (month < 1 || month > 12) {
            throw new IllegalArgumentException("Invalid month");
        }
        if (year < 0) {
            throw new IllegalArgumentException("Invalid year");
        }

        int[] daysInMonth = {29, 30};
        return daysInMonth[month % 2];
    }

    public static void main(String[] args) {
        int month = 3;
        int year = 2022;
        int days = getDaysInMonth(month, year);
        System.out.println("Month: " + month + ", Year: " + year + ", Days: " + days);
    }
}

