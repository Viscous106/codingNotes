
import java.io.IOException;
public class Demo {
    public static void main(String[] args) throws IOException {
        BookRepo repo = new BookRepo("docs/CSVs/Download CSV File - Sheet1.csv");
        repo.printTitlesOFAllbooks();
    }
}
