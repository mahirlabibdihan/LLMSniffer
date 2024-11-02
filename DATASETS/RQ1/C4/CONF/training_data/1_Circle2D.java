




public class Circle2D {
    
    private double x;
    private double y;
    
    private double radius;

    
    public Circle2D() {
        x = 0;
        y = 0;
        radius = 1;
    }

    
    public Circle2D(double x, double y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    
    public double getArea() {
        return Math.PI * Math.pow(radius, 2);
    }

    
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    
    public boolean contains(double x, double y) {
        double distanceFromCenterPoint = Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
        return distanceFromCenterPoint < radius;

    }

    
    public boolean contains(Circle2D circle2D) {
        double distFromCenterPoints =
                Math.sqrt(Math.pow(circle2D.getX() - this.x, 2) + Math.pow(circle2D.getY() - this.y,
                        2));
        return this.radius > (distFromCenterPoints + circle2D.getRadius());
    }

    
    public boolean overlaps(Circle2D circle2D) {
        double distCentPoints = Math.sqrt(Math.pow(circle2D.getX() - this.x, 2) + Math.pow(circle2D.getY() - this.y, 2));
        double rSqSum = Math.pow(circle2D.getRadius() + this.radius, 2);
        return distCentPoints < rSqSum;
    }

    
    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }


}
