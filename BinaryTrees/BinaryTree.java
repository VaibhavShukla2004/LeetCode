import java.util.*;
import java.util.Scanner;

class Scan{
    public static Scanner sc = new Scanner(System.in);
}

class Node {
    int data;
    Node left,right;
    Node(int data){ this.data = data; }
    
    static void inOrder(Node root)
    {
        if(root == null){ return; }
        inOrder(root.left);
        System.out.print(root.data + " ");
        inOrder(root.right);
    }
    
    static void preOrder(Node root)
    {
        if(root == null){ return; }
        System.out.print(root.data + " ");
        preOrder(root.left);
        preOrder(root.right);
    }
    
    static void postOrder(Node root)
    {
        if(root == null){ return; }
        postOrder(root.left);
        postOrder(root.right);
        System.out.print(root.data + " ");
    }
    
    static void levelOrder(Node root)
    {
        LinkedList<Node> list = new LinkedList<>();
        list.offer(root);
        
        while(!list.isEmpty())
        {
            Node popped = list.poll();
            System.out.print(popped.data + " ");
            if(popped.left != null) list.offer(popped.left);
            if(popped.right != null) list.offer(popped.right);
        }
        
        return;
    }
    
    static Node buildNode()
    {
        Node temp = null;
        System.out.println("Put Node : ");
        int n = Scan.sc.nextInt();
        if(n == 1){
            System.out.println("Node data : "); 
            int data = Scan.sc.nextInt();
            temp = new Node(data);
            System.out.println("Left Side of " + data);
            temp.left = Node.buildNode();
            System.out.println("Right Side of " + data);
            temp.right = Node.buildNode();
        }
        else{ return null; }
        
        return temp;
    }
}

public class Main {
    public static void main(String[] args) {
        Node a = null;
        a = Node.buildNode();
        Node.inOrder(a);
    }
}