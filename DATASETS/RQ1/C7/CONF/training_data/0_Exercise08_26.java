
public class SortRowsDemo {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.println("Enter a 3-by-3 matrix row by row:");
        double[][] m = new double[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                m[i][j] = input.nextDouble();
            }
        }

        
        double[][] sorted = sortRows(m);

        
        System.out.println("The row-sorted array is");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(sorted[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static double[][] sortRows(double[][] m) {
        
        double[][] sorted = new double[3][3];
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sorted[i][j] = m[i][j];
            }
        }
        
        for (int i = 0; i < 3; i++) {
            Arrays.sort(sorted[i]);
        }
        
        return sorted;
    }

}
