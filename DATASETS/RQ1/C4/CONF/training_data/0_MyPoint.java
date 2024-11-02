public class MyPoint {
    private double x;
    private double y;

    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }

    public MyPoint(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double distance(MyPoint point) {
        double xDiff = x - point.x;
        double yDiff = y - point.y;
        return Math.sqrt(xDiff * xDiff + yDiff * yDiff);
    }

    public double distance(double x, double y) {
        return distance(new MyPoint(x, y));
    }
}
