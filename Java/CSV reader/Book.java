public class Book {
    String title;
    String author;
    double ratings;
    int reviews;
    int year;
    String genre;
    int price;

    public Book(String title, String author, double ratings, int reviews, int price, int year, String genre){
        this.title = title;
        this.ratings = ratings;
        this.author = author;
        this.price = price;
        this.reviews = reviews;
        this.year = year;
        this.genre = genre;
    }


}
