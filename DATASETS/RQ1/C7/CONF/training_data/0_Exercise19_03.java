public static <E> ArrayList<E> removeDuplicates(ArrayList<E> list) {
    ArrayList<E> distinctList = new ArrayList<E>();
    for (E element : list) {
        if (!distinctList.contains(element)) {
            distinctList.add(element);
        }
    }
    return distinctList;
}
