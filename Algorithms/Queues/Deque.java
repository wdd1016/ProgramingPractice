import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private Node<Item> first, last;
    private int size;

    private class Node<Item>
    {
        Item item;
        Node<Item> prev;
        Node<Item> next;
    }
    // construct an empty deque
    public Deque() {
        first = null;
        last = null;
        size = 0;
    }

    // is the deque empty?
    public boolean isEmpty() { return size == 0; }

    // return the number of items on the deque
    public int size() { return size; }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException("null을 추가할 수 없습니다.");
        Node<Item> oldFirst = first;
        first = new Node<>();
        first.item = item;
        first.prev = null;
        first.next = oldFirst;
        if (isEmpty()) last = first;
        else oldFirst.prev = first;
        size++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException("null을 추가할 수 없습니다.");
        Node<Item> oldLast = last;
        last = new Node<>();
        last.item = item;
        last.prev = oldLast;
        last.next = null;
        if (isEmpty()) first = last;
        else oldLast.next = last;
        size++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) throw new java.util.NoSuchElementException("비어있는 덱에서 원소를 제거할 수 없습니다.");
        Item item = first.item;
        first = first.next;
        if (first == null) last = null;
        else first.prev = null;
        size--;
        return item;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (isEmpty()) throw new java.util.NoSuchElementException("비어있는 덱에서 원소를 제거할 수 없습니다.");
        Item item = last.item;
        last = last.prev;
        if (last == null) first = null;
        else last.next = null;
        size--;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() { return new DequeueIterator(); }

    private class DequeueIterator implements Iterator<Item> {
        private Node<Item> current = first;

        public boolean hasNext() { return current != null; }
        public void remove() { throw new UnsupportedOperationException(); }
        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<>();

        System.out.println("Testing isEmpty() on new deque: " + deque.isEmpty()); // true
        System.out.println("Testing size() on new deque: " + deque.size()); // 0

        deque.addLast(1);
        System.out.println("Added 1 to the front. isEmpty(): " + deque.isEmpty()); // false
        System.out.println("Size after adding 1 to the front: " + deque.size()); // 1

        deque.addLast(2);
        System.out.println("Added 2 to the back. Size: " + deque.size()); // 2

        System.out.println("First item removed: " + deque.removeFirst()); // 1
        System.out.println("Size after removing first item: " + deque.size()); // 1

        System.out.println("Last item removed: " + deque.removeLast()); // 2
        System.out.println("Size after removing last item: " + deque.size()); // 0


        Iterator<Integer> it = deque.iterator();
        it.next();
        it.remove();
    }
}