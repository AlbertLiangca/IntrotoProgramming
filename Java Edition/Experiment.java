public class Experiment {
    public static void main(String[] args){
        
        int x = Integer.parseInt(args[0]);

        for (int i = 0; i <= x; i++) {
            String output = "";
            if (i % 3 == 0) {
                output += "Fizz";
            }
            if (i % 5 == 0) {
                output += "Buzz";
            }
            if (output == "") {
                output += Integer.toString(i);
            }
            System.out.println(output);
        }
    }
}
