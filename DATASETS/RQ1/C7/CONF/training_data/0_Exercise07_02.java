
public class ReverseNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int[] numbers = new int[10];

        System.out.println("Enter ten integers:");

        
        for (int i = 0; i < 10; i++) {
            numbers[i] = input.nextInt();
        }

        
        System.out.print("The numbers in reverse order are: ");
        for (int i = 9; i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
    }
}
