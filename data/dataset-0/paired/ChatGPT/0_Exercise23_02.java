public static <E extends Comparable<E>> void mergeSort(E[] list) {
    if (list.length > 1) {
        // Split the array into two sub-arrays
        int mid = list.length / 2;
        E[] left = Arrays.copyOfRange(list, 0, mid);
        E[] right = Arrays.copyOfRange(list, mid, list.length);

        // Recursively sort the sub-arrays
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted sub-arrays
        merge(left, right, list);
    }
}

private static <E extends Comparable<E>> void merge(E[] left, E[] right, E[] list) {
    int i = 0; // Index of left sub-array
    int j = 0; // Index of right sub-array
    int k = 0; // Index of merged array

    while (i < left.length && j < right.length) {
        if (left[i].compareTo(right[j]) <= 0) {
            list[k++] = left[i++];
        } else {
            list[k++] = right[j++];
        }
    }

    // Copy remaining elements from left sub-array (if any)
    while (i < left.length) {
        list[k++] = left[i++];
    }

    // Copy remaining elements from right sub-array (if any)
    while (j < right.length) {
        list[k++] = right[j++];
    }
}

public static <E> void mergeSort(E[] list, Comparator<? super E> comparator) {
    if (list.length > 1) {
        // Split the array into two sub-arrays
        int mid = list.length / 2;
        E[] left = Arrays.copyOfRange(list, 0, mid);
        E[] right = Arrays.copyOfRange(list, mid, list.length);

        // Recursively sort the sub-arrays
        mergeSort(left, comparator);
        mergeSort(right, comparator);

        // Merge the sorted sub-arrays
        merge(left, right, list, comparator);
    }
}

private static <E> void merge(E[] left, E[] right, E[] list, Comparator<? super E> comparator) {
    int i = 0; // Index of left sub-array
    int j = 0; // Index of right sub-array
    int k = 0; // Index of merged array

    while (i < left.length && j < right.length) {
        if (comparator.compare(left[i], right[j]) <= 0) {
            list[k++] = left[i++];
        } else {
            list[k++] = right[j++];
        }
    }

    // Copy remaining elements from left sub-array (if any)
    while (i < left.length) {
        list[k++] = left[i++];
    }

    // Copy remaining elements from right sub-array (if any)
    while (j < right.length) {
        list[k++] = right[j++];
    }
}
