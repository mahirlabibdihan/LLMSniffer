public class SalesCommission {
    public static void main(String[] args) {
        double baseSalary = 5000.0;
        double targetIncome = 30000.0;
        double commissionRate1 = 0.08;
        double commissionRate2 = 0.10;
        double commissionRate3 = 0.12;

        double lowSales = 0.0;
        double highSales = 100000.0;
        double middleSales = (lowSales + highSales) / 2;

        while (highSales - lowSales > 0.01) {
            double commission = calculateCommission(baseSalary, middleSales, commissionRate1, commissionRate2, commissionRate3);
            if (commission < targetIncome) {
                lowSales = middleSales + 0.01;
            } else {
                highSales = middleSales - 0.01;
            }
            middleSales = (lowSales + highSales) / 2;
        }

        System.out.printf("Minimum sales required to earn $30,000: $%.2f", middleSales);
    }

    public static double calculateCommission(double baseSalary, double salesAmount, double commissionRate1, double commissionRate2, double commissionRate3) {
        double commission = 0.0;

        if (salesAmount <= 5000.0) {
            commission = salesAmount * commissionRate1;
        } else if (salesAmount <= 10000.0) {
            commission = 5000.0 * commissionRate1 + (salesAmount - 5000.0) * commissionRate2;
        } else {
            commission = 5000.0 * commissionRate1 + 5000.0 * commissionRate2 + (salesAmount - 10000.0) * commissionRate3;
        }

        return baseSalary + commission;
    }
}
