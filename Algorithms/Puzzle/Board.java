import java.util.ArrayList;
import edu.princeton.cs.algs4.StdOut;

public class Board {

    private int[][] tiles;
    private int     len;
    private int     hammingValue;
    private int     manhattanValue;

    // create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
        if (tiles == null || tiles[0] == null || tiles.length != tiles[0].length)
            return;

        this.len = tiles.length;
        this.tiles = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                this.tiles[i][j] = tiles[i][j];
            }
        }
        this.hammingValue = -1;
        this.manhattanValue = -1;
    }

    // string representation of this board
    public String toString() {
        StringBuilder str = new StringBuilder();

        str.append(len);
        str.append('\n');
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                str.append(' ');
                str.append(tiles[i][j]);
                if (j == len - 1)
                    str.append('\n');
                else
                    str.append(' ');
            }
        }
        return str.toString();
    }

    // board dimension n
    public int dimension() {
        return len;
    }

    // number of tiles out of place
    public int hamming() {
        if (hammingValue == -1) {
            hammingValue = 0;
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    if (tiles[i][j] != 0 && tiles[i][j] != i * len + j + 1)
                        hammingValue++;
                }
            }
        }
        return hammingValue;
    }

    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        if (manhattanValue == -1) {
            manhattanValue = 0;
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    if (tiles[i][j] != 0 && tiles[i][j] != i * len + j + 1) {
                        int correctRow = (tiles[i][j] - 1) / len;
                        int correctCol = (tiles[i][j] - 1) % len;
                        manhattanValue += Math.abs(i - correctRow) + Math.abs(j - correctCol);
                    }
                }
            }
        }
        return manhattanValue;
    }

    // is this board the goal board?
    public boolean isGoal() {
        return this.hamming() == 0;
    }

    // does this board equal y?
    public boolean equals(Object y) {
        if (y == this) return true;

        if (y == null || y.getClass() != this.getClass()) return false;

        // y를 Board 타입으로 캐스팅
        Board other = (Board) y;

        if (this.dimension() != other.dimension())
            return false;

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (this.tiles[i][j] != other.tiles[i][j])
                    return false;
            }
        }
        return true;
    }

    // all neighboring boards
    public Iterable<Board> neighbors() {
        ArrayList<Board> adjacency = new ArrayList<>();
        int correctRow = -1, correctCol = -1;

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (tiles[i][j] == 0) {
                    correctRow = i;
                    correctCol = j;
                    break;
                }
            }
            if (correctRow != -1) break;
        }
        if (correctRow == -1)
            return adjacency;

        int[][] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

        for (int[] direction : directions) {
            int newRow = correctRow + direction[0];
            int newCol = correctCol + direction[1];

            if (newRow >= 0 && newRow < len && newCol >= 0 && newCol < len) {
                Board newBoard = new Board(this.tiles);

                newBoard.tiles[correctRow][correctCol] = newBoard.tiles[newRow][newCol];
                newBoard.tiles[newRow][newCol] = 0;
                adjacency.add(newBoard);
            }
        }

        return adjacency;
    }

    // a board that is obtained by exchanging any pair of tiles
    public Board twin() {
        Board newBoard = new Board(this.tiles);

        int row1 = 0, col1 = 0, row2 = 1, col2 = 0;

        if (newBoard.tiles[row1][col1] == 0) {
            col1 = 1; // 첫 번째 타일이 빈 칸일 경우 두 번째 타일로 이동
        }

        if (newBoard.tiles[row2][col2] == 0) {
            col2 = 1; // 두 번째 타일이 빈 칸일 경우 다른 타일로 이동
        }

        int temp = newBoard.tiles[row1][col1];
        newBoard.tiles[row1][col1] = newBoard.tiles[row2][col2];
        newBoard.tiles[row2][col2] = temp;

        return newBoard;
    }

    // unit testing (not graded)
    public static void main(String[] args) {
        int[][] tiles = {
                {1, 2, 3},
                {0, 4, 6},
                {7, 5, 8}
        };
        Board board = new Board(tiles);
        StdOut.println("Current Board:");
        StdOut.println(board);

        StdOut.println("Hamming Distance: " + board.hamming());
        StdOut.println("Manhattan Distance: " + board.manhattan());

        StdOut.println("Is Goal: " + board.isGoal());

        StdOut.println("Neighbors:");
        for (Board neighbor : board.neighbors()) {
            StdOut.println(neighbor);
        }

        StdOut.println("Twin Board:");
        StdOut.println(board.twin());
    }
}