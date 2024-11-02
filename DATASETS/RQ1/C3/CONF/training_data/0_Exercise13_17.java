import java.util.Scanner;

public class Complex implements Cloneable {
    private double a;
    private double b;

    public Complex() {
        this(0, 0);
    }

    public Complex(double a) {
        this(a, 0);
    }

    public Complex(double a, double b) {
        this.a = a;
        this.b = b;
    }

    public double getRealPart() {
        return a;
    }

    public double getImaginaryPart() {
        return b;
    }

    public Complex add(Complex secondComplex) {
        return new Complex(a + secondComplex.getRealPart(), b + secondComplex.getImaginaryPart());
    }

    public Complex subtract(Complex secondComplex) {
        return new Complex(a - secondComplex.getRealPart(), b - secondComplex.getImaginaryPart());
    }

    public Complex multiply(Complex secondComplex) {
        double newA = a * secondComplex.getRealPart() - b * secondComplex.getImaginaryPart();
        double newB = b * secondComplex.getRealPart() + a * secondComplex.getImaginaryPart();
        return new Complex(newA, newB);
    }

    public Complex divide(Complex secondComplex) {
        double c = secondComplex.getRealPart();
        double d = secondComplex.getImaginaryPart();
        double newA = (a * c + b * d) / (c * c + d * d);
        double newB = (b * c - a * d) / (c * c + d * d);
        return new Complex(newA, newB);
    }

    public double abs() {
        return Math.sqrt(a * a + b * b);
    }

    @Override
    public String toString() {
        if (b == 0) {
            return a + "";
        } else {
            return "(" + a + " + " + b + "i)";
        }
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first complex number: ");
        double a1 = input.nextDouble();
        double b1 = input.nextDouble();
        System.out.print("Enter the second complex number: ");
        double a2 = input.nextDouble();
        double b2 = input.nextDouble();
        Complex c1 = new Complex(a1, b1);
        Complex c2 = new Complex(a2, b2);
        System.out.println(c1 + " + " + c2 + " = " + c1.add(c2));
        System.out.println(c1 + " - " + c2 + " = " + c1.subtract(c2));
        System.out.println(c1 + " * " + c2 + " = " + c1.multiply(c2));
        System.out.println(c1 + " / " + c2 + " = " + c1.divide(c2));
        System.out.println("|" + c1 + "| = " + c1.abs());
    }
}