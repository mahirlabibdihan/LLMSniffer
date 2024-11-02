import java.util.Scanner;

public class MatrixExplorer {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the size for the matrix: ");
        int size = input.nextInt();

        int[][] matrix = new int[size][size];

        // Filling the matrix with random 0s and 1s
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = (int) (Math.random() * 2);
            }
        }

        // Printing the matrix
        System.out.println("Generated Matrix:");
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.println();
        }

        // Checking rows for all 0s or 1s
        for (int i = 0; i < size; i++) {
            boolean allZeros = true;
            boolean allOnes = true;
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] != 0) {
                    allZeros = false;
                }
                if (matrix[i][j] != 1) {
                    allOnes = false;
                }
            }
            if (allZeros) {
                System.out.println("All 0s on row " + (i + 1));
            }
            if (allOnes) {
                System.out.println("All 1s on row " + (i + 1));
            }
        }

        // Checking columns for same numbers
        for (int j = 0; j < size; j++) {
            boolean sameNumbers = true;
            int num = matrix[0][j];
            for (int i = 1; i < size; i++) {
                if (matrix[i][j] != num) {
                    sameNumbers = false;
                    break;
                }
            }
            if (sameNumbers) {
                System.out.println("All same numbers on column " + (j + 1));
            }
        }

        // Checking major diagonal for same numbers
        boolean sameMajorDiagonal = true;
        int majorDiagonalNum = matrix[0][0];
        for (int i = 1; i < size; i++) {
            if (matrix[i][i] != majorDiagonalNum) {
                sameMajorDiagonal = false;
                break;
            }
        }
        if (sameMajorDiagonal) {
            System.out.println("All same numbers on the major diagonal");
        }

        // Checking sub-diagonal for same numbers
        boolean sameSubDiagonal = true;
        int subDiagonalNum = matrix[size - 1][0];
        for (int i = size - 2, j = 1; i >= 0 && j < size; i--, j++) {
            if (matrix[i][j] != subDiagonalNum) {
                sameSubDiagonal = false;
                break;
            }
        }
        if (sameSubDiagonal) {
            System.out.println("All same numbers on the sub-diagonal");
        }

        input.close();
    }
}