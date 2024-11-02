import javax.swing.*;
import java.awt.*;

public class GradePieChart extends JFrame {
    public GradePieChart() {
        setTitle("Grade Pie Chart");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void paint(Graphics g) {
        super.paint(g);
        // Define the dimensions of the chart area
        int chartWidth = 200;
        int chartHeight = 200;
        int chartX = 100;
        int chartY = 100;

        // Calculate the angles of each pie slice
        double projectAngle = 0.2 * 360;
        double quizAngle = 0.1 * 360;
        double midtermAngle = 0.3 * 360;
        double finalAngle = 0.4 * 360;

        // Define the colors of each pie slice
        Color projectColor = Color.RED;
        Color quizColor = Color.BLUE;
        Color midtermColor = Color.GREEN;
        Color finalColor = Color.ORANGE;

        // Draw the pies
        g.setColor(projectColor);
        g.fillArc(chartX, chartY, chartWidth, chartHeight, 0, (int) projectAngle);

        g.setColor(quizColor);
        g.fillArc(chartX, chartY, chartWidth, chartHeight, (int) projectAngle, (int) quizAngle);

        g.setColor(midtermColor);
        g.fillArc(chartX, chartY, chartWidth, chartHeight, (int) (projectAngle + quizAngle), (int) midtermAngle);

        g.setColor(finalColor);
        g.fillArc(chartX, chartY, chartWidth, chartHeight, (int) (projectAngle + quizAngle + midtermAngle), (int) finalAngle);

        // Draw the labels
        g.setColor(Color.BLACK);
        g.drawString("Projects", chartX - 50, chartY - 20);
        g.drawString("Quizzes", chartX + chartWidth + 10, chartY + 20);
        g.drawString("Midterm Exams", chartX + chartWidth / 2, chartY + chartHeight + 20);
        g.drawString("Final Exam", chartX + chartWidth / 2, chartY - 60);
    }

    public static void main(String[] args) {
        new GradePieChart();
    }
}