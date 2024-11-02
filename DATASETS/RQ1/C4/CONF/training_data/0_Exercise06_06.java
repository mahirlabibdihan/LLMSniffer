public class DisplayPattern {
    
    public static void main(String[] args) {
        displayPattern(3); 
    }
    
    public static void displayPattern(int n) {
        for (int i = 1; i <= n; i++) {
            
            for (int j = n - i; j >= 1; j--) {
                System.out.print("  ");
            }
            
            for (int j = i; j >= 1; j--) {
                System.out.print(j + " ");
            }
            System.out.println(); 
        }
    }
    
}