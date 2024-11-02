

import java.util.Arrays;


public class nan {
    public static void main(String[] args) {
        
        Double[] values = new Double[]{4400.1, 1203.3, 3100.0, 18700.8, 4100.6};
        System.out.println("Generic Max method returned: " + max(values) + ". When passed this Array of values: " +
                " \n" + Arrays.toString(values));
    }

    public static <E extends Comparable<E>> E max(E[] list) {
        E maxValue = list[0];
        for (int i = 1; i < list.length; i++) {
            if (list[i].compareTo(maxValue) > 0) {
                maxValue = list[i];
            }
        }
        return maxValue;
    }

}
