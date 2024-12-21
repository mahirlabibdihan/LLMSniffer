import java.util.Scanner;

public class Combinations {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner input = new Scanner(System.in);
        
        // Prompt the user to enter 10 integers
        System.out.print("Enter 10 integers: ");
        
        // Read the 10 integers into an array
        int[] nums = new int[10];
        for (int i = 0; i < 10; i++) {
            nums[i] = input.nextInt();
        }
        
        // Display all combinations of picking two numbers from the 10
        System.out.println("All combinations of picking two numbers:");
        for (int i = 0; i < 9; i++) {
            for (int j = i + 1; j < 10; j++) {
                System.out.println(nums[i] + " " + nums[j]);
            }
        }
    }
}