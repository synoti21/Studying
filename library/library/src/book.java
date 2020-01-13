public class Book{
    String isbn, author, title;
    boolean isLent;
    Client lentClient = new Client();

    public void lent(Client lendingClient) {
        lentClient = lendingClient;
        System.out.println("Lent Successfully");
    }
    
}