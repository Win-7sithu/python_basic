class Human
{
    private String name;
    
    public Human(String name)
    {
        this.name = name;
        //System.out.println("Human Constructor.");
        
    }

    public void work()
    {
        System.out.println("Human "+this.name+" works.");
    }

}  

class Doctor extends Human
{
    private String medicalField;
    public Doctor(String name, String medicalField)
    {
        super(name);
        this.medicalField = medicalField;
        //System.out.println("Doctor Constructor!");
    }
    public void work()
    {
        System.out.println("Doctor works "+ " in "+ this.medicalField);
    }
}
class Teacher extends Human
{
    private String school;
    public Teacher(String name, String school)
    {
        super(name);
        this.school = school;

        //System.out.println("Teacher Constructor!");
    }
    public void work()
    {
        System.out.println("Teacher teaches at " + this.school);
    }

}

public class inheritance 
{
    public static void main(String []args)
    {
        Human h = new Doctor("Tint Shwe", "Heart");
        h.work();
        h = new Teacher("Nyein", "BEHS.PG");
        h.work();

    }

}
