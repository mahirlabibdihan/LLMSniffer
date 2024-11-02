// This program shuffles rows in a 2D array

public class ArrayShuffler {

    public static void main(String[] args) {
        int[][] matrix = {{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}};

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        shuffle(matrix);

        System.out.println("\nShuffled Matrix:");
        printMatrix(matrix);
    }

    public static void shuffle(int[][] matrix) {
        int numRows = matrix.length;

        for (int i = 0; i < numRows; i++) {
            int randIndex = (int) (Math.random() * numRows);

            int[] temp = matrix[i];
            matrix[i] = matrix[randIndex];
            matrix[randIndex] = temp;
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}