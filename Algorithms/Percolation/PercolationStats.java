import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private static final double CONFIDENCE_95 = 1.96;

    private double[] percolationThreshold;
    private int trialCounts;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0)
            throw new IllegalArgumentException("n & trials must be a natural number.");
        percolationThreshold = new double[trials];
        trialCounts = trials;

        for (int i = 0; i < trials; i++) {
            Percolation percolation = new Percolation(n);
            while (true) {
                percolation.open(StdRandom.uniformInt(1, n + 1), StdRandom.uniformInt(1, n + 1));
                if (percolation.percolates()) {
                    percolationThreshold[i] = (double) percolation.numberOfOpenSites() / (n * n);
                    break;
                }
            }
        }
    }
    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(percolationThreshold);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(percolationThreshold);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() { return this.mean() - CONFIDENCE_95 * this.stddev() / Math.sqrt(trialCounts); }

    // high endpoint of 95% confidence interval
    public double confidenceHi() { return this.mean() + CONFIDENCE_95 * this.stddev() / Math.sqrt(trialCounts); }

    // test client (see below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats percolationStats = new PercolationStats(n, trials);

        System.out.printf("%-24s = %.16f\n", "mean", percolationStats.mean());
        System.out.printf("%-24s = %.16f\n", "stddev", percolationStats.stddev());
        System.out.printf("%-24s = [%.16f, %.16f]\n", "95% confidence interval", percolationStats.confidenceLo(), percolationStats.confidenceHi());

    }

}
