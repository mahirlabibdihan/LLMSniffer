

import java.io.*;
import java.nio.file.Files;
import java.util.Arrays;


public class FileAggregator {
    private static final String PARENT_PATH = "ch_17/exercise17_12";

    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("Usage: java FileAggregator SourceFile1 . . . SourceFilen TargetFile");
            return;
        }
        File[] sourceFiles = new File[args.length - 1]; 
        String targetFile = args[args.length - 1]; 
        File outFile = new File(PARENT_PATH, targetFile);
        for (int i = 0; i < args.length - 1; i++) {
            sourceFiles[i] = new File(PARENT_PATH, args[i]);
        }
        try {
            combineFiles(sourceFiles, outFile);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    private static void combineFiles(File[] srcFiles, File targetFile) throws Exception {
        System.out.println("Combining src files into target file: " + targetFile.getName());
        byte[][] bytes = new byte[srcFiles.length][];
        int arraysIdx = 0;
        for (File f : srcFiles) {
            System.out.println("Processing: " + f.getName());
            bytes[arraysIdx++] = Files.readAllBytes(f.toPath());
        }
        FileOutputStream outputStream = new FileOutputStream(targetFile);
        for (byte[] bytArray : bytes) {
            outputStream.write(bytArray);
        }
        outputStream.flush();
        outputStream.close();
        System.out.println("Completed: Success");
    }
}
