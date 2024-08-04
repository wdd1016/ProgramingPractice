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
        ArrayList<Point> foundEndPoints = new ArrayList<>();
        ArrayList<Double> foundSlopes = new ArrayList<>();
        for (int i = 0; i < copiedPoints.length - 3; i++) {
            Point basePoint = copiedPoints[i];
            Point[] aroundPoints = Arrays.copyOfRange(copiedPoints, i + 1, copiedPoints.length);
            double[] aroundSlopes = new double[aroundPoints.length];
            Comparator<Point> comparator = basePoint.slopeOrder();

            Arrays.sort(aroundPoints, comparator);
            for (int j = 0; j < aroundPoints.length; j++) {
                aroundSlopes[j] = basePoint.slopeTo(aroundPoints[j]);
            }

            int count = 0;
            for (int j = 0; j < aroundPoints.length - 1; j++) {
                count++;
                if (aroundSlopes[j] != aroundSlopes[j + 1]) {
                    if (count >= 3) {
                        foundSegments.add(new LineSegment(basePoint, aroundPoints[j]));
                        foundEndPoints.add(aroundPoints[j]);
                        foundSlopes.add(aroundSlopes[j]);
                    }
                count = 0;
                }
            }
            if (count >= 2) {
                foundSegments.add(new LineSegment(basePoint, aroundPoints[aroundPoints.length - 1]));
                foundEndPoints.add(aroundPoints[aroundPoints.length - 1]);
                foundSlopes.add(aroundSlopes[aroundPoints.length - 1]);
            }
        }

        ArrayList<Integer> indices = new ArrayList<>();
        for (int i = 0; i < foundSegments.size(); i++) indices.add(i);

        indices.sort((x, y) -> {
                    int slopeComparison = Double.compare(foundSlopes.get(x), foundSlopes.get(y));
                    if (slopeComparison != 0) {
                        return slopeComparison;
                    } else {
                        return foundEndPoints.get(x).compareTo(foundEndPoints.get(y));
                    }
                });

        ArrayList<LineSegment> sortedSegments = new ArrayList<>();
        ArrayList<Point> sortedEndPoints = new ArrayList<>();
        ArrayList<Double> sortedSlopes = new ArrayList<>();
        for (int index : indices) {
            sortedSegments.add(foundSegments.get(index));
            sortedEndPoints.add(foundEndPoints.get(index));
            sortedSlopes.add(foundSlopes.get(index));
        }

        ArrayList<LineSegment> finalSegments = new ArrayList<>();

        if (sortedSegments.size() > 0) finalSegments.add(sortedSegments.get(0));
        for (int i = 1; i < sortedSegments.size(); i++) {
            if (Double.compare(sortedSlopes.get(i), sortedSlopes.get(i - 1)) != 0
                    || sortedEndPoints.get(i).compareTo(sortedEndPoints.get(i - 1)) != 0) {
                finalSegments.add(sortedSegments.get(i));
            }
        }

        lines = finalSegments.toArray(new LineSegment[0]);
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