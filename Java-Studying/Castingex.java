class Castingex{
    public static void main(String[] args) {
        float f = 9.1234567f;
        double d = 9.1234567;
        double d2 = (double)f; //casting float type 'f' to double type. Casting 9.1234567f to float ==>
        // already casted so this doesn't mean anything. 

        System.out.printf("f = %20.18f\n",f);
        System.out.printf("d = %20.18f\n",d);
        System.out.printf("d2 = %20.18f\n",d2); // casting "double" type d to "float" type.
        //the range of double is larger than float.
    }
}