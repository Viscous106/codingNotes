
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

    //load the data
    //path 
    //open the file
    //read it line by line
    //split the line 
    //[India, Aditya Kumar Rai, 4.0, 20, 2023, 100, Fiction]
    //get values of all attributes
    // title = val[1];
    //create object of book
    //add this to an arraylist
    //ArrayList<Book> list <<book1> <book2> <book3>...>

public class CSVDataLoader {
    String filePath;
    public CSVDataLoader(String filePath){
        this.filePath = filePath;
    }
    public ArrayList<Book> loadBookList() throws FileNotFoundException, IOException{
        ArrayList<Book> bookList = new ArrayList<Book>();
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        br.readLine();
        String line;
        while((line = br.readLine()) != null){
            String[] values = line.split(",");
            String title = values[0];
            String author = values[1];
            double ratings = Double.parseDouble(values[2]);
            int reviews = Integer.parseInt(values[3]);
            int price = Integer.parseInt(values[4]);
            int year = Integer.parseInt(values[5]);
            String genre = values[6];
            Book book = new Book(title, author, ratings, reviews, price, year, genre);
            bookList.add(book);


        }
        return bookList;


    }

    }
