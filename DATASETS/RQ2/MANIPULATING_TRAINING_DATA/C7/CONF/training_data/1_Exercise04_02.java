



public class GreatCircleDistance {
    public static void main(String[] args) {

        double xOne, xTwo, yOne, yTwo, distance;

        final double radius = 6371.01;

        Scanner input = new Scanner(System.in);

        System.out.println("Enter point 1 (latitude and longitude) in degrees: ");

        xOne = input.nextDouble();
        yOne = input.nextDouble();

        xOne = Math.toRadians(xOne);
        yOne = Math.toRadians(yOne);

        System.out.println("Enter point 2 (latitude and longitude) in degrees: ");

        xTwo = input.nextDouble();
        yTwo = input.nextDouble();

        xTwo = Math.toRadians(xTwo);
        yTwo = Math.toRadians(yTwo);


        distance = radius * (Math.acos((Math.sin(xOne) * Math.sin(xTwo)) +
                (Math.cos(xOne) * Math.cos(xTwo) * Math.cos(yOne - yTwo))));

        System.out.println("The distance between the two points is: " + distance
                + " km");


    }

}
