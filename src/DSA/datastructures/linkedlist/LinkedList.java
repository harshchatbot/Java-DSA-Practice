package DSA.datastructures.linkedlist;

public class LinkedList {

    private Node head;
    private Node tail;
    private int length;

    class Node {
        int value;
        Node next;

        //constructor for inner class i.e this node class
        Node(int value){
            this.value = value;
        }

        
    }

    public LinkedList(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public void printList(){
        Node temp = head;
        while(temp != null){
            System.out.println(temp.value);
            temp = temp.next;

        }
        
    }

    public void getHead(){
        System.out.println("Head: "+ head.value);
    }

    public void getTail(){
        System.out.println("Tail: "+ tail.value);
    }

    public void getLength(){
        System.out.println("Length: "+ length);
    }



    //Append Method  - add in the end
    public void append(int value){
        Node newNode = new Node(value);
        if(length == 0){
            head = newNode;
            tail = newNode;

        }else {

            tail.next = newNode;
            tail = newNode;
        }

        length++;
    }

    //Remove Last method - complex one
    //covering 3 scenarios
    //1. LL with length 0
    //2. LL with length 1 and 3. LL with length 2
    public Node removeLast(){
        if(length == 0) return null;  //scenario 1
        Node temp = head;
        Node pre = head;
        while(temp.next != null){
            pre = temp;
            temp = temp.next;
        }
        tail = pre;
        temp.next = null;
        length--;

        //scenario 2 where LL is of only 1 length then if we remove that last node then head and tail should point to null
        if(length == 0){
            head = null;
            tail = null;
        }

        return temp;
    }
    
}
