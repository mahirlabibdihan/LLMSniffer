
public class FutureInvestmentValue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        
        System.out.print("Enter the investment amount: $");
        double investmentAmount = scanner.nextDouble();
        System.out.print("Enter the annual interest rate (as a percentage): ");
        double annualInterestRate = scanner.nextDouble();
        System.out.print("Enter the number of years: ");
        int numberOfYears = scanner.nextInt();
        
        
        double monthlyInterestRate = annualInterestRate / 1200.0; 
        double futureInvestmentValue = investmentAmount * Math.pow(1 + monthlyInterestRate, numberOfYears * 12);
        
        
        System.out.printf("The future investment value is: $%.2f", futureInvestmentValue);
    }
}
