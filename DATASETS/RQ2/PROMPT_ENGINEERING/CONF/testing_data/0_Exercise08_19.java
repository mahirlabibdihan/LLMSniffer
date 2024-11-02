import java.util.Scanner;

public class ConsecutiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of rows: ");
        int rows = scanner.nextInt();
        
        System.out.println("Enter the number of columns: ");
        int columns = scanner.nextInt();
        
        int[][] array = new int[rows][columns];
        
        System.out.println("Enter the values in the array: ");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                array[i][j] = scanner.nextInt();
            }
        }
        
        boolean containsConsecutiveFour = isConsecutiveFour(array);
        
        System.out.println("The array contains four consecutive numbers with the same value: " + containsConsecutiveFour);
    }

    public static boolean isConsecutiveFour(int[][] values) {
        int rows = values.length;
        int columns = values[0].length;

        // Check horizontally
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns - 3; j++) {
                if (values[i][j] == values[i][j + 1]
                    && values[i][j] == values[i][j + 2]
                    && values[i][j] == values[i][j + 3]) {
                    return true;
                }
            }
        }

        // Check vertically
        for (int j = 0; j < columns; j++) {
            for (int i = 0; i < rows - 3; i++) {
                if (values[i][j] == values[i + 1][j]
                    && values[i][j] == values[i + 2][j]
                    && values[i][j] == values[i + 3][j]) {
                    return true;
                }
            }
        }

        // Check diagonally (top-left to bottom-right)
        for (int i = 0; i < rows - 3; i++) {
            for (int j = 0; j < columns - 3; j++) {
                if (values[i][j] == values[i + 1][j + 1]
                    && values[i][j] == values[i + 2][j + 2]
                    && values[i][j] == values[i + 3][j + 3]) {
                    return true;
                }
            }
        }

        // Check diagonally (bottom-left to top-right)
        for (int i = 3; i < rows; i++) {
            for (int j = 0; j < columns - 3; j++) {
                if (values[i][j] == values[i - 1][j + 1]
                    && values[i][j] == values[i - 2][j + 2]
                    && values[i][j] == values[i - 3][j + 3]) {
                    return true;
                }
            }
        }

        return false;
    }
}