


public class Pair {
    private Point p1;
    private Point p2;

    public Pair(){}

    public Pair(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

   double getDistance() {
        if (p1 == null || p2 == null) throw new IllegalArgumentException("Pair must have 2 non-null points defined....");
        return Math.sqrt(Math.pow((p2.x - p1.x), 2) + Math.pow((p2.y - p1.y), 2));
    }

    public Point getP1() {
        return p1;
    }

    public void setP1(Point p1) {
        this.p1 = p1;
    }

    public Point getP2() {
        return p2;
    }

    public void setP2(Point p2) {
        this.p2 = p2;
    }


    @Override
    public String toString() {
        return "Pair{" +
                "p1=" + p1 +
                ", p2=" + p2 +
                '}';
    }
}
