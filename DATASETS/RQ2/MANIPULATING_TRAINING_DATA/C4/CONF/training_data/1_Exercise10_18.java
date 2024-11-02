

import java.math.BigInteger;
import java.util.Arrays;


public class Exercise10_18 {
    
    static final BigInteger lowerBound = BigInteger.valueOf(Long.MAX_VALUE);
    BigInteger[] primeBigIntegers = new BigInteger[5];
    BigInteger testNum = lowerBound;

    public static void main(String[] args) {
        Exercise10_18 obj = new Exercise10_18();

        int idx = 0;
        while (idx < 5) {
            obj.testNum = obj.testNum.nextProbablePrime();
            obj.primeBigIntegers[idx] = obj.testNum;
            idx++;
        }
        System.out.println(Arrays.toString(obj.primeBigIntegers));
    }

}