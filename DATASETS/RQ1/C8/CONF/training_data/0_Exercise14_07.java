public class RandomMatrix extends Application {  @Override  public void start(Stage primaryStage) {        GridPane gridPane = new GridPane();    gridPane.setAlignment(Pos.CENTER);    gridPane.setHgap(5);    gridPane.setVgap(5);        for (int i = 0; i < 10; i++) {      for (int j = 0; j < 10; j++) {        int num = (int) (Math.random() * 2);        TextField textField = new TextField(String.valueOf(num));        textField.setPrefColumnCount(1);        textField.setAlignment(Pos.CENTER);        gridPane.add(textField, j, i);      }    }        Scene scene = new Scene(gridPane, 300, 300);        primaryStage.setTitle("Random Matrix");    primaryStage.setScene(scene);    primaryStage.show();  }  public static void main(String[] args) {    launch(args);  }}