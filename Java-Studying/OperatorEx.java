
class operatorex{
    public static void main(String[] args) {
        int dec = -8;
        System.out.printf("%s\t %d << %d = %d \t%s%n",toBinaryString(dec),dec,2,dec<<2,toBinaryString(dec << 2));

    }

    static String toBinaryString(int x)
    {
        String zero = "0000000000000000000000000000";
        String tmp = zero + Integer.toBinaryString(x);
        return tmp.substring(tmp.length()-32);
    }
}