

import java.util.*;


public class Exercise07_31 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter list1: ");
        int n1 = in.nextInt();
        int[] l1 = new int[n1];
        int i = 0;
        while (i < n1) {
            l1[i++] = in.nextInt();
        }

        System.out.println("Enter list2: ");
        int n2 = in.nextInt();
        int[] l2 = new int[n2];
        i = 0;
        while (i < n2) {
            l2[i++] = in.nextInt();
        }


        System.out.println(Arrays.toString(merge(l1, l2)));

    }

    public static int[] merge(int[] list1, int[] list2) {
        int len = list1.length + list2.length;
        int startL2 = list1.length;
        int[] result = new int[len];
        System.arraycopy(list1, 0, result, 0, list1.length);
        System.arraycopy(list2, 0, result, startL2, list2.length);

        Arrays.sort(result);
        return result;

    }
}