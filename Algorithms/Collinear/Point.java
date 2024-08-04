import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;

public class Point implements Comparable<Point> {
    private final int x;
    private final int y;

    // constructs the point (x, y)
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // draws this point
    public void draw() {
        StdDraw.point(x, y);
    }

    // draws the line segment from this point to that point
    public void drawTo(Point that) {
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // string representation
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    // compare two points by y-coordinates, breaking ties by x-coordinates
    public int compareTo(Point that) {
        if (this.y < that.y) return -1;
        else if (this.y > that.y) return 1;
        else if (this.x < that.x) return -1;
        else if (this.x > that.x) return 1;
        else return 0;
    }

    // the slope between this point and that point
    public double slopeTo(Point that) {
        if (this.x == that.x) {
            if (this.y == that.y) return Double.NEGATIVE_INFINITY;
            else return Double.POSITIVE_INFINITY;
        }
        else if (this.y == that.y) return 0.0;
        return ((double) (that.y - this.y) / (that.x - this.x));
    }

    // compare two points by slopes they make with this point
    public Comparator<Point> slopeOrder() {
        return new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                double slope1 = slopeTo(o1);
                double slope2 = slopeTo(o2);

                if (slope1 < slope2) return -1;
                else if (slope1 > slope2) return 1;
                else return 0;
            }
        };
    }

    // Unit tests the Point data type.
    public static void main(String[] args) {
        /* YOUR CODE HERE */
    }
}