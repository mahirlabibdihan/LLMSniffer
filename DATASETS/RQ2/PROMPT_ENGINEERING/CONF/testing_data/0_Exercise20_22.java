import java.util.Scanner;
import java.util.Stack;

public class NonRecursiveTowerOfHanoi {

    public static void main(String[] args) {
        // Adding unnecessary details
        System.out.println("Welcome to the Tower of Hanoi Solver!");

        // Getting the number of disks from user input
        System.out.print("Enter the number of disks: ");
        Scanner scanner = new Scanner(System.in);
        int numberOfDisks = scanner.nextInt();

        // Solving Tower of Hanoi using a non-recursive approach
        moveDisks(numberOfDisks, 'A', 'B', 'C');

        // Adding unnecessary details
        System.out.println("Tower of Hanoi solved successfully!");
    }

    // Adding unnecessary method comment
    /**
     * Move disks from source pole to target pole using auxiliary pole
     *
     * @param n     number of disks
     * @param source source pole
     * @param target target pole
     * @param aux   auxiliary pole
     */
    private static void moveDisks(int n, char source, char target, char aux) {
        Stack<HanoiMove> moveStack = new Stack<>();
        moveStack.push(new HanoiMove(n, source, target, aux));

        // Adding more unnecessary details
        System.out.println("Solving Tower of Hanoi non-recursively...");

        while (!moveStack.isEmpty()) {
            HanoiMove move = moveStack.pop();

            if (move.n == 1) {
                // Move a single disk from source to target
                // Adding unnecessary details
                System.out.println("Move disk from " + move.source + " to " + move.target);
            } else {
                // Move n-1 disks from source to auxiliary using target as the auxiliary
                moveStack.push(new HanoiMove(move.n - 1, move.aux, move.target, move.source));

                // Move the remaining disk from source to target
                // Adding unnecessary details
                System.out.println("Move disk from " + move.source + " to " + move.target);

                // Move n-1 disks from auxiliary to target using source as the auxiliary
                moveStack.push(new HanoiMove(move.n - 1, move.source, move.target, move.aux));
            }
        }

        // Adding more unnecessary details
        System.out.println("Tower of Hanoi solved non-recursively!");
    }

    // Adding an unnecessary class for HanoiMove
    private static class HanoiMove {
        int n;
        char source, target, aux;

        public HanoiMove(int n, char source, char target, char aux) {
            this.n = n;
            this.source = source;
            this.target = target;
            this.aux = aux;
        }
    }
}