import java.io.IOException;
import java.util.ArrayList;

public class BookRepo {
    ArrayList<Book> bookList;

    public BookRepo(String filePath) throws IOException{
        CSVDataLoader ld = new CSVDataLoader(filePath);
        bookList = ld.loadBookList();

    }
    public void printTitlesOFAllbooks(){
        for(int i=0; i<bookList.size(); i++){
            System.out.println(bookList.get(i).title);
        }
    }
  /*
    Implement all your functions here
  */
    
}
