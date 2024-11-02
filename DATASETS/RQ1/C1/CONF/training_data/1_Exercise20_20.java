package ch_20;

import java.io.File;
import java.util.Scanner;
import java.util.Stack;


public class Exercise20_20 {
    public static void main(String[] args) {

        System.out.print("Enter a directory or a file: ");
        Scanner input = new Scanner(System.in);
        String directory = input.nextLine();
        System.out.println(getSize(new File(directory)) + " bytes");
    }

    public static long getSize(File file) {
        long size = 0; // Total size of all files

        Stack<File> stack = new Stack<File>();
        stack.push(file);

        while (!stack.empty()) {
            File t = stack.pop();
            if (t.isDirectory()) {
                File[] files = t.listFiles(); // All files and subdirectories
                for (File f : files) {
                    stack.push(f);
                }
            } else {
                size += t.length();
            }
        }

        return size;
    }
}
