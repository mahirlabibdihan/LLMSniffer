import java.util.Scanner;

public class SubstringMatcher {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a string s1: ");
        String s1 = scanner.nextLine();
        
        System.out.print("Enter a string s2: ");
        String s2 = scanner.nextLine();
        
        int index = findSubstring(s1, s2);
        
        if (index != -1) {
            System.out.println("Matched at index " + index);
        } else {
            System.out.println("Substring not found.");
        }
        
        scanner.close();
    }

    public static int findSubstring(String s1, String s2) {
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        
        for (int i = 0; i <= arr1.length - arr2.length; i++) {
            boolean matched = true;
            
            for (int j = 0; j < arr2.length; j++) {
                if (arr1[i + j] != arr2[j]) {
                    matched = false;
                    break;
                }
            }
            
            if (matched) {
                return i;
            }
        }
        
        return -1;
    }
}