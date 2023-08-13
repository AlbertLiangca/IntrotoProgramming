import shop.Customer;

import java.util.Arrays;

public class HelloWorld {
    public static void main(String[] args) {
        Customer customer = new Customer();
        customer.setName("Albert");
        customer.setInterests(Arrays.asList("coding"));

        System.out.println(customer.getName() + " loves " + customer.getInterests().get(0));
    }
}