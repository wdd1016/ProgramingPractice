import java.util.ArrayList;
import java.util.Arrays;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdDraw;

public class BruteCollinearPoints {
    private LineSegment[] lines;

    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        if (points == null)
            throw new IllegalArgumentException("argument to FastCollinearPoints constructor is null");

        for (Point pt : points) {
            if (pt == null) throw new IllegalArgumentException("argument to point is null");
        }

        Point[] copiedPoints = points.clone();
        Arrays.sort(copiedPoints);

        for (int i = 1; i < copiedPoints.length; i++) {
            if (copiedPoints[i - 1].equals(copiedPoints[i])) throw new IllegalArgumentException("copiedPoints are duplicated");
        }

        ArrayList<LineSegment> foundSegments = new ArrayList<>();
        for (int p = 0; p < copiedPoints.length - 3; p++) {
            for (int q = p + 1; q < copiedPoints.length - 2; q++) {
                for (int r = q + 1; r < copiedPoints.length - 1; r++) {
                    for (int s = r + 1; s < copiedPoints.length; s++) {
                        double pqSlope = copiedPoints[p].slopeTo(copiedPoints[q]);
                        double prSlope = copiedPoints[p].slopeTo(copiedPoints[r]);
                        double psSlope = copiedPoints[p].slopeTo(copiedPoints[s]);
                        if (pqSlope == prSlope && pqSlope == psSlope) {
                            foundSegments.add(new LineSegment(copiedPoints[p], copiedPoints[s]));
                        }
                    }
                }
            }
        }
        lines = foundSegments.toArray(new LineSegment[0]);
    }

    // the number of line segments
    public int numberOfSegments() { return lines.length; }

    // the line segments
    public LineSegment[] segments() { return lines.clone(); }

    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}