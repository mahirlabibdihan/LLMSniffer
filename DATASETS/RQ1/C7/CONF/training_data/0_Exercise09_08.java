public class FanTest {
    public static void main(String[] args) {
        Fan fan1 = new Fan();
        fan1.setSpeed(Fan.MAX_SPEED);
        fan1.setRadius(10);
        fan1.setColor("yellow");
        fan1.turnOn();

        Fan fan2 = new Fan();
        fan2.setSpeed(Fan.MEDIUM_SPEED);
        fan2.setRadius(5);
        fan2.setColor("blue");
        fan2.turnOff();

        System.out.println("Fan 1: " + fan1.toString());
        System.out.println("Fan 2: " + fan2.toString());
    }
}
