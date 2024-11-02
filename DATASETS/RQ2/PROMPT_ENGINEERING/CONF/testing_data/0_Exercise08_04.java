public class WeeklyHours {

    public static void main(String[] args) {
        int[][] weeklyHours = {
            {2, 4, 3, 4, 5, 8, 8},
            {7, 3, 4, 3, 3, 4, 4},
            {3, 3, 4, 3, 3, 2, 2},
            {9, 3, 4, 7, 3, 4, 1},
            {3, 5, 4, 3, 6, 3, 8},
            {3, 4, 4, 6, 3, 4, 4},
            {3, 7, 4, 8, 3, 8, 4},
            {6, 3, 5, 9, 2, 7, 9}
        };

        int[] totalHours = calculateTotalHours(weeklyHours);
        sortEmployees(weeklyHours, totalHours);

        displayResult(weeklyHours, totalHours);
    }

    public static int[] calculateTotalHours(int[][] hours) {
        int[] totalHours = new int[hours.length];
        for (int i = 0; i < hours.length; i++) {
            int sum = 0;
            for (int j = 0; j < hours[i].length; j++) {
                sum += hours[i][j];
            }
            totalHours[i] = sum;
        }
        return totalHours;
    }

    public static void sortEmployees(int[][] hours, int[] totalHours) {
        for (int i = 0; i < totalHours.length - 1; i++) {
            int maxIndex = i;
            for (int j = i + 1; j < totalHours.length; j++) {
                if (totalHours[j] > totalHours[maxIndex]) {
                    maxIndex = j;
                }
            }
            if (maxIndex != i) {
                int tempTotal = totalHours[maxIndex];
                totalHours[maxIndex] = totalHours[i];
                totalHours[i] = tempTotal;

                int[] tempHours = hours[maxIndex];
                hours[maxIndex] = hours[i];
                hours[i] = tempHours;
            }
        }
    }

    public static void displayResult(int[][] hours, int[] totalHours) {
        System.out.println("Employees and their total hours in decreasing order:");

        for (int i = 0; i < totalHours.length; i++) {
            int employeeNumber = i + 1;
            int total = totalHours[i];
            System.out.println("Employee " + employeeNumber + ": " + total + " hours");
        }
    }
}