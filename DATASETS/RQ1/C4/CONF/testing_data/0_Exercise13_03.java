import java.util.ArrayList;
import java.util.Collections;

public class SortArrayList {
    public static void main(String[] args) {
        ArrayList<Number> numbers = new ArrayList<>();
        numbers.add(3.14);
        numbers.add(2);
        numbers.add(-1.5);
        numbers.add(10);
        System.out.println("Original list: " + numbers);
        sort(numbers);
        System.out.println("Sorted list: " + numbers);
    }
    
    public static void sort(ArrayList<Number> list) {
        Collections.sort(list);
    }
}