public class LineIntersectionTest {
    public static void main(String[] args) {
        
        double x1 = 1.0;
        double y1 = 1.0;
        double x2 = 5.0;
        double y2 = 5.0;

        
        double x3 = 1.0;
        double y3 = 5.0;
        double x4 = 5.0;
        double y4 = 1.0;

        
        double slope1 = (y2 - y1) / (x2 - x1);
        double yIntercept1 = y1 - slope1 * x1;

        double slope2 = (y4 - y3) / (x4 - x3);
        double yIntercept2 = y3 - slope2 * x3;

        
        if (slope1 == slope2) {
            System.out.println("The two lines are parallel and do not intersect.");
        } else {
            
            double xIntersect = (yIntercept2 - yIntercept1) / (slope1 - slope2);
            double yIntersect = slope1 * xIntersect + yIntercept1;

            
            if (xIntersect >= Math.min(x1, x2) && xIntersect <= Math.max(x1, x2) &&
                yIntersect >= Math.min(y1, y2) && yIntersect <= Math.max(y1, y2) &&
                xIntersect >= Math.min(x3, x4) && xIntersect <= Math.max(x3, x4) &&
                yIntersect >= Math.min(y3, y4) && yIntersect <= Math.max(y3, y4)) {
                System.out.println("The two lines intersect at (" + xIntersect + ", " + yIntersect + ").");
            } else {
                System.out.println("The two lines do not intersect.");
            }
        }
    }
}

