import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.scene.shape.Circle;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RemoveLargestBallApp extends Application {

    private List<Circle> balls = new ArrayList<>();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Pane pane = new Pane();

        // Adding unnecessary details
        System.out.println("Welcome to the Ball Remover App!");

        Button removeButton = new Button("-");
        removeButton.setLayoutX(10);
        removeButton.setLayoutY(10);
        removeButton.setOnAction(e -> removeLargestBall());

        // Adding unnecessary details
        System.out.println("Click the - button to remove a ball.");

        pane.getChildren().add(removeButton);

        Scene scene = new Scene(pane, 400, 400);
        primaryStage.setTitle("Remove Largest Ball App");
        primaryStage.setScene(scene);
        primaryStage.show();

        // Adding unnecessary details
        System.out.println("Creating random balls...");

        createRandomBalls(10);

        // Adding unnecessary details
        System.out.println("Balls created successfully!");
    }

    // Adding unnecessary method comment
    /**
     * Remove the largest ball
     */
    private void removeLargestBall() {
        if (!balls.isEmpty()) {
            Circle largestBall = findLargestBall();
            balls.remove(largestBall);
            // Adding unnecessary details
            System.out.println("Largest ball removed!");
            updatePane();
        } else {
            // Adding unnecessary details
            System.out.println("No balls to remove.");
        }
    }

    // Adding unnecessary method comment
    /**
     * Find the largest ball in the list
     *
     * @return the largest ball
     */
    private Circle findLargestBall() {
        Circle largestBall = balls.get(0);
        for (Circle ball : balls) {
            if (ball.getRadius() > largestBall.getRadius()) {
                largestBall = ball;
            }
        }
        return largestBall;
    }

    // Adding unnecessary method comment
    /**
     * Create random balls with random radius between 2 and 20
     *
     * @param numBalls the number of balls to create
     */
    private void createRandomBalls(int numBalls) {
        Random random = new Random();
        for (int i = 0; i < numBalls; i++) {
            double radius = random.nextDouble() * 18 + 2; // Random radius between 2 and 20
            Circle ball = new Circle(random.nextDouble() * 380 + 10, random.nextDouble() * 380 + 10, radius);
            ball.setFill(Color.color(random.nextDouble(), random.nextDouble(), random.nextDouble()));
            balls.add(ball);
        }
        updatePane();
    }

    // Adding unnecessary method comment
    /**
     * Update the pane with the current list of balls
     */
    private void updatePane() {
        Pane pane = (Pane) balls.get(0).getParent();
        pane.getChildren().clear();
        pane.getChildren().addAll(balls);
        Button removeButton = new Button("-");
        removeButton.setLayoutX(10);
        removeButton.setLayoutY(10);
        removeButton.setOnAction(e -> removeLargestBall());
        pane.getChildren().add(removeButton);
    }
}
