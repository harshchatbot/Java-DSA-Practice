package DSA.datastructures.linkedlist;

public class Main {

    public static void main (String[] args) {

        //LinkedList myLinkedList = new LinkedList(4);
        //LinkedList myLinkedList = new LinkedList(1);
        LinkedList myLinkedList = new LinkedList(2);

        //myLinkedList.getHead();
        //myLinkedList.getTail();
        //myLinkedList.getLength();

        //call append method to append value 2 after 4 or 1 as u wish the first value
        //myLinkedList.append(2);
        myLinkedList.append(3);

        //myLinkedList.printList(); commented in removeLast method scenario

        // 2 items - returns 2 node
        //System.out.println(myLinkedList.removeLast().value);
        // 1 item - returns 1 node
        //System.out.println(myLinkedList.removeLast().value);
        // 0 items - returns null
        //System.out.println(myLinkedList.removeLast());

        myLinkedList.prepend(1);

        myLinkedList.printList();

    }

    
}
