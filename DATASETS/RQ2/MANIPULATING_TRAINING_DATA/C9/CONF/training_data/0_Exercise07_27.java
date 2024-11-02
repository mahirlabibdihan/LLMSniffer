public static boolean equals(int[] list1, int[] list2) {
    if (list1.length != list2.length) {
        return false;
    }
    Arrays.sort(list1);
    Arrays.sort(list2);
    for (int i = 0; i < list1.length; i++) {
        if (list1[i] != list2[i]) {
            return false;
        }
    }
    return true;
}
 import java.util.Arrays;
import java.util.Scanner;

public class IdenticalArrays {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt user to enter list1
        System.out.print("Enter list1: ");
        int[] list1 = readArray(input);

        // Prompt user to enter list2
        System.out.print("Enter list2: ");
        int[] list2 = readArray(input);

        // Check if the arrays are identical
        if (equals(list1, list2)) {
            System.out.println("Two lists are identical");
        } else {
            System.out.println("Two lists are not identical");
        }
    }

    // Reads an array from user input
    public static int[] readArray(Scanner input) {
        int length = input.nextInt();
        int[] array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = input.nextInt();
        }
        return array;
    }

    // Implements the equals method as described earlier
    public static boolean equals(int[] list1, int[] list2) {
        if (list1.length != list2.length) {
            return false;
        }
        Arrays.sort(list1);
        Arrays.sort(list2);
        for (int i = 0; i < list1.length; i++) {
            if (list1[i] != list2[i]) {
                return false;
            }
        }
        return true;
    }
}