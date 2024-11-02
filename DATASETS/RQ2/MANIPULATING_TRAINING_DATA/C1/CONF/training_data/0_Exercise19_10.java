public static <E extends Comparable<E>> E max(ArrayList<E> list) {
    if (list == null || list.isEmpty()) {
        return null;
    }

    E maxElement = list.get(0);

    for (int i = 1; i < list.size(); i++) {
        E currentElement = list.get(i);
        if (currentElement.compareTo(maxElement) > 0) {
            maxElement = currentElement;
        }
    }

    return maxElement;
}