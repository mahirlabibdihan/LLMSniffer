import java.util.Scanner;public class CommonPrefixFinderByHarryDulaney {    public static void main(String[] args) {        Scanner input = new Scanner(System.in);        System.out.println("Welcome to the Common Prefix Finder!");        System.out.print("Enter the first string: ");        String firstString = input.nextLine();        System.out.print("Enter the second string: ");        String secondString = input.nextLine();        System.out.print("The common prefix is: ");        int minLength = Math.min(firstString.length(), secondString.length());        StringBuilder commonPrefix = new StringBuilder();        for (int i = 0; i < minLength; i++) {            char charFromFirst = firstString.charAt(i);            char charFromSecond = secondString.charAt(i);            if (charFromFirst == charFromSecond) {                commonPrefix.append(charFromFirst);            } else {                break; // No need to continue if characters don't match            }        }        if (commonPrefix.length() == 0) {            System.out.println("The strings have no common prefix.");        } else {            System.out.println(commonPrefix.toString());        }        input.close();    }}