import java.util.Scanner;public class ASCIIToChar {  public static void main(String[] args) {    Scanner scanner = new Scanner(System.in);    // Prompt user to enter an ASCII code    System.out.print("Enter an ASCII code (between 0 and 127): ");    int asciiCode = scanner.nextInt();    // Convert the ASCII code to a character    char character = (char) asciiCode;    // Display the character    System.out.printf("The character for the ASCII code %d is %c\n", asciiCode, character);    scanner.close();  }}