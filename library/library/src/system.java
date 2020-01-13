import java.util.*;

public class System{
    Scanner scanner = new Scanner(System.in);
    Client client_list[];
    Client now_logined = new Client();
    public void register(){ // When there's no clients registered, or typing "register".
        
        String input_name = scanner.nextLine();
        String input_birth = scanner.nextLine();
        String input_address = scanner.nextLine();
        String id = scanner.nextLine();
        String password = scanner.nextLine();
        
        Client new_client = new Client();
        new_client.setName(input_name);
        new_client.setBirth(input_birth);
        new_client.setAddress(input_address);
        new_client.id = id;
        new_client.password = password;
        //Adding Object information to client_list;
    }
    public void login(){
        int i=0; 
        String input_id = scanner.nextLine();
        String input_password = scanner.nextLine();
        
        //"for loop" to find the matching id
        //if there's a matching id, check password

        now_logined = client_list[i];
    }

    
    
}
