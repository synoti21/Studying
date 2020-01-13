public class Client{
    String birth, address, name;
    String id,password;
    public static int clients = 0;
    
    setName(String input_name)
    {
        this.name = input_name;
    }
    setBirth(String input_birth)
    {
        this.birth = input_birth;
    }
    setAddress(String input_address)
    {
        this.address = input_address;
    }

    client()
    {
        clients++;
    }


}

/*
    손님의 기능 ; 
    1) 각 손님의 정보를 가지고 있다.
    2) 총 손님의 수에 대한 정보를 가지고 있다. 
*/