import java.util.Scanner;

public class IntersectingPointCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the endpoints of the first line segment (x1, y1) and (x2, y2):");
        double x1 = input.nextDouble();
        double y1 = input.nextDouble();
        double x2 = input.nextDouble();
        double y2 = input.nextDouble();

        System.out.println("Enter the endpoints of the second line segment (x3, y3) and (x4, y4):");
        double x3 = input.nextDouble();
        double y3 = input.nextDouble();
        double x4 = input.nextDouble();
        double y4 = input.nextDouble();

        // Calculate the slopes and intercepts of the lines
        double slope1 = (y2 - y1) / (x2 - x1);
        double slope2 = (y4 - y3) / (x4 - x3);
        double intercept1 = y1 - slope1 * x1;
        double intercept2 = y3 - slope2 * x3;

        // Check if the lines are parallel
        if (slope1 == slope2) {
            System.out.println("The lines are parallel. They do not intersect.");
        } else {
            // Calculate the intersecting point
            double intersectX = (intercept2 - intercept1) / (slope1 - slope2);
            double intersectY = slope1 * intersectX + intercept1;

            System.out.println("The intersecting point is at (" + intersectX + ", " + intersectY + ")");
        }

        input.close();
    }
}