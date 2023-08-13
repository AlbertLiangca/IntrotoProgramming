package shop;

import java.util.ArrayList;

public class Variables {
    public static void main(String[] args) {
        int age = 30;
        String name = "Albert";
        Address address = new Address("main street", "123a");
        Customer customer = new Customer(name, new ArrayList<>(), address);

        System.out.println("before: " + age);
        changeInt(age);
        System.out.println("after: " + age);

        System.out.println("before: " + customer.getName());
        changeCustomer(customer);
        System.out.println("after: " + customer.getName());


    }

    public static void changeInt(int x) {
        x = 5;
    }

    public static void changeCustomer(Customer c) {
        c.setName("Els");
    }
}
