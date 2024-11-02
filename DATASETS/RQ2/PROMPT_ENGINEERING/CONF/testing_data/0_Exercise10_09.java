import java.util.Scanner;

public class TestCourse {
    public static void main(String[] args) {
        // Create a course
        Course course = new Course("Introduction to Programming");

        // Add three students
        course.addStudent("Alice");
        course.addStudent("Bob");
        course.addStudent("Charlie");

        // Display the students in the course
        System.out.println("Students in the course:");
        course.displayStudents();

        // Remove one student
        System.out.println("\nRemoving student Bob...");
        course.dropStudent("Bob");

        // Display the students in the course again
        System.out.println("\nStudents in the course after removing Bob:");
        course.displayStudents();

        // Clear all students from the course
        System.out.println("\nClearing all students from the course...");
        course.clear();

        // Display the students in the course one more time
        System.out.println("\nStudents in the course after clearing:");
        course.displayStudents();
    }
}

class Course {
    private String courseName;
    private String[] students;
    private int numberOfStudents;

    public Course(String courseName) {
        this.courseName = courseName;
        students = new String[1]; // Start with an array of size 1
        numberOfStudents = 0;
    }

    public void addStudent(String student) {
        if (numberOfStudents == students.length) {
            // If the array is full, increase its size by creating a new larger array
            String[] newStudents = new String[students.length * 2];
            System.arraycopy(students, 0, newStudents, 0, students.length);
            students = newStudents;
        }
        students[numberOfStudents] = student;
        numberOfStudents++;
    }

    public void dropStudent(String student) {
        for (int i = 0; i < numberOfStudents; i++) {
            if (students[i].equals(student)) {
                // Move students after the removed one to the left
                for (int j = i; j < numberOfStudents - 1; j++) {
                    students[j] = students[j + 1];
                }
                students[numberOfStudents - 1] = null;
                numberOfStudents--;
                break; // Exit loop after finding and removing the student
            }
        }
    }

    public void clear() {
        // Simply reset the array and the number of students
        students = new String[1];
        numberOfStudents = 0;
    }

    public void displayStudents() {
        for (int i = 0; i < numberOfStudents; i++) {
            System.out.println(students[i]);
        }
    }
}