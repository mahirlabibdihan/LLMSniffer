import javax.swing.*;
import java.awt.*;

public class GradeBarChart extends JFrame {
    public GradeBarChart() {
        setTitle("Grade Bar Chart");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void paint(Graphics g) {
        super.paint(g);
        
        int chartWidth = 300;
        int chartHeight = 200;
        int chartX = 50;
        int chartY = 50;

        
        int projectLength = (int) (chartWidth * 0.2);
        int quizLength = (int) (chartWidth * 0.1);
        int midtermLength = (int) (chartWidth * 0.3);
        int finalLength = (int) (chartWidth * 0.4);

        
        Color projectColor = Color.RED;
        Color quizColor = Color.BLUE;
        Color midtermColor = Color.GREEN;
        Color finalColor = Color.ORANGE;

        
        g.setColor(projectColor);
        g.fillRect(chartX, chartY, projectLength, chartHeight);

        g.setColor(quizColor);
        g.fillRect(chartX + projectLength, chartY, quizLength, chartHeight);

        g.setColor(midtermColor);
        g.fillRect(chartX + projectLength + quizLength, chartY, midtermLength, chartHeight);

        g.setColor(finalColor);
        g.fillRect(chartX + projectLength + quizLength + midtermLength, chartY, finalLength, chartHeight);

        
        g.setColor(Color.BLACK);
        g.drawString("Projects", chartX, chartY + chartHeight + 20);
        g.drawString("Quizzes", chartX + projectLength, chartY + chartHeight + 20);
        g.drawString("Midterm Exams", chartX + projectLength + quizLength, chartY + chartHeight + 20);
        g.drawString("Final Exam", chartX + projectLength + quizLength + midtermLength, chartY + chartHeight + 20);
    }

    public static void main(String[] args) {
        new GradeBarChart();
    }
}