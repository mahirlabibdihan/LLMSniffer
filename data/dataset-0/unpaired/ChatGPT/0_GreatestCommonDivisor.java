public class GCD {
  public static void main(String[] args) {
    int num1 = 24, num2 = 60, gcd = 1;
    for(int i = 1; i <= num1 && i <= num2; ++i)
    {
        if(num1 % i==0 && num2 % i==0)
            gcd = i;
    }
    System.out.println("GCD of " + num1 +" and " + num2 + " is: " + gcd);
  }
}


public class GCD {
  public static int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
  }
  public static void main(String[] args) {
    int num1 = 24, num2 = 60;
    int gcd = gcd(num1, num2);
    System.out.println("GCD of " + num1 +" and " + num2 + " is: " + gcd);
  }
}

