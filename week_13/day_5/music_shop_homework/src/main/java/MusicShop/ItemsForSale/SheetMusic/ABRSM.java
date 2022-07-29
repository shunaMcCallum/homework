package MusicShop.ItemsForSale.SheetMusic;

public class ABRSM extends SheetMusic {

    private int grade;

    public ABRSM(double boughtPrice, double salePrice, String title, Publisher publisher, String instrument, int publicationYear, SheetMusicType type, int grade) {
        super(boughtPrice, salePrice, title, publisher, instrument, publicationYear, type);
        this.grade = grade;
    }

    public int getGrade() {
        return grade;
    }
}
