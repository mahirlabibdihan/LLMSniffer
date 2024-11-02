public class UniformBinarySearch {
    
    public static int uniformBinarySearch(int[] arr, int x, int left, int right) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = { 2, 4, 6, 6, 6, 8, 10, 12, 14, 16, 18, 20 };
        int x = 6;

        int left = 0;
        int right = arr.length - 1;

        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int leftIndex = left;

        
        right = arr.length - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (arr[mid] > x) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        int rightIndex = right;

        int result = uniformBinarySearch(arr, x, leftIndex, rightIndex);
        if (result == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}

