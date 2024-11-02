public class SelfOrganizingList {
    
    private Node head;
    private int size;

    public SelfOrganizingList() {
        this.head = null;
        this.size = 0;
    }

    public void add(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        size++;
    }

    public boolean contains(int data) {
        Node current = head;
        Node previous = null;
        while (current != null && current.data != data) {
            previous = current;
            current = current.next;
        }
        if (current != null) {
            if (previous != null) {
                previous.next = current.next;
                current.next = head;
                head = current;
            }
            return true;
        }
        return false;
    }

    private class Node {
        private int data;
        private Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public static void main(String[] args) {
        SelfOrganizingList list = new SelfOrganizingList();

        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);
        list.add(50);

        System.out.println("Is 30 in the list? " + list.contains(30));
        System.out.println("Is 10 in the list? " + list.contains(10));
        System.out.println("Is 60 in the list? " + list.contains(60));
        System.out.println("Is 20 in the list? " + list.contains(20));

    }
}

