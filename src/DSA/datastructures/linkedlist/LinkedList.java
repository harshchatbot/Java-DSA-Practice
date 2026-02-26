package DSA.datastructures.linkedlist;

public class LinkedList {

    private Node head;
    private Node tail;
    private int length;

    class Node {
        int value;
        Node next;

        // constructor for inner class i.e this node class
        Node(int value) {
            this.value = value;
        }

    }

    public LinkedList(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.println(temp.value);
            temp = temp.next;

        }

    }

    public void getHead() {
        System.out.println("Head: " + head.value);
    }

    public void getTail() {
        System.out.println("Tail: " + tail.value);
    }

    public void getLength() {
        System.out.println("Length: " + length);
    }

    // Append Method - add in the end
    public void append(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            head = newNode;
            tail = newNode;

        } else {

            tail.next = newNode;
            tail = newNode;
        }

        length++;
    }

    // Remove Last method - complex one
    // covering 3 scenarios
    // 1. LL with length 0
    // 2. LL with length 1 and 3. LL with length 2
    public Node removeLast() {
        if (length == 0)
            return null; // scenario 1
        Node temp = head;
        Node pre = head;
        while (temp.next != null) {
            pre = temp;
            temp = temp.next;
        }
        tail = pre;
        temp.next = null;
        length--;

        // scenario 2 where LL is of only 1 length then if we remove that last node then
        // head and tail should point to null
        if (length == 0) {
            head = null;
            tail = null;
        }

        return temp;
    }

    // Prepend method
    public void prepend(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }

        length++;
    }

    // Removing first item from the list here also 3 edge cases.
    public Node removeFirst() {
        if (length == 0)
            return null; // scenario 1
        Node temp = head;
        head = head.next;
        temp.next = null;
        length--;

        // scenario 2 where LL is of only 1 length then if we remove that last node then
        // head and tail should point to null
        if (length == 0) {
            // head = null; not required here as head is already set to null
            tail = null;
        }

        return temp;
    }

    // Get
    public Node get(int index) {
        if (index < 0 || index >= length)
            return null; // means that index cannot be less that 0 i.e negative 1 and cannot be more than
                         // length of the LL
        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    // Set
    public boolean set(int index, int value) {

        Node temp = get(index);
        if (temp != null) {
            temp.value = value;
            return true;

        }
        return false;
    }

    // Insert
    public boolean insert(int index, int value) {
        if (index < 0 || index > length)
            return false; // as we cagain cannot insert at -1 or greater than length of LL but yes we can
                          // prepend and append
        if (index == 0) {
            prepend(value);
            return true;
        }
        if (index == length) {
            append(value);
            return true;
        }

        // In case of insertion at middle ?
        Node newNode = new Node(value); // new node will be created which we will insert in LL
        Node temp = get(index - 1); // cuz where ever we want to insert in middle, we need to know the index of node
                                    // before
        newNode.next = temp.next; // now that newly created node is pointing to same node where temp.next is
                                  // pointing
        temp.next = newNode; // now temp.next is pointing to newNode
        length++;
        return true;

    }

    // Remove method
    public Node remove(int index) {
        if (index < 0 || index >= length)
            return null;
        if (index == 0)
            return removeFirst();
        if (index == length - 1)
            return removeLast(); // using removeLast directly in return as this method returntype is also same as
                                 // remove i.e node

        Node prev = get(index - 1);
        Node temp = prev.next; // cuz its O(1)

        prev.next = temp.next;
        temp.next = null;
        length--;

        return temp;
    }

    // Reverse method , complex one
    public void reverse() {
        Node temp = head;
        head = tail;
        tail = temp;
        Node after = temp.next;
        Node before = null;
        for (int i = 0; i < length; i++) {
            after = temp.next;
            temp.next = before;
            before = temp;
            temp = after;

        }
    }

    // ****** Find Middle Node ( ** Interview Question) */
    // Note : we are not allowed to find the middle node using length so we dont
    // have length member vairable
    // ensure both scenarios when we have odd number of nodes and when we have even
    // number of nodes
    // we will be using a strategy using two vairables called fast and slow :
    /*
     * Love it 🔥 Harsh — this is exactly the right direction (Floyd’s Tortoise &
     * Hare approach).
     * 
     * You’re thinking correctly:
     * 
     * slow → moves 1 step
     * 
     * fast → moves 2 steps
     * 
     * When fast reaches the end → slow is at middle
     */
    public Node findMiddleNode() {

        // take 2 vairables slow and fast and set them to head
        Node slow = head;
        Node fast = head;

        // now when we loop over the LL, fast iterate by +2 and slow by +1
        // here we will be having two situations
        // 1. Fast pointing at last node i.e case when we have odd number of nodes
        while (fast != null) {

            fast = fast.next; // step 1
            if (fast != null) {
                fast = fast.next; // step 2
                slow = slow.next; // +1 steps
            }
            

        }

        //2. When we have LL even
        while (fast != null && fast.next != null){

            fast = fast.next;
            if(fast != null){
                fast = fast.next;
            }
            slow = slow.next;
        }

        return slow;

    }

}
