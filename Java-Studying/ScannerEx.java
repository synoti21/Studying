import java.util.*;

class ScannerEx{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("두자리 정수를 입력해주세요.>");
        String input = scanner.nextLine();
        int num = Integer.parseInt(input); //parseInt -> String 타입인 input을 정수형으로 바꿔준다. 

        System.out.println("입력내용 :" + input);
        System.out.printf("num = %d%n",num);
    }

}