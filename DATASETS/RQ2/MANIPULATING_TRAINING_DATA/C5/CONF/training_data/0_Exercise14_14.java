import javafx.application.Application;import javafx.geometry.Insets;import javafx.geometry.Point3D;import javafx.scene.Group;import javafx.scene.PerspectiveCamera;import javafx.scene.Scene;import javafx.scene.SceneAntialiasing;import javafx.scene.layout.StackPane;import javafx.scene.paint.Color;import javafx.scene.paint.PhongMaterial;import javafx.scene.shape.Box;import javafx.scene.transform.Rotate;import javafx.scene.transform.Translate;import javafx.stage.Stage;public class Rectanguloid extends Application {  private final double BOX_SIZE = 100;  @Override  public void start(Stage primaryStage) throws Exception {    