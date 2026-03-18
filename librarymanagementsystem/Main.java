import model.Book;
import service.LibraryService;
import util.FileUtil;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LibraryService service = new LibraryService();
        FileUtil.loadBooks(service.getBooks());

        int choice;
        do {
            System.out.println("1.Add Book 2.View Books 3.Exit");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("ID: ");
                    int id = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Title: ");
                    String title = sc.nextLine();
                    System.out.print("Author: ");
                    String author = sc.nextLine();
                    service.addBook(new Book(id, title, author));
                    break;
                case 2:
                    service.viewBooks();
                    break;
                case 3:
                    FileUtil.saveBooks(service.getBooks());
            }
        } while (choice != 3);
    }
}
