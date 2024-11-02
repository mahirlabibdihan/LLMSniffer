import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.apache.commons.net.ftp.FTP;
import org.apache.commons.net.ftp.FTPClient;

public class FTPClientExample {
    public static void main(String[] args) {
        FTPClient ftpClient = new FTPClient();
        try {
            ftpClient.connect("ftp.example.com");
            ftpClient.login("username", "password");
            ftpClient.enterLocalPassiveMode();
            ftpClient.setFileType(FTP.BINARY_FILE_TYPE);

            // Upload file
            String fileToUpload = "file.txt";
            InputStream inputStream = new FileInputStream(fileToUpload);
            ftpClient.storeFile(fileToUpload, inputStream);
            inputStream.close();

            ftpClient.logout();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                ftpClient.disconnect();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

