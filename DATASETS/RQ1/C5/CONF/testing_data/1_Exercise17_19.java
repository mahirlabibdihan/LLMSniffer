

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Scanner;


public class HexReader{
    static BufferedInputStream bufferedInputStream;
    static ArrayList<String> strBytes;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        strBytes = new ArrayList<>();
        System.out.println("Enter a filename: ");
        String fileName = in.nextLine().trim();
        try {
            bufferedInputStream = new BufferedInputStream(new FileInputStream(fileName));
            int b;
            while ((b = bufferedInputStream.read()) != -1) {
                String val = getBits(b);
                System.out.println("Read byte value = " + val);
                int asInteger = Integer.parseInt(val, 2);
                strBytes.add(Integer.toHexString(asInteger).toUpperCase());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("The byte contents of the file, converted to hex are: ");
        System.out.println(strBytes.toString());
    }

    public static String getBits(int value) {
        StringBuilder bits = new StringBuilder();
        for (int i = 0; i < 8; i++) {
            bits.insert(0, (value & 1));
            value >>= 1;
        }
        return bits.toString();
    }
}
