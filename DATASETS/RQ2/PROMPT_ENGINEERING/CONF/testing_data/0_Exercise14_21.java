import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import java.util.Random;

public class TwoCirclesDistance extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Pane pane = new Pane();

        // Create two circles with random positions
        Circle circle1 = new Circle();
        circle1.setCenterX(generateRandomCoordinate());
        circle1.setCenterY(generateRandomCoordinate());
        circle1.setRadius(15);
        circle1.setFill(Color.RED);

        Circle circle2 = new Circle();
        circle2.setCenterX(generateRandomCoordinate());
        circle2.setCenterY(generateRandomCoordinate());
        circle2.setRadius(15);
        circle2.setFill(Color.BLUE);

        // Calculate the distance between the centers
        double distance = calculateDistance(circle1, circle2);

        // Create a line connecting the centers
        Line line = new Line(circle1.getCenterX(), circle1.getCenterY(), circle2.getCenterX(), circle2.getCenterY());
        line.setStroke(Color.GREEN);

        // Display the distance as text
        Text distanceText = new Text((circle1.getCenterX() + circle2.getCenterX()) / 2,
                (circle1.getCenterY() + circle2.getCenterY()) / 2, String.format("%.2f", distance));

        // Add shapes to the pane
        pane.getChildren().addAll(circle1, circle2, line, distanceText);

        Scene scene = new Scene(pane, 400, 400);
        primaryStage.setTitle("Two Circles and Distance");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private double generateRandomCoordinate() {
        Random random = new Random();
        return random.nextDouble() * 350 + 25; // Ensure circles are within the visible area
    }

    private double calculateDistance(Circle circle1, Circle circle2) {
        double x1 = circle1.getCenterX();
        double y1 = circle1.getCenterY();
        double x2 = circle2.getCenterX();
        double y2 = circle2.getCenterY();

        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
}
