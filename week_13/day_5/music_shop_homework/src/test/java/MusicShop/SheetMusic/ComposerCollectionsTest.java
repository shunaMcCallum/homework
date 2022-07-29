package MusicShop.SheetMusic;

import MusicShop.ItemsForSale.SheetMusic.ComposerCollections;
import MusicShop.ItemsForSale.SheetMusic.Publisher;
import MusicShop.ItemsForSale.SheetMusic.SheetMusicType;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ComposerCollectionsTest {
    ComposerCollections composerCollection;

    @Before
    public void before() {
        composerCollection = new ComposerCollections(10.50, 15.50, "The Best of Bach", Publisher.BooseyAndHawkes, "Viola", 2008, SheetMusicType.Collection);
    }

    @Test
    public void hasTitle() {
        assertEquals("The Best of Bach", composerCollection.getTitle());
    }

    @Test
    public void hasPublisher() {
        assertEquals(Publisher.BooseyAndHawkes, composerCollection.getPublisher());
    }

    @Test
    public void hasInstrument() {
        assertEquals("Viola", composerCollection.getInstrument());
    }

    @Test
    public void hasPublicationYear() {
        assertEquals(2008, composerCollection.getPublicationYear());
    }

    @Test
    public void hasType() {
        assertEquals(SheetMusicType.Collection, composerCollection.getType());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(10.50, composerCollection.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(15.50, composerCollection.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(5.00, composerCollection.calculateMarkup(), 0);
    }
}
