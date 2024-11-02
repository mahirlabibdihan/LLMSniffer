


public class QueueHandler{
    public static void main(String[] args) {
        Queue q1 = new Queue();
        for (int i = 0; i < 20; i++) {
            int value = (int) (i + Math.random() * (int) (Math.random() * 9));
            q1.enqueue(value);
            System.out.println("TestQueue.enqueue(" + value + ")" + " ");
        }
        for (int i = 0; i < 20; i++) {
            int value = q1.dequeue();
            System.out.println("TestQueue.dequeue(" + value + ")" + " ");
        }
    }
}
