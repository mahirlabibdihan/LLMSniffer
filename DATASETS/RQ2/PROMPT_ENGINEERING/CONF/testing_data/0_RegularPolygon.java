public class RegularPolygon {
    private int numSides;
    private double sideLength;
    private double xCoordinate;
    private double yCoordinate;

    public RegularPolygon() {
        numSides = 3;
        sideLength = 1.0;
        xCoordinate = 0.0;
        yCoordinate = 0.0;
    }

    public RegularPolygon(int sides, double length) {
        numSides = sides;
        sideLength = length;
        xCoordinate = 0.0;
        yCoordinate = 0.0;
    }

    public RegularPolygon(int sides, double length, double x, double y) {
        numSides = sides;
        sideLength = length;
        xCoordinate = x;
        yCoordinate = y;
    }

    public int getNumSides() {
        return numSides;
    }

    public void setNumSides(int sides) {
        numSides = sides;
    }

    public double getSideLength() {
        return sideLength;
    }

    public void setSideLength(double length) {
        sideLength = length;
    }

    public double getXCoordinate() {
        return xCoordinate;
    }

    public void setXCoordinate(double x) {
        xCoordinate = x;
    }

    public double getYCoordinate() {
        return yCoordinate;
    }

    public void setYCoordinate(double y) {
        yCoordinate = y;
    }

    public double getPerimeter() {
        return numSides * sideLength;
    }

    public double getArea() {
        return (numSides * Math.pow(sideLength, 2)) / (4 * Math.tan(Math.PI / numSides));
    }
}

public class RegularPolygonTest {
    public static void main(String[] args) {
        RegularPolygon polygon1 = new RegularPolygon();
        RegularPolygon polygon2 = new RegularPolygon(6, 4.0);
        RegularPolygon polygon3 = new RegularPolygon(10, 4.0, 5.6, 7.8);

        System.out.println("Polygon 1 - Perimeter: " + polygon1.getPerimeter() + ", Area: " + polygon1.getArea());
        System.out.println("Polygon 2 - Perimeter: " + polygon2.getPerimeter() + ", Area: " + polygon2.getArea());
        System.out.println("Polygon 3 - Perimeter: " + polygon3.getPerimeter() + ", Area: " + polygon3.getArea());
    }
}