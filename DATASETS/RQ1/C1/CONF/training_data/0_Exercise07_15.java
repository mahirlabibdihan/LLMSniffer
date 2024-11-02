import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Read in ten integers
        int[] numbers = new int[10];
        System.out.print("Enter ten integers: ");
        for (int i = 0; i < 10; i++) {
            numbers[i] = new java.util.Scanner(System.in).nextInt();
        }
        
        // Eliminate duplicates and display the result
        int[] result = eliminateDuplicates(numbers);
        System.out.print("The distinct numbers are: ");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + " ");
        }
    }
    
    public static int[] eliminateDuplicates(int[] list) {
        // Sort the array to group duplicate values together
        Arrays.sort(list);
        
        // Count the number of distinct values
        int count = 1;
        for (int i = 1; i < list.length; i++) {
            if (list[i] != list[i-1]) {
                count++;
            }
        }
        
        // Create a new array with the distinct values
        int[] result = new int[count];
        result[0] = list[0];
        int j = 1;
        for (int i = 1; i < list.length; i++) {
            if (list[i] != list[i-1]) {
                result[j] = list[i];
                j++;
            }
        }
        
        return result;
    }
}