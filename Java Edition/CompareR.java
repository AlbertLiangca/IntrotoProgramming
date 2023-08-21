public class CompareR {
    public static void sortCircles(Circle[] circles) {

        for (int i = 0; i < circles.length; i++) {
            for (int j = i; j < circles.length; j++) {
                if (circles[i].compareTo(circles[j]) > 0) {
                    Circle tempcircle = new Circle(circles[j].getRadius());
                    circles[j] = circles[i];
                    circles[i] = tempcircle;
                }
            }
        }
    }
}

class Circle {
    private float radius;

    public Circle(float r) {
        if (r >= 0)
            radius = r;
        else
            radius = 1;
    }

    public float getRadius() {
        return radius;
    }

    public int compareTo(Circle c) {
        if (radius == c.radius)
            return 0;
        else if (radius < c.radius)
            return -1;
        else
            return 1;
    }
}
