
public class Point implements Comparable<Point> {
    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    @Override
    public int compareTo(Point other) {
        int xComparison = Double.compare(x, other.x);
        if (xComparison != 0) {
            return xComparison;
        }
        return Double.compare(y, other.y);
    }

    public double distanceTo(Point other) {
        double dx = x - other.x;
        double dy = y - other.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
}

class Pair {
    private Point p1;
    private Point p2;

    public Pair(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public Point getP1() {
        return p1;
    }

    public Point getP2() {
        return p2;
    }

    public double getDistance() {
        return p1.distanceTo(p2);
    }
}

class CompareY implements java.util.Comparator<Point> {
    public int compare(Point p1, Point p2) {
        return Double.compare(p1.getY(), p2.getY());
    }
}

public class ClosestPair {
    public static Pair getClosestPair(double[][] points) {
        Point[] pointObjs = new Point[points.length];
        for (int i = 0; i < points.length; i++) {
            pointObjs[i] = new Point(points[i][0], points[i][1]);
        }
        Arrays.sort(pointObjs);

        return getClosestPair(pointObjs, 0, pointObjs.length - 1);
    }

    private static Pair getClosestPair(Point[] points, int low, int high) {
        if (low >= high) {
            return null;
        } else if (low + 1 == high) {
            return new Pair(points[low], points[high]);
        }

        int mid = (low + high) / 2;
        Pair pair1 = getClosestPair(points, low, mid);
        Pair pair2 = getClosestPair(points, mid + 1, high);
        Pair minPair = getMinPair(pair1, pair2);

        double minDistance = minPair.getDistance();
        Point[] strip = getStrip(points, low, high, points[mid].getX(), minDistance);
        Pair stripPair = getClosestStripPair(strip, minDistance);

        return getMinPair(minPair, stripPair);
    }

    private static Pair getMinPair(Pair pair1, Pair pair2) {
        if (pair1 == null) {
            return pair2;
        } else if (pair2 == null) {
            return pair1;
        }
        return pair1.getDistance() < pair2.getDistance() ? pair1 : pair2;
    }

    private static Point[] getStrip(Point[] points, int low, int high, double midX, double minDistance) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            if (Math.abs(points[i].getX() - midX) < minDistance) {
                count++;
            }
        }
        Point[] strip = new Point
