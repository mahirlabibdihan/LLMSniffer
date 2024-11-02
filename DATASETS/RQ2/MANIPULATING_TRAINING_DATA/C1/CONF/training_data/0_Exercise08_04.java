public class ComputeWeeklyHours {
   public static void main(String[] args) {
      int[][] weeklyHours = {
         {2, 4, 3, 4, 5, 8, 8},
         {7, 3, 4, 3, 3, 4, 4},
         {3, 3, 4, 3, 3, 2, 2},
         {9, 3, 4, 7, 3, 4, 1},
         {3, 5, 4, 3, 6, 3, 8},
         {3, 4, 4, 6, 3, 4, 4},
         {3, 7, 4, 8, 3, 8, 4},
         {6, 3, 5, 9, 2, 7, 9}
      };
      
      int[] totalHours = new int[weeklyHours.length];
      
      // Compute the total hours for each employee
      for (int i = 0; i < weeklyHours.length; i++) {
         int sum = 0;
         for (int j = 0; j < weeklyHours[i].length; j++) {
            sum += weeklyHours[i][j];
         }
         totalHours[i] = sum;
      }
      
      // Create a list of tuples containing employee number and total hours
      List<Tuple<Integer, Integer>> employeeHours = new ArrayList<>();
      for (int i = 0; i < totalHours.length; i++) {
         employeeHours.add(new Tuple<>(i, totalHours[i]));
      }
      
      // Sort the list in decreasing order of total hours
      employeeHours.sort((a, b) -> b.getSecond() - a.getSecond());
      
      // Display the sorted list
      for (Tuple<Integer, Integer> employee : employeeHours) {
         System.out.printf("Employee %d: %d hours\n", employee.getFirst(), employee.getSecond());
      }
   }
}

class Tuple<A, B> {
   private A first;
   private B second;
   
   public Tuple(A first, B second) {
      this.first = first;
      this.second = second;
   }
   
   public A getFirst() {
      return first;
   }
   
   public B getSecond() {
      return second;
   }
}