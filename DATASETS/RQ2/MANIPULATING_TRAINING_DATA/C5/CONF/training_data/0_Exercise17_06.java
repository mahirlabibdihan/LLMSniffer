import java.io.Serializable;public class Loan implements Serializable {  private static final long serialVersionUID = 1L;  private double annualInterestRate;  private int numberOfYears;  private double loanAmount;    public Loan(double annualInterestRate, int numberOfYears, double loanAmount) {    this.annualInterestRate = annualInterestRate;    this.numberOfYears = numberOfYears;    this.loanAmount = loanAmount;  }    public double getAnnualInterestRate() {    return annualInterestRate;  }    public void setAnnualInterestRate(double annualInterestRate) {    this.annualInterestRate = annualInterestRate;  }    public int getNumberOfYears() {    return numberOfYears;  }    public void setNumberOfYears(int numberOfYears) {    this.numberOfYears = numberOfYears;  }    public double getLoanAmount() {    return loanAmount;  }    public void setLoanAmount(double loanAmount) {    this.loanAmount = loanAmount;  }    public double getMonthlyPayment() {    