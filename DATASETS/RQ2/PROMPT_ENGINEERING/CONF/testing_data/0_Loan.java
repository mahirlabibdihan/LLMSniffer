public class Loan {

    private double annualInterestRate;
    private int numberOfYears;
    private double loanAmount;
    private java.util.Date loanDate;

    /**
     * Constructs a loan with a specified annual interest rate,
     * number of years, and loan amount.
     */
    public Loan(double annualInterestRate, int numberOfYears, double loanAmount) {
        setAnnualInterestRate(annualInterestRate);
        setNumberOfYears(numberOfYears);
        setLoanAmount(loanAmount);
        this.loanDate = new java.util.Date();
    }

    /**
     * Returns the annual interest rate.
     */
    public double getAnnualInterestRate() {
        return annualInterestRate;
    }

    /**
     * Sets a new annual interest rate.
     */
    public void setAnnualInterestRate(double annualInterestRate) {
        this.annualInterestRate = annualInterestRate;
    }

    /**
     * Returns the number of years.
     */
    public int getNumberOfYears() {
        return numberOfYears;
    }

    /**
     * Sets a new number of years.
     */
    public void setNumberOfYears(int numberOfYears) {
        this.numberOfYears = numberOfYears;
    }

    /**
     * Returns the loan amount.
     */
    public double getLoanAmount() {
        return loanAmount;
    }

    /**
     * Sets a new loan amount.
     */
    public void setLoanAmount(double loanAmount) {
        this.loanAmount = loanAmount;
    }

    /**
     * Finds the monthly payment.
     */
    public double findMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        return (loanAmount * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -numberOfYears * 12));
    }

    /**
     * Finds the total payment.
     */
    public double findTotalPayment() {
        return findMonthlyPayment() * numberOfYears * 12;
    }

    /**
     * Returns the loan date.
     */
    public java.util.Date getLoanDate() {
        return loanDate;
    }
}