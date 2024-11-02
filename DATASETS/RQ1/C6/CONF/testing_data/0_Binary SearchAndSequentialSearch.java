public class SearchComparison {

    
    public static int sequentialSearch(int[] arr, int x) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }

    
    public static int binarySearch(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return -1;
    }

    
    public static void main(String[] args) {
        int[] arr = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 };
        int x = 12;

        long start = System.nanoTime();
        int sequentialIndex = sequentialSearch(arr, x);
        long end = System.nanoTime();
        System.out.println("Sequential Search:");
        if (sequentialIndex != -1) {
            System.out.println("Element found at index " + sequentialIndex);
        } else {
            System.out.println("Element not found");
        }
        System.out.println("Time taken: " + (end - start) + " ns");

        start = System.nanoTime();
        int binaryIndex = binarySearch(arr, x);
        end = System.nanoTime();
        System.out.println("Binary Search:");
        if (binaryIndex != -1) {
            System.out.println("Element found at index " + binaryIndex);
        } else {
            System.out.println("Element not found");
        }
        System.out.println("Time taken: " + (end - start) + " ns");
    }
}

