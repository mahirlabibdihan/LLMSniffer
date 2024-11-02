

import java.util.ArrayList;
import java.util.Arrays;


public class ArrayShuffler{
    public static void main(String[] args) {
        
        ArrayList<Double> doubleList =
                new ArrayList<>(Arrays.asList(1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8));
        
        ArrayList<Integer> integerList =
                new ArrayList<>(Arrays.asList(11, 22, 33, 44, 55, 66, 77, 88));

        System.out.println("Before shuffling the ArrayList of Doubles is: " + doubleList);
        shuffle(doubleList);
        System.out.println("After performing Generic shuffle: " + doubleList);

        System.out.println("Before shuffling the ArrayList of Integers is: " + integerList);
        shuffle(integerList);
        System.out.println("After performing Generic shuffle: " + integerList);
    }

    public static <E> void shuffle(ArrayList<E> list) {
        for (int i = 0; i < list.size() && !list.isEmpty(); i++) { 
            int randomIdx = (int) (Math.random() * (list.size() - 1));
            
            E value = list.get(i); 
            E temp = list.get(randomIdx); 
            list.set(randomIdx, value); 
            list.set(i, temp); 
        }
    }
}
