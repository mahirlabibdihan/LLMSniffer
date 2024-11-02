
public class LinkedListGUI extends Application {
    private LinkedList<Integer> list = new LinkedList<>();
    private Set<Integer> set = new HashSet<>(); 

    @Override
    public void start(Stage primaryStage) {
        BorderPane pane = new BorderPane();
        pane.setPadding(new Insets(10));

        
        TextArea taList = new TextArea();
        taList.setEditable(false);
        taList.setWrapText(true);
        pane.setCenter(taList);

        
        HBox hbInput = new HBox(10);
        hbInput.setAlignment(Pos.CENTER);
        Label lblNumber = new Label("Number:");
        TextField tfNumber = new TextField();
        tfNumber.setPrefColumnCount(3);
        Button btnAdd = new Button("Add");
        hbInput.getChildren().addAll(lblNumber, tfNumber, btnAdd);
        pane.setBottom(hbInput);

        
        HBox hbButtons = new HBox(10);
        hbButtons.setAlignment(Pos.CENTER);
        Button btnSort = new Button("Sort");
        Button btnShuffle = new Button("Shuffle");
        Button btnReverse = new Button("Reverse");
        hbButtons.getChildren().addAll(btnSort, btnShuffle, btnReverse);
        pane.setTop(hbButtons);

        
        btnAdd.setOnAction(e -> {
            String text = tfNumber.getText().trim();
            if (!text.isEmpty()) {
                try {
                    int number = Integer.parseInt(text);
                    if (set.add(number)) { 
                        list.add(number);
                        displayList(taList);
                    }
                } catch (NumberFormatException ex) {
                    
                }
                tfNumber.clear();
            }
        });

        btnSort.setOnAction(e -> {
            Collections.sort(list);
            displayList(taList);
        });

        btnShuffle.setOnAction(e -> {
            Collections.shuffle(list);
            displayList(taList);
        });

        btnReverse.setOnAction(e -> {
            Collections.reverse(list);
            displayList(taList);
        });

        Scene scene = new Scene(pane);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Linked List GUI");
        primaryStage.show();
    }

    
    private void displayList(TextArea taList) {
        taList.setText(list.toString());
    }

    public static void main(String[] args) {
        launch(args);
    }
}
