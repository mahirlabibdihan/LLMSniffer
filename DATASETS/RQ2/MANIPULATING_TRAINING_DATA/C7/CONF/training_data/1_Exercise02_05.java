



public class CalculateTips {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Welcome to the super excellent java master gratuity and bill calculator! :) ");
        System.out.println("Enter your subtotal and the gratuity rate: ");

        double subTotal = input.nextDouble();
        double percentGratuity = input.nextDouble();

        double gratuity = subTotal * (percentGratuity / 100);

        double total = subTotal + gratuity;

        System.out.print("The gratuity is: $");
        System.out.printf("%.2f", gratuity);
        System.out.print(" and the total including gratuity is: $" + total);


    }

}
