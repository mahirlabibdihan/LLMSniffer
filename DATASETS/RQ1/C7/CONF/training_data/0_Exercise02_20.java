
public class NextMonthInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Enter the balance: ");
        double balance = scanner.nextDouble();
        System.out.print("Enter the annual interest rate: ");
        double annualInterestRate = scanner.nextDouble();

        
        double monthlyInterestRate = annualInterestRate / 1200.0;
        double interest = balance * monthlyInterestRate;

        
        System.out.printf("The interest for the next month is $%.2f", interest);
    }
}
