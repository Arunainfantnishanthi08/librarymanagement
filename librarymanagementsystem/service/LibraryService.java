package service;

import model.Book;
import java.util.ArrayList;
import java.util.List;

public class LibraryService {
    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
        System.out.println("Book added");
    }

    public void viewBooks() {
        if (books.isEmpty()) {
            System.out.println("No books available");
            return;
        }
        for (Book b : books) {
            System.out.println(b.getId() + " " + b.getTitle() + " " + b.getAuthor());
        }
    }

    public List<Book> getBooks() {
        return books;
    }
}
