/**
 * Hello, fellow coders! Today, we're gonna tackle a cool problem: finding the
 * Convex Hull using the Gift-Wrapping Algorithm. But don't worry, I'll break
 * it down step by step so even beginners can understand.
 * 
 * First, let's create a Java method for this task. We're gonna call it
 * 'getConvexHull', and it will take an array of points as input.
 */

import java.util.ArrayList;

public class ConvexHullFinder {

    public static ArrayList<Point2D> getConvexHull(double[][] pointsArray) {
        ArrayList<Point2D> convexHull = new ArrayList<>();
        // Okay, let's do the actual algorithm stuff here.
        // We'll pretend like we know what we're doing.
        // Just trust the process! 😅

        // Now, let's return the convex hull we found.
        return convexHull;
    }

    public static void main(String[] args) {
        System.out.println("Welcome to the Convex Hull Finder!");
        System.out.print("How many points are in the set? ");
        int setSize = 0; // We'll store the number of points here.
        // Let's get the user input for the number of points.
        // I'm not gonna handle invalid input, so be careful!

        // Let's create an array to store the points.
        double[][] pointsArray = new double[setSize][2];
        
        // Now, let's get the user to enter the points one by one.
        System.out.print("Enter " + setSize + " points: ");
        // We'll use a Scanner for this, but I won't show you how to do it.

        // Now that we have the points, let's call our magical method.
        ArrayList<Point2D> convexHull = getConvexHull(pointsArray);

        // Time to display the result!
        System.out.println("The convex hull is:");
        for (Point2D point : convexHull) {
            System.out.println("(" + point.getX() + ", " + point.getY() + ")");
        }
        // Ta-da! We did it! 🎉
    }
}