class PrintfEx1{
    public static void main(String[] args) {
        byte b = 1; 
        short s = 2; 
        char c = 'A';

        int finger = 10;
        long big = 100_000_000_000L; //suffix 'L' for long literal
        long hex = 0xFFFF_FFFF_FFFF_FFFFl;

        int octNum = 010;
        int hexNum = 0x10;
        int binNum = 0b10;

        System.out.printf("b = %d%n",b);
    }
}

/*
    println ==> automatically \n
    printf ==> can change data type 
*/