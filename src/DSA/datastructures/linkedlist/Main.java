package DSA.datastructures.linkedlist;

import DSA.datastructures.linkedlist.LinkedList.Node;

public class Main {

    public static void main(String[] args) {

        // LinkedList myLinkedList = new LinkedList(4);
        LinkedList myLinkedList = new LinkedList(1);
        // LinkedList myLinkedList = new LinkedList(2);
        // LinkedList myLinkedList = new LinkedList(0);
        // LinkedList myLinkedList = new LinkedList(11);
        // LinkedList myLinkedList = new LinkedList(0);

        // myLinkedList.getHead();
        // myLinkedList.getTail();
        // myLinkedList.getLength();

        // call append method to append value 2 after 4 or 1 as u wish the first value
        // myLinkedList.append(2);
        // myLinkedList.append(3);
        // myLinkedList.append(2);

        // myLinkedList.printList(); commented in removeLast method scenario

        // 2 items - returns 2 node
        // System.out.println(myLinkedList.removeLast().value);
        // 1 item - returns 1 node
        // System.out.println(myLinkedList.removeLast().value);
        // 0 items - returns null
        // System.out.println(myLinkedList.removeLast());

        // myLinkedList.prepend(1);

        // myLinkedList.printList();

        // 2 items - returns 2 node
        // System.out.println(myLinkedList.removeFirst().value);
        // 1 item - returns 1 node
        // System.out.println(myLinkedList.removeFirst().value);
        // 0 items - returns null
        // System.out.println(myLinkedList.removeFirst());

        // myLinkedList.append(1);
        // myLinkedList.append(2);
        // myLinkedList.append(3);
        // myLinkedList.append(4);

        // System.out.println(myLinkedList.get(2).value + "\n");

        // myLinkedList.append(3);
        // myLinkedList.append(23);
        // myLinkedList.append(7);

        // myLinkedList.set(1, 4);

        // myLinkedList.append(2);

        // myLinkedList.insert(1, 1);

        // myLinkedList.remove(2);

        // myLinkedList.reverse();


        //FInd the middle node
        LinkedList myList = new LinkedList(1);
        myList.append(2);
        myList.append(3);
        myList.append(4);
        myList.append(5);
        Node middleNode = myList.findMiddleNode();
        System.out.println("Middle Node Odd: " + middleNode.value); // Output: 3

        myList.append(6);
        middleNode = myList.findMiddleNode();
        System.out.println("Middle Node Even: " + middleNode.value); // Output: 4

        myLinkedList.printList();

    }

}
