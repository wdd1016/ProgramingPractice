import java.util.ArrayList;
import java.util.Collections;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;

public class Solver {
    private SearchNode minSearchNode;


    private class SearchNode implements Comparable<SearchNode> {
        private Board board;
        private int moves;
        private SearchNode previous;
        private int manhattanPriority;


        // 생성자
        public SearchNode(Board board, int moves, SearchNode previous) {
            this.board = board;
            this.moves = moves;
            this.previous = previous;
            this.manhattanPriority = board.manhattan() + moves; // Manhattan 거리 + 이동 횟수
        }

        public int compareTo(SearchNode that) {
            if (this.manhattanPriority < that.manhattanPriority)
                return -1;
            else if (this.manhattanPriority > that.manhattanPriority)
                return 1;
            else
                return 0;
        }
    }

    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        if (initial == null)
            throw new IllegalArgumentException("Board is null");

        MinPQ<SearchNode> minPQ = new MinPQ<>();
        MinPQ<SearchNode> minPQTwin = new MinPQ<>();

        minPQ.insert(new SearchNode(initial, 0, null));
        minPQTwin.insert(new SearchNode(initial.twin(), 0, null));

        SearchNode minNode;
        SearchNode minNodeTwin;

        while (!(minPQ.min().board.isGoal()) && !(minPQTwin.min().board.isGoal())) {
            minNode = minPQ.min();
            minNodeTwin = minPQTwin.min();
            minPQ.delMin();
            minPQTwin.delMin();

            for (Board neighbor : minNode.board.neighbors()) {
                if (minNode.previous == null || !(neighbor.equals(minNode.previous.board))) {
                    minPQ.insert(new SearchNode(neighbor, minNode.moves + 1, minNode));
                }
            }
            for (Board neighbor : minNodeTwin.board.neighbors()) {
                if (minNodeTwin.previous == null || !(neighbor.equals(minNodeTwin.previous.board))) {
                    minPQTwin.insert(new SearchNode(neighbor, minNodeTwin.moves + 1, minNodeTwin));
                }
            }
        }
        this.minSearchNode = minPQ.min();
    }

    // is the initial board solvable? (see below)
    public boolean isSolvable() {
        return minSearchNode.board.isGoal();
    }

    // min number of moves to solve initial board; -1 if unsolvable
    public int moves() {
        if (!isSolvable()) {
            return -1;
        } else {
            return minSearchNode.moves;
        }
    }

    // sequence of boards in a shortest solution; null if unsolvable
    public Iterable<Board> solution() {
        if (!isSolvable()) {
            return null;
        } else {
            ArrayList<Board> sequence = new ArrayList<>();
            SearchNode temp = minSearchNode;

            while (temp != null) {
                sequence.add(temp.board);
                temp = temp.previous;
            }

            Collections.reverse(sequence);

            return sequence;
        }
    }

    // test client (see below)
    public static void main(String[] args) {
        // create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}