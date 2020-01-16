class varex1{
    public static void main(String[] args) {
        int year = 0 ; 
        int age = 14;
        
        final int CONSTANT = 2; //this cannot be modified
        //in C language, this is similar to #define CONSTANT = 100.


        System.out.println(age); //SuperClass System -> extends out class -> println(line) method(parameter)
        System.out.println(year);

        year = age + 100;
        age = year + 35;

        System.out.println(year);
        System.out.println(age);
        System.out.println(CONSTANT);
    }
}

/*
    literal type :

    float num1 = 3.14'f';
    float num2 = 3.14; (x) ==> double type literal cannot be assigned to float

    int num3 = 0x1234543534; (x) ==> overflowed
    double num4 = 3.14f (o) ==> smaller range than double

    
*/