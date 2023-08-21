

public class Point {
    double x;
    double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public int compareTo(Point c) {
        if (Math.sqrt(this.x*this.x + this.y*this.y) == Math.sqrt(c.x*c.x + c.y*c.y)) {
            return 0;
        }
        else if (Math.sqrt(this.x*this.x + this.y*this.y) < Math.sqrt(c.x*c.x + c.y*c.y)) {
            return -1;
        }
        else return 1;

    }
}
