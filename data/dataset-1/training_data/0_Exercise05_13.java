public class Main {
    public static void main(String[] args) {
        int n = 1;
        while (n * n * n < 12000) {
            n++;
        }
        n--;
        System.out.println("The largest integer n such that n^3 < 12,000 is " + n);
    }
}
