package shop;

public class Scope {
    public static void main(String[] args) {
        int x = 7;
        if (x < 4) {
            System.out.println(x);
            int y = 8;
            System.out.println(y);
            if (y < 10) {
                System.out.println(x + y);
            }
        }
    }
}
