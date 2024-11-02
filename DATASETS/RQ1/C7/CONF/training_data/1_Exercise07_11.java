



public class nan{
    static double mean;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double[] nums = new double[10];
        System.out.print("Enter 10 numbers: ");
        for (int i = 0; i < nums.length; i++) {
            nums[i] = in.nextDouble();
        }
        mean = mean(nums);
        double std = deviation(nums);

        System.out.printf("The mean is %.2f" + "\n", mean);
        System.out.printf("The standard deviation is %.5f", std);
    }

    public static double deviation(double[] x) {
        double numerator = 0.0;
        double denominator = x.length - 1;
        for (double d : x) {
            numerator += Math.pow((d - mean), 2);
        }
        return Math.sqrt((numerator / denominator));

    }

    public static double mean(double[] x) {
        double sum = 0;
        double total = x.length;
        for (double d : x) {
            sum += d;
        }
        return sum / total;

    }
}
