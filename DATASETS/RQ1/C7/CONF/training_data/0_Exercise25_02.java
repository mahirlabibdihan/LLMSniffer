class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    Node root;

    public BinaryTree() {
        this.root = null;
    }

    public boolean isFullBinaryTree(Node node) {
        
        if (node == null) {
            return true;
        }

        
        if (node.left == null && node.right == null) {
            return true;
        }

        
        if (node.left == null || node.right == null) {
            return false;
        }

        
        return isFullBinaryTree(node.left) && isFullBinaryTree(node.right);
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);

        if (tree.isFullBinaryTree(tree.root)) {
            System.out.println("The tree is a full binary tree.");
        } else {
            System.out.println("The tree is not a full binary tree.");
        }
    }
}
