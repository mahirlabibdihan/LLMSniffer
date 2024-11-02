import java.util.Scanner;

public class PasswordChecker {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter a password
        System.out.print("Enter a password: ");
        String password = input.nextLine();

        // Check if the password is valid
        if (checkPassword(password)) {
            System.out.println("Valid Password");
        } else {
            System.out.println("Invalid Password");
        }
    }

    public static boolean checkPassword(String password) {
        // Check if the password has at least 8 characters
        if (password.length() < 8) {
            return false;
        }

        // Check if the password consists of only letters and digits
        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);
            if (!Character.isLetterOrDigit(ch)) {
                return false;
            }
        }

        // Check if the password contains at least two digits
        int count = 0;
        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);
            if (Character.isDigit(ch)) {
                count++;
            }
        }
        if (count < 2) {
            return false;
        }

        // If all checks pass, the password is valid
        return true;
    }
}