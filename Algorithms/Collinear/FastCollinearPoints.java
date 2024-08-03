import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdDraw;

public class FastCollinearPoints {
    private LineSegment[] lines;

    // finds all line segments containing 4 or more points
    public FastCollinearPoints(Point[] points) {
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
        ArrayList<Point> foundStartPoints = new ArrayList<>();
        for (int i = 0; i < copiedPoints.length - 3; i++) {
            Point basePoint = copiedPoints[i];
            Point[] aroundPoints = Arrays.copyOfRange(copiedPoints, i + 1, copiedPoints.length);
            Comparator<Point> comparator = basePoint.slopeOrder();

            Arrays.sort(aroundPoints, comparator);
            int count = 1;
            for (int j = 0; j < aroundPoints.length; j++) {
                if (j == aroundPoints.length - 1) {
                    if (count >= 3) {
                        int k;
                        for (k = 0; k < foundStartPoints.size(); k++) {
                            Point pt = foundStartPoints.get(k);
                            if (pt.slopeTo(basePoint) == pt.slopeTo(aroundPoints[j])) break;
                        }
                        if (k == foundStartPoints.size()) {
                            foundSegments.add(new LineSegment(basePoint, aroundPoints[j]));
                            foundStartPoints.add(basePoint);
                        }
                    }
                } else if (basePoint.slopeTo(aroundPoints[j]) == basePoint.slopeTo(aroundPoints[j + 1])) {
                    count++;
                } else {
                    if (count >= 3) {
                        int k;
                        for (k = 0; k < foundStartPoints.size(); k++) {
                            Point pt = foundStartPoints.get(k);
                            if (pt.slopeTo(basePoint) == pt.slopeTo(aroundPoints[j])) break;
                        }
                        if (k == foundStartPoints.size()) {
                            foundSegments.add(new LineSegment(basePoint, aroundPoints[j]));
                            foundStartPoints.add(basePoint);
                        }
                    }
                count = 1;
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
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}