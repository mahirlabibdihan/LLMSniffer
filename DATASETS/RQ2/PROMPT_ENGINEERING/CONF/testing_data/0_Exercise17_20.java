import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class BinaryEditorApp extends JFrame {
    private JTextField fileNameField;
    private JTextArea binaryTextArea;
    private JButton loadButton;
    private JButton saveButton;

    public BinaryEditorApp() {
        super("Binary Editor");

        // Create the main frame
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Create a label and text field for file input
        JLabel fileLabel = new JLabel("Enter File Name:");
        fileNameField = new JTextField(20);

        // Create a button to load the file
        loadButton = new JButton("Load File");
        loadButton.addActionListener(new LoadButtonListener());

        // Create a text area for displaying binary representation
        binaryTextArea = new JTextArea();
        binaryTextArea.setEditable(false);

        // Create a button to save changes to the file
        saveButton = new JButton("Save Changes");
        saveButton.addActionListener(new SaveButtonListener());

        // Add components to the frame
        JPanel topPanel = new JPanel();
        topPanel.add(fileLabel);
        topPanel.add(fileNameField);
        topPanel.add(loadButton);

        add(topPanel, BorderLayout.NORTH);
        add(new JScrollPane(binaryTextArea), BorderLayout.CENTER);
        add(saveButton, BorderLayout.SOUTH);
    }

    private class LoadButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String fileName = fileNameField.getText();
            File file = new File(fileName);

            if (file.exists()) {
                try {
                    byte[] fileData = Files.readAllBytes(Path.of(fileName));
                    StringBuilder binaryData = new StringBuilder();

                    for (byte b : fileData) {
                        binaryData.append(Integer.toBinaryString(b & 0xFF));
                    }

                    binaryTextArea.setText(binaryData.toString());
                } catch (IOException e) {
                    binaryTextArea.setText("Error reading file!");
                }
            } else {
                binaryTextArea.setText("File not found!");
            }
        }
    }

    private class SaveButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String fileName = fileNameField.getText();
            String binaryData = binaryTextArea.getText();

            try {
                BufferedWriter writer = Files.newBufferedWriter(Path.of(fileName), StandardOpenOption.WRITE);
                writer.write(binaryData);
                writer.close();
                binaryTextArea.setText("Changes saved successfully!");
            } catch (IOException e) {
                binaryTextArea.setText("Error saving changes!");
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BinaryEditorApp app = new BinaryEditorApp();
            app.setVisible(true);
        });
    }
}