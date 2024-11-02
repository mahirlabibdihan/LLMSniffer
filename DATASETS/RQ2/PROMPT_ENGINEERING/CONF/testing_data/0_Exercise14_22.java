import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class ConnectTwoCircles extends JFrame {
    public ConnectTwoCircles() {
        setTitle("Connect Two Circles");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Random random = new Random();

                int centerX1 = random.nextInt(getWidth() - 30) + 15;
                int centerY1 = random.nextInt(getHeight() - 30) + 15;

                int centerX2 = random.nextInt(getWidth() - 30) + 15;
                int centerY2 = random.nextInt(getHeight() - 30) + 15;

                int radius = 15;

                g.drawOval(centerX1 - radius, centerY1 - radius, 2 * radius, 2 * radius);
                g.drawOval(centerX2 - radius, centerY2 - radius, 2 * radius, 2 * radius);

                // Calculate the distance between centers
                double distance = Math.sqrt(Math.pow(centerX2 - centerX1, 2) + Math.pow(centerY2 - centerY1, 2));

                // Draw a line connecting the circles
                if (distance > 2 * radius) {
                    g.drawLine(centerX1, centerY1, centerX2, centerY2);
                }
            }
        };

        add(panel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ConnectTwoCircles connectTwoCircles = new ConnectTwoCircles();
            connectTwoCircles.setVisible(true);
        });
    }
}