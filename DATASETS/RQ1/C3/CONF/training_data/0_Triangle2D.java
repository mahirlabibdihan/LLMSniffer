public class Triangle2D {
    private MyPoint p1, p2, p3;

    public Triangle2D() {
        this(new MyPoint(0, 0), new MyPoint(1, 1), new MyPoint(2, 5));
    }

    public Triangle2D(MyPoint p1, MyPoint p2, MyPoint p3) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    public MyPoint getP1() {
        return p1;
    }

    public void setP1(MyPoint p1) {
        this.p1 = p1;
    }

    public MyPoint getP2() {
        return p2;
    }

    public void setP2(MyPoint p2) {
        this.p2 = p2;
    }

    public MyPoint getP3() {
        return p3;
    }

    public void setP3(MyPoint p3) {
        this.p3 = p3;
    }

    public double getArea() {
        double side1 = p1.distance(p2);
        double side2 = p2.distance(p3);
        double side3 = p3.distance(p1);
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    public double getPerimeter() {
        double side1 = p1.distance(p2);
        double side2 = p2.distance(p3);
        double side3 = p3.distance(p1);
        return side1 + side2 + side3;
    }

    public boolean contains(MyPoint p) {
        double area1 = new Triangle2D(p, p1, p2).getArea();
        double area2 = new Triangle2D(p, p2, p3).getArea();
        double area3 = new Triangle2D(p, p3, p1).getArea();
        double totalArea = getArea();
        return area1 + area2 + area3 <= totalArea;
    }

    public boolean contains(Triangle2D t) {
        return contains(t.p1) && contains(t.p2) && contains(t.p3);
    }

    public boolean overlaps(Triangle2D t) {
        return !contains(t) && !t.contains(this) &&
               (segmentsIntersect(p1, p2, t.p1, t.p2) ||
                segmentsIntersect(p1, p2, t.p2, t.p3) ||
                segmentsIntersect(p1, p2, t.p3, t.p1) ||
                segmentsIntersect(p2, p3, t.p1, t.p2) ||
                segmentsIntersect(p2, p3, t.p2, t.p3) ||
                segmentsIntersect(p2, p3, t.p3, t.p1) ||
                segmentsIntersect(p3, p1, t.p1, t.p2) ||
                segmentsIntersect(p3, p1, t.p2, t.p3) ||
                segmentsIntersect(p3, p1, t.p3, t.p1));
    }

    private boolean segmentsIntersect(MyPoint p1, MyPoint p2, MyPoint p3, MyPoint p4) {
        double d1 = orientation(p1, p2, p3);
        double d2 = orientation(p1, p2, p4);
        double d3 = orientation(p3, p4, p1
