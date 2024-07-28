import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import java.util.Iterator;

//public class Permutation {
//    public static void main(String[] args) {
//        int k = Integer.parseInt(args[0]);
//        RandomizedQueue<String> rq = new RandomizedQueue<>();
//
//        while (!StdIn.isEmpty()) {
//            rq.enqueue(StdIn.readString());
//        }
//
//        Iterator<String> it = rq.iterator();
//        for (int i = 0; i < k; i++) {
//            StdOut.println(it.next());
//        }
//    }
//}

// Knuth's method refers to the Fisher-Yates shuffle,
// which is a well-known algorithm for generating a random permutation of a finite sequence—in this case,
// to solve the problem using a single Deque or RandomizedQueue of maximum size k.

public class Permutation {
    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        if (k < 0) throw new IllegalArgumentException("k must be non-negative");

        RandomizedQueue<String> rq = new RandomizedQueue<>();
        int count = 0;

        while (!StdIn.isEmpty()) {
            String item = StdIn.readString();
            count++;

            if (rq.size() < k) {
                rq.enqueue(item);
            } else {
                int r = StdRandom.uniformInt(count);
                if (r < k) {
                    rq.dequeue();
                    rq.enqueue(item);
                }
            }
        }

        Iterator<String> it = rq.iterator();
        for (int i = 0; i < k && it.hasNext(); i++) {
            StdOut.println(it.next());
        }
    }
}