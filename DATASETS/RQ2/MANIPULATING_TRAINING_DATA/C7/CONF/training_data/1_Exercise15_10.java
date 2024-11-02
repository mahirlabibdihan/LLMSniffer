



public class StringPaneDisplay {
    double x = 300;
    double y = 200;
    double moveText = 150;
    String nuString = "";
    boolean alternate = true;

    @Override
    public void start(Stage primaryStage) throws Exception {
        Pane pane = new Pane();
        Canvas canvas = new Canvas(600, 400);
        GraphicsContext gc = canvas.getGraphicsContext2D();
        gc.moveTo(x, y);
        gc.setFill(Color.BLACK);
        pane.getChildren().add(canvas);
        Scene scene = new Scene(pane, 600, 400);

        scene.setOnKeyPressed(event -> {
            if (event.getCode() == KeyCode.ENTER) {
                if (alternate) {
                    alternate = false;
                    gc.strokeText(nuString, (x + Math.random() * moveText), (y + Math.random() * moveText));
                } else {
                    gc.strokeText(nuString, (x + Math.random() * -moveText), (y + Math.random() * -moveText));
                }
                nuString = "";
            } else {
                nuString += event.getText();
            }
        });

        primaryStage.setTitle(getClass().getName());
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
