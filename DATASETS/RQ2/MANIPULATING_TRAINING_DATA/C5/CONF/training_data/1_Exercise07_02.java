

import java.util.Scanner;


public class NumberReverter {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Enter ten space-separated integers: ");

        int[] arr = new int[10];

        for (int i = 0; i < 10; i++) {
            arr[i] = input.nextInt();
        }

        displayReverse(arr);
        input.close();
    }

    private static void displayReverse(int[] arrRev) {
        for (int i = arrRev.length - 1; i >= 0; i--) {
            System.out.print(arrRev[i] + " ");

        }
    }
}
