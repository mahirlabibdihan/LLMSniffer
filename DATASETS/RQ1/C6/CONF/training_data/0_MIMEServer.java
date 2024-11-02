import java.io.*;
import java.net.*;

public class MIMEServer extends Thread {

    private ServerSocket serverSocket;

    public MIMEServer(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(10000);
    }

    public void run() {
        while (true) {
            try {
                System.out.println("Waiting for client on port " + serverSocket.getLocalPort() + "...");
                Socket server = serverSocket.accept();

                System.out.println("Just connected to " + server.getRemoteSocketAddress());
                DataInputStream in = new DataInputStream(server.getInputStream());

                String request = in.readUTF();
                System.out.println("Client request: " + request);

                String[] requestParts = request.split(" ");
                String fileName = requestParts[1].substring(1);

                File file = new File(fileName);
                byte[] fileData = new byte[(int) file.length()];
                DataInputStream fileIn = new DataInputStream(new FileInputStream(file));
                fileIn.readFully(fileData);
                fileIn.close();

                DataOutputStream out = new DataOutputStream(server.getOutputStream());
                out.writeUTF("HTTP/1.1 200 OK\r\n");
                out.writeUTF("Content-Type: application/octet-stream\r\n");
                out.writeUTF("Content-Length: " + fileData.length + "\r\n\r\n");
                out.write(fileData);

                out.close();
                in.close();
                server.close();

            } catch (SocketTimeoutException s) {
                System.out.println("Socket timed out!");
                break;
            } catch (IOException e) {
                e.printStackTrace();
                break;
            }
        }

