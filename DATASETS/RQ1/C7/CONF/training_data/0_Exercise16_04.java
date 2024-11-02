
public class MilesKilometersConverter extends Application {

    private TextField milesField;
    private TextField kilometersField;

    @Override
    public void start(Stage primaryStage) {
        
        milesField = new TextField();
        kilometersField = new TextField();

        
        milesField.setOnAction(e -> convertMilesToKilometers());
        kilometersField.setOnAction(e -> convertKilometersToMiles());

        
        Label milesLabel = new Label("Miles:");
        Label kilometersLabel = new Label("Kilometers:");

        
        HBox inputBox = new HBox(10, milesLabel, milesField, kilometersLabel, kilometersField);
        inputBox.setAlignment(Pos.CENTER);

        
        VBox root = new VBox(20, inputBox);
        root.setAlignment(Pos.CENTER);

        
        Scene scene = new Scene(root, 400, 200);
        primaryStage.setTitle("Miles/Kilometers Converter");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void convertMilesToKilometers() {
        try {
            
            double miles = Double.parseDouble(milesField.getText());
            double kilometers = miles * 1.609344;

            
            kilometersField.setText(String.format("%.2f", kilometers));
        } catch (NumberFormatException e) {
            
            kilometersField.setText("Invalid input");
        }
    }

    private void convertKilometersToMiles() {
        try {
            
            double kilometers = Double.parseDouble(kilometersField.getText());
            double miles = kilometers / 1.609344;

            
            milesField.setText(String.format("%.2f", miles));
        } catch (NumberFormatException e) {
            
            milesField.setText("Invalid input");
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
