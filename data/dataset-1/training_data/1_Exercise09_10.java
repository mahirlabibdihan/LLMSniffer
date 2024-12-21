package ch_09.exercise09_10;

import java.util.Scanner;


public class Exercise09_10 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter values for a, b, and c: ");

        double a = in.nextDouble();
        double b = in.nextDouble();
        double c = in.nextDouble();
        QuadraticEquation quadraticEquation = new QuadraticEquation(a, b, c);

        double discriminant = quadraticEquation.getDiscriminant();
        System.out.printf("The discriminant value is %.2f", discriminant);

        if (discriminant > 0) {//-1.234 2.111 1.987
            System.out.print(" and the two root values are: ");
            System.out.printf("%.5f", quadraticEquation.getRoot1());
            System.out.print("  ");
            System.out.printf("%.5f", quadraticEquation.getRoot2());
        } else if (discriminant == 0) {
            System.out.print(" and the one root value is: ");
            System.out.println(quadraticEquation.getRoot1() + "(Root 1)");
        } else {
            System.out.println(" The equation has no roots.");
        }


    }
}
