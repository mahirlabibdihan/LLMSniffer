




public class nan {
    final static double ROTATE = 90.0;

    @Override
    public void start(Stage primaryStage) {
        GridPane gridPane = new GridPane();
        gridPane.setAlignment(Pos.CENTER);

        Label text1 = new Label("Java");
        text1.setFont(Font.font("Times New Roman", FontWeight.BOLD, FontPosture.ITALIC, 22));
        text1.setTextFill(new Color(Math.random(),Math.random(),Math.random(),Math.random()));
        text1.setRotate(ROTATE);
        gridPane.add(text1, 0, 0);

        Label text2 = new Label("Java");
        text2.setFont(Font.font("Times New Roman", FontWeight.BOLD, FontPosture.ITALIC, 22));
        text2.setTextFill(new Color(Math.random(),Math.random(),Math.random(),Math.random()));
        text2.setRotate(ROTATE);
        gridPane.add(text2, 1, 0);

        Label text3 = new Label("Java");
        text3.setFont(Font.font("Times New Roman", FontWeight.BOLD, FontPosture.ITALIC, 22));
        text3.setTextFill(new Color(Math.random(),Math.random(),Math.random(),Math.random()));
        text3.setRotate(ROTATE);
        gridPane.add(text3, 2, 0);

        Label text4 = new Label("Java");
        text4.setFont(Font.font("Times New Roman", FontWeight.BOLD, FontPosture.ITALIC, 22));
        text4.setTextFill(new Color(Math.random(),Math.random(),Math.random(),Math.random()));
        text4.setRotate(ROTATE);
        gridPane.add(text4, 3, 0);

        Label text5 = new Label("Java");
        text5.setFont(Font.font("Times New Roman", FontWeight.BOLD, FontPosture.ITALIC, 22));
        text5.setTextFill(new Color(Math.random(),Math.random(),Math.random(),Math.random()));
        text5.setRotate(ROTATE);
        gridPane.add(text5, 4, 0);


        Scene scene = new Scene(gridPane, 250, 100);
        primaryStage.setTitle(getClass().getName());
        primaryStage.setScene(scene);
        primaryStage.show();


    }
}