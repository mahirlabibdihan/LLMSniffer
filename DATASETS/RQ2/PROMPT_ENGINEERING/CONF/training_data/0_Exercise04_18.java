import java.util.Scanner;

public class StudentMajorAndStatus {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter two characters: ");
        String s = input.nextLine();

        char major = s.charAt(0);
        char status = s.charAt(1);

        String majorString, statusString;

        switch (major) {
            case 'M':
                majorString = "Mathematics";
                break;
            case 'C':
                majorString = "Computer Science";
                break;
            case 'I':
                majorString = "Information Technology";
                break;
            default:
                System.out.println("Invalid input");
                return;
        }

        switch (status) {
            case '1':
                statusString = "Freshman";
                break;
            case '2':
                statusString = "Sophomore";
                break;
            case '3':
                statusString = "Junior";
                break;
            case '4':
                statusString = "Senior";
                break;
            default:
                System.out.println("Invalid input");
                return;
        }

        System.out.println(majorString + " " + statusString);
    }
}
