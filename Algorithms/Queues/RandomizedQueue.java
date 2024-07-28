import java.util.Iterator;
import java.util.NoSuchElementException;

import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] queue;
    private int size;

    // construct an empty randomized queue
    public RandomizedQueue() {
        queue = (Item[]) new Object[2];
        size = 0;
    }

    // is the randomized queue empty?
    public boolean isEmpty() { return size == 0; }

    // return the number of items on the randomized queue
    public int size() { return size; }

    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < size; i++) { copy[i] = queue[i]; }
        queue = copy;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) throw new IllegalArgumentException("null을 추가할 수 없습니다.");
        if (size == queue.length) resize(2 * queue.length);
        queue[size++] = item;
    }

    // remove and return a random item
    public Item dequeue() {
        if (isEmpty()) throw new java.util.NoSuchElementException("비어있는 큐에서 원소를 제거할 수 없습니다.");
        int idx = StdRandom.uniformInt(0, size);
        Item item = queue[idx];
        queue[idx] = queue[--size];
        queue[size] = null;
        if (size > 0 && size == queue.length / 4) resize(queue.length / 2);
        return item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (isEmpty()) throw new java.util.NoSuchElementException("비어있는 큐에서 원소를 찾을 수 없습니다.");
        return queue[StdRandom.uniformInt(0, size)];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() { return new QueueIterator(); }

    private class QueueIterator implements Iterator<Item> {
        private int[] order;
        private int currentIdx;

        public QueueIterator() {
            order = new int[size];
            for (int i = 0; i < size; i++) { order[i] = i; }
            StdRandom.shuffle(order);
            currentIdx = 0;
        }

        public boolean hasNext() { return (currentIdx < order.length && order[currentIdx] < queue.length); }
        public void remove() { throw new UnsupportedOperationException(); }
        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            return queue[order[currentIdx++]];
        }
    }
    // unit testing (required)
    public static void main(String[] args) {
        RandomizedQueue<Integer> rq = new RandomizedQueue<>();

        // Test isEmpty() and size()
        assert rq.isEmpty();
        assert rq.size() == 0;

        // Test enqueue()
        rq.enqueue(1);
        rq.enqueue(2);
        rq.enqueue(3);
        rq.enqueue(4);
        rq.enqueue(5);

        // Test size()
        assert rq.size() == 5;

        // Test sample()
        System.out.println("Sampled item: " + rq.sample());

        // Test dequeue()
        System.out.println("Dequeued item: " + rq.dequeue());
        System.out.println("Dequeued item: " + rq.dequeue());

        // Test size() after dequeue
        assert rq.size() == 3;

        // Test iterator
        System.out.println("Items in random order:");
        for (int item : rq) {
            System.out.println(item);
        }

        // Test isEmpty() and size() after multiple dequeues
        rq.dequeue();
        rq.dequeue();
        rq.dequeue();
        assert rq.isEmpty();
        assert rq.size() == 0;

        Iterator<Integer> it = rq.iterator();
        System.out.println(it.hasNext());
        it.next();

        System.out.println("All tests passed!");
    }

}