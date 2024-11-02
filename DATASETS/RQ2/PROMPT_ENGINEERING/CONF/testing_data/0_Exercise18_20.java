/**
 * Welcome to the CircleDisplay program!
 * This program displays circles centered in the pane with gaps between them.
 * Author: [Your Name]
 */

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class CircleDisplay extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Create the CirclePane
        CirclePane circlePane = new CirclePane();

        // Create a scene and set it in the stage
        Scene scene = new Scene(circlePane, 400, 400);
        primaryStage.setTitle("Circle Display");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // CirclePane class
    private static class CirclePane extends Pane {

        public CirclePane() {
            setPrefSize(400, 400);
            displayCircles();
        }

        private void displayCircles() {
            // Constants
            final int CIRCLE_GAP = 10;
            final int BORDER_GAP = 10;

            // Calculate the maximum number of circles that fit in the pane
            int maxCircles = Math.min((int) ((getWidth() - 2 * BORDER_GAP) / (CIRCLE_GAP * 2)),
                    (int) ((getHeight() - 2 * BORDER_GAP) / (CIRCLE_GAP * 2)));

            // Display circles
            for (int i = 0; i < maxCircles; i++) {
                double radius = CIRCLE_GAP * (i + 1);
                double centerX = getWidth() / 2;
                double centerY = getHeight() / 2;

                // Create a circle
                Circle circle = new Circle(centerX, centerY, radius);
                circle.setFill(Color.TRANSPARENT);
                circle.setStroke(Color.BLACK);

                // Add the circle to the pane
                getChildren().add(circle);
            }
        }
    }
}