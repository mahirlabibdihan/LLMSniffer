



public class nan{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a sequence of numbers ending with a 0: ");

        ArrayList<Integer> list = new ArrayList<>();
        Integer integer;
        while ((integer = in.nextInt()) != 0) {
            list.add(integer);
        }

        System.out.println("The largest number is " + max(list));
        in.close();
    }

    public static Integer max(ArrayList<Integer> list) {
        if (list == null || list.isEmpty()) {
            return null;
        }
        Integer max = list.get(0);
        for (Integer integer : list) {
            max = Math.max(max, integer);
        }
        return max;
    }

}
