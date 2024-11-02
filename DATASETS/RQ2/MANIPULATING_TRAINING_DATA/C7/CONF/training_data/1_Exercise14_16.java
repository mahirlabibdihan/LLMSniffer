



public class GridDisplay {
    private static final double WIDTH = 200;
    private static final double HEIGHT = 200;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Pane pane = new Pane();

        Line line1 = new Line(0, 0, 0, 0);
        line1.startYProperty().bind(pane.heightProperty().divide(3));
        line1.endXProperty().bind(pane.widthProperty());
        line1.endYProperty().bind(pane.heightProperty().divide(3));
        line1.setStroke(Color.BLUE);

        Line line2 = new Line(0, 0, 0, 0);
        line2.startYProperty().bind(pane.heightProperty().multiply(2).divide(3));
        line2.endXProperty().bind(pane.widthProperty());
        line2.endYProperty().bind(pane.heightProperty().multiply(2).divide(3));
        line2.setStroke(Color.BLUE);

        Line line3 = new Line(0, 0, 0, 0);
        line3.startXProperty().bind(pane.widthProperty().divide(3));
        line3.endXProperty().bind(pane.widthProperty().divide(3));
        line3.endYProperty().bind(pane.heightProperty());
        line3.setStroke(Color.RED);

        Line line4 = new Line(0, 0, 0, 0);
        line4.startXProperty().bind(pane.widthProperty().multiply(2).divide(3));
        line4.endXProperty().bind(pane.widthProperty().multiply(2).divide(3));
        line4.endYProperty().bind(pane.heightProperty());
        line4.setStroke(Color.RED);

        pane.getChildren().addAll(line1, line2, line3, line4);

        Scene scene = new Scene(pane, WIDTH, HEIGHT);
        primaryStage.setScene(scene);
        primaryStage.setTitle(getClass().getName());
        primaryStage.show();
    }

}
