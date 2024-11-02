import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.stage.Stage;

import java.util.Random;

public class DrawArrowLine extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Pane pane = new Pane();

        // Generate random coordinates for the starting and ending points
        Random random = new Random();
        double startX = random.nextDouble() * 300;
        double startY = random.nextDouble() * 300;
        double endX = random.nextDouble() * 300;
        double endY = random.nextDouble() * 300;

        drawArrowLine(startX, startY, endX, endY, pane);

        Scene scene = new Scene(pane, 300, 300);
        primaryStage.setTitle("Random Arrow Line");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void drawArrowLine(double startX, double startY,
                                     double endX, double endY, Pane pane) {
        Line line = new Line(startX, startY, endX, endY);
        line.setStroke(Color.BLACK);

        // Calculate arrowhead points
        double angle = Math.atan2(endY - startY, endX - startX);
        double arrowLength = 10;
        double arrowWidth = 5;
        double arrowX1 = endX - arrowLength * Math.cos(angle - Math.toRadians(30));
        double arrowY1 = endY - arrowLength * Math.sin(angle - Math.toRadians(30));
        double arrowX2 = endX - arrowLength * Math.cos(angle + Math.toRadians(30));
        double arrowY2 = endY - arrowLength * Math.sin(angle + Math.toRadians(30));

        // Create arrowhead lines
        Line arrowLine1 = new Line(endX, endY, arrowX1, arrowY1);
        Line arrowLine2 = new Line(endX, endY, arrowX2, arrowY2);

        pane.getChildren().addAll(line, arrowLine1, arrowLine2);
    }
}