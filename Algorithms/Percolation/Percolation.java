import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
  private WeightedQuickUnionUF quickUnionAll;
  private WeightedQuickUnionUF quickUnionTop;
  private boolean[][] percolationMap;
  private int numOfOpenSites;
  private int num;
  private int virtualTop;
  private int virtualBottom;
  // creates n-by-n grid, with all sites initially blocked
  public Percolation(int n) {
    if (n <= 0)
      throw new IllegalArgumentException("n must be a natural number.");
    quickUnionAll = new WeightedQuickUnionUF(n * n + 2);
    quickUnionTop = new WeightedQuickUnionUF(n * n + 2);
    percolationMap = new boolean[n + 1][n + 1];
    numOfOpenSites = 0;
    num = n;
    virtualTop = n * n;
    virtualBottom = n * n + 1;
    for (int i = 0; i < n; i++) {
      quickUnionAll.union(virtualTop, i);
      quickUnionTop.union(virtualTop, i);
      quickUnionAll.union(virtualBottom, n * (n - 1) + i);
    }
  }

  // opens the site (row, col) if it is not open already
  public void open(int row, int col) {
    if (row < 1 || col < 1 || row > num || col > num)
      throw new IllegalArgumentException("row & col are not between 1 and " + num);
    if (!percolationMap[row][col]) {
      percolationMap[row][col] = true;
      numOfOpenSites++;
      if (row + 1 <= num && isOpen(row + 1, col)) {
        quickUnionAll.union(coorToIdx(row, col), coorToIdx(row + 1, col));
        quickUnionTop.union(coorToIdx(row, col), coorToIdx(row + 1, col));
      }
      if (row - 1 > 0 && isOpen(row - 1, col)) {
        quickUnionAll.union(coorToIdx(row, col), coorToIdx(row - 1, col));
        quickUnionTop.union(coorToIdx(row, col), coorToIdx(row - 1, col));
      }
      if (col + 1 <= num && isOpen(row, col + 1)) {
        quickUnionAll.union(coorToIdx(row, col), coorToIdx(row, col + 1));
        quickUnionTop.union(coorToIdx(row, col), coorToIdx(row, col + 1));
      }
      if (col - 1 > 0 && isOpen(row, col - 1)) {
        quickUnionAll.union(coorToIdx(row, col), coorToIdx(row, col - 1));
        quickUnionTop.union(coorToIdx(row, col), coorToIdx(row, col - 1));
      }
    }
  }

  // is the site (row, col) open?
  public boolean isOpen(int row, int col) {
    if (row < 1 || col < 1 || row > num || col > num)
      throw new IllegalArgumentException("row & col are not between 1 and " + num);
    return percolationMap[row][col];
  }

  // is the site (row, col) full?
  public boolean isFull(int row, int col) {
    if (isOpen(row, col))
      return (quickUnionTop.find(virtualTop) == quickUnionTop.find(coorToIdx(row, col)));
    else
      return false;
  }

  // returns the number of open sites
  public int numberOfOpenSites() {
    return numOfOpenSites;
  }

  // does the system percolate?
  public boolean percolates() {
    if (num == 1)
      return percolationMap[1][1];
    else
      return (quickUnionAll.find(virtualTop) == quickUnionAll.find(virtualBottom));
  }

  private int coorToIdx(int row, int col) {
    return ((row - 1) * num + (col - 1));
  }

  // test client (optional)
  public static void main(String[] args) {
    int n = 1;

    Percolation percolation = new Percolation(n);

    while (true) {
      int row = StdRandom.uniformInt(1, n + 1);
      int col = StdRandom.uniformInt(1, n + 1);
      percolation.open(row, col);
      if (percolation.percolates()) {
        double percolationThreshold = (double) percolation.numberOfOpenSites() / (n * n);
        System.out.println(percolationThreshold);
        break;
      }
    }
  }
}