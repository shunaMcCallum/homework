package MusicShop.SheetMusic;

import MusicShop.ItemsForSale.SheetMusic.ABRSM;
import MusicShop.ItemsForSale.SheetMusic.Publisher;
import MusicShop.ItemsForSale.SheetMusic.SheetMusicType;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ABRSMTest {
    ABRSM abrsm;

    @Before
    public void before() {
        abrsm = new ABRSM(4.50, 7.50, "Grade 1 Scales", Publisher.ABRSM, "Piano", 2016, SheetMusicType.Scales, 1);
    }

    @Test
    public void hasTitle() {
        assertEquals("Grade 1 Scales", abrsm.getTitle());
    }

    @Test
    public void hasPublisher() {
        assertEquals(Publisher.ABRSM, abrsm.getPublisher());
    }

    @Test
    public void hasInstrument() {
        assertEquals("Piano", abrsm.getInstrument());
    }

    @Test
    public void hasPublicationYear() {
        assertEquals(2016, abrsm.getPublicationYear());
    }

    @Test
    public void hasType() {
        assertEquals(SheetMusicType.Scales, abrsm.getType());
    }

    @Test
    public void hasGrade() {
        assertEquals(1, abrsm.getGrade());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(4.50, abrsm.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(7.50, abrsm.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(3.00, abrsm.calculateMarkup(), 0);
    }
}
