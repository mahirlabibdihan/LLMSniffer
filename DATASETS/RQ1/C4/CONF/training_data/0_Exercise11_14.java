import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.print("Enter five integers for list1: ");
        ArrayList<Integer> list1 = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            int num = input.nextInt();
            list1.add(num);
        }

        
        System.out.print("Enter five integers for list2: ");
        ArrayList<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            int num = input.nextInt();
            list2.add(num);
        }

        
        ArrayList<Integer> result = union(list1, list2);
        System.out.print("The combined list is ");
        for (int num : result) {
            System.out.print(num + " ");
        }
    }

    public static ArrayList<Integer> union(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        ArrayList<Integer> result = new ArrayList<>(list1);
        result.addAll(list2);
        return result;
    }
}
