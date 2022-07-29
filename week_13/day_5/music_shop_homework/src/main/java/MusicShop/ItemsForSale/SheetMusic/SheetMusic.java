package MusicShop.ItemsForSale.SheetMusic;

import MusicShop.ItemsForSale.ISell;
import MusicShop.ItemsForSale.ItemsForSale;

public abstract class SheetMusic extends ItemsForSale {
    private String title;
    private Publisher publisher;
    private String instrument;
    private int publicationYear;
    private SheetMusicType type;

    public SheetMusic(double boughtPrice, double salePrice, String title, Publisher publisher, String instrument, int publicationYear, SheetMusicType type) {
        super(boughtPrice, salePrice);
        this.title = title;
        this.publisher = publisher;
        this.instrument = instrument;
        this.publicationYear = publicationYear;
        this.type = type;
    }

    public String getTitle() {
        return title;
    }

    public Publisher getPublisher() {
        return publisher;
    }

    public String getInstrument() {
        return instrument;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    public SheetMusicType getType() {
        return type;
    }
}
