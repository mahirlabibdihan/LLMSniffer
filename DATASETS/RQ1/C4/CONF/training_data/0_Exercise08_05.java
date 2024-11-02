import java.util.Scanner;

public class AddMatrices {
    
    public static double[][] addMatrix(double[][] a, double[][] b) {
        if(a.length != b.length || a[0].length != b[0].length) {
            throw new IllegalArgumentException("Matrices must have same dimensions");
        }
        
        int rows = a.length;
        int cols = a[0].length;
        
        double[][] result = new double[rows][cols];
        
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                result[i][j] = a[i][j] + b[i][j];
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double[][] a = new double[3][3];
        double[][] b = new double[3][3];
        
        System.out.print("Enter matrix1: ");
        for(int i=0; i<a.length; i++) {
            for(int j=0; j<a[0].length; j++) {
                a[i][j] = input.nextDouble();
            }
        }
        
        System.out.print("Enter matrix2: ");
        for(int i=0; i<b.length; i++) {
            for(int j=0; j<b[0].length; j++) {
                b[i][j] = input.nextDouble();
            }
        }
        
        double[][] result = addMatrix(a, b);
        
        System.out.println("The addition of the matrices is: ");
        for(int i=0; i<result.length; i++) {
            for(int j=0; j<result[0].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
        
    }
}