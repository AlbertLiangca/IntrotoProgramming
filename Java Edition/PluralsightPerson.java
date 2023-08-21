public class PluralsightPerson {

    private String name;
    private int age = 25;

    public PluralsightPerson(String name, int age) {
        setAge(age);
        setName(name);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age < 18 || age > 65) {
            throw new IllegalArgumentException("Age is not between 18 and 65.");
        }

        this.age = age;

    }

}
