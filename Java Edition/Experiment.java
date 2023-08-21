public class Experiment extends CompareR {
    public static void main(String[] args) {
    Circle [] circles = {new Circle(14),new Circle(4),new Circle(1),new Circle(22),new Circle(13),new Circle(9)};
    sortCircles(circles);
    for(int i = 0; i < circles.length; i ++) {
        System.out.println(circles[i].getRadius());
    }
}
}
