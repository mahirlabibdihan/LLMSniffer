
class HttpClient {

    public static void main(String[] args) throws IOException {
        
        Socket socket = new Socket("www.example.com", 80);

        
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        
        out.println("GET / HTTP/1.1");
        out.println("Host: www.example.com");
        out.println();

        
        String response;
        while ((response = in.readLine()) != null) {
            System.out.println(response);
        }

        
        socket.close();
    }
}

