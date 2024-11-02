public static int solveQuadratic(double[] eqn, double[] roots) {
    double a = eqn[0];
    double b = eqn[1];
    double c = eqn[2];
    double discriminant = b * b - 4 * a * c;
    if (discriminant < 0) {
        return 0; 
    } else if (discriminant == 0) {
        roots[0] = -b / (2 * a);
        return 1; 
    } else {
        roots[0] = (-b + Math.sqrt(discriminant)) / (2 * a);
        roots[1] = (-b - Math.sqrt(discriminant)) / (2 * a);
        return 2; 
    }
}
 import java.util.Scanner;

public class QuadraticEquationSolver {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] eqn = new double[3];
        double[] roots = new double[2];
        System.out.print("Enter a, b, c: ");
        eqn[0] = input.nextDouble();
        eqn[1] = input.nextDouble();
        eqn[2] = input.nextDouble();
        int numRoots = solveQuadratic(eqn, roots);
        if (numRoots == 0) {
            System.out.println("The equation has no real roots.");
        } else if (numRoots == 1) {
            System.out.println("The equation has one real root: " + roots[0]);
        } else {
            System.out.println("The equation has two real roots: " + roots[0] + " and " + roots[1]);
        }
    }
}