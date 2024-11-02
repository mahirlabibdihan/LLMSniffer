import java.io.*;

public class Exercise17_12 {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Exercise17_12 SourceFile1 . . . SourceFilen TargetFile");
            System.exit(0);
        }

        try {
            FileOutputStream outputStream = new FileOutputStream(args[args.length - 1]);

            for (int i = 0; i < args.length - 1; i++) {
                FileInputStream inputStream = new FileInputStream(args[i]);
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    outputStream.write(buffer, 0, bytesRead);
                }
                inputStream.close();
            }

            outputStream.close();
            System.out.println("Files combined successfully into " + args[args.length - 1]);
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
