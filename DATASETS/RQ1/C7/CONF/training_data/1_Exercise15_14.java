



public class PolygonMouseHover{
    static final double WIDTH = 400;
    static final double HEIGHT = 150;
    static double mouseX;
    static double mouseY;

    @Override
    public void start(Stage primaryStage) throws Exception {
        Pane pane = new Pane();
        Polygon polygon = new Polygon(40, 20, 70, 40, 60, 80, 45, 45, 20, 60);
        polygon.setFill(Color.TRANSPARENT);
        polygon.setStroke(Color.BLACK);

        Text message = new Text(polygon.getStrokeWidth() / 2, polygon.getStrokeWidth() / 2, "");
        pane.getChildren().add(polygon);
        pane.getChildren().add(message);
        Scene scene = new Scene(pane, WIDTH, HEIGHT);

        scene.setOnMouseMoved(mouseEvent -> {
            mouseX = mouseEvent.getSceneX();
            mouseY = mouseEvent.getSceneY();
            if (isPointInPolygon(mouseX, mouseY, polygon)) {
                message.setText("Mouse point is inside the polygon");
            } else {
                message.setText("Mouse point is outside the polygon");
            }
            message.setX(mouseX);
            message.setY(mouseY);
        });

        primaryStage.setTitle(getClass().getName());
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private boolean isPointInPolygon(double mouseX, double mouseY, Polygon polygon) {
        return polygon.contains(mouseX, mouseY);
    }

    public static void main(String[] args) {
        launch(args);
    }
}
