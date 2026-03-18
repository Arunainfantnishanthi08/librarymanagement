package util;

import model.Book;
import java.io.*;
import java.util.List;

public class FileUtil {

    private static final String FILE_NAME = "books.txt";

    public static void saveBooks(List<Book> books) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (Book b : books) {
                bw.write(b.toString());
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error saving books");
        }
    }

    public static void loadBooks(List<Book> books) {
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");
                books.add(new Book(
                        Integer.parseInt(data[0]),
                        data[1],
                        data[2]
                ));
            }
        } catch (IOException e) {
            System.out.println("No previous book data found");
        }
    }
}
