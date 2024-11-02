import java.util.Scanner;

public class RegularPolygonArea {
    
    public static double area(int n, double side) {
        double numerator = n * side * side;
        double denominator = 4 * Math.tan(Math.PI / n);
        return numerator / denominator;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of sides: ");
        int n = input.nextInt();
        System.out.print("Enter the side: ");
        double side = input.nextDouble();
        double area = area(n, side);
        System.out.println("The area of the polygon is " + area);
    }
}