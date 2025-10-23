public class Student {
    int ID;
    String name;
    float cgpa;

    void showInfo(){
        System.out.println(ID);
        System.out.println(name);
        System.out.println(cgpa);
    }

    public Student(int ID, String name, float cgpa) {
        this.ID = ID;
        this.name = name;
        this.cgpa = cgpa;
    }
}
