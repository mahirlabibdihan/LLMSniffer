public class Main { public static void main(String[] args) {  int count = 0;  for (int year = 101; year <= 2100; year++) {   if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {    System.out.printf("%-5d", year);    count++;    if (count % 10 == 0) {     System.out.println();    }   }  }  System.out.println("\n\nThe number of leap years is " + count); }}