import java.io.*;

public class Exercise17_02{
    public static void main(String[] args) throws IOException {
        File file = new File("Exercise17_02.dat");

        
        DataOutputStream output = null;
        if (file.exists()) {
            output = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(file, true)));
        } else {
            output = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(file)));
        }

        
        for (int i = 0; i < 100; i++) {
            output.writeInt((int) (Math.random() * 100));
        }

        
        output.close();

        System.out.println("Data has been written to " + file.getAbsolutePath());
    }
}
