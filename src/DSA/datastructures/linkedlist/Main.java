package DSA.datastructures.linkedlist;

public class Main {

    public static void main (String[] args) {

        LinkedList myLinkedList = new LinkedList(4);

        myLinkedList.getHead();
        myLinkedList.getTail();
        myLinkedList.getLength();

        //call append method to append value 2 after 4 or 1 as u wish the first value
        myLinkedList.append(2);

        myLinkedList.printList();

    }

    
}
