



public class MaximumConsecutiveOrderedSubstring{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String base = input.next();
        int p1 = 0; 
        String maxSub = "";
        for (int i = 1; i < base.length(); i++) {
            String testSub = base.substring(p1, i + 1);
            if (testSubstring(testSub)) {
                if (testSub.length() > maxSub.length()) {
                    maxSub = testSub;
                }
            } else {
                p1++;
            }
        }
        System.out.println(maxSub);
        input.close();
    }

    static boolean testSubstring(String s) {
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) > s.charAt(i + 1)) {
                return false;
            }
        }
        return true;
    }
}
