public class PluralsightVar {
    public static void main(String[] args) {
       boolean isWorking = false;

       System.out.println(isWorking);
       
       PluralsightPerson person = new PluralsightPerson("Joe",45);

       System.out.println(person.getAge());
       person.setAge(30);
       System.out.println(person.getAge());

       Integer a = new Integer(10);
       Integer b = 10;

       int a1 = 10;
       int b1 = 10;

       System.out.println((a.intValue() == b.intValue()));
       System.out.println(a1 == b1);



    }
}
