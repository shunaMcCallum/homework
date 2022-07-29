package MusicShop.Instruments;

import MusicShop.ItemsForSale.Instruments.Brass.Trumpet;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Strings.Viola;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ViolaTest {
    Viola viola;

    @Before
    public void before() {
        viola = new Viola(InstrumentType.Strings, InstrumentMaker.Amati, "Maggini", "Antiqued Varnished Wood", "Omgisntthisthemostbeautifulsoundyouveeverheard", 16, 2500.00, 3000.00);
    }

    @Test
    public void hasInstrumentType() {
        assertEquals(InstrumentType.Strings, viola.getInstrumentType());
    }

    @Test
    public void hasInstrumentMaker() {
        assertEquals(InstrumentMaker.Amati, viola.getInstrumentMaker());
    }

    @Test
    public void hasModel() {
        assertEquals("Maggini", viola.getModel());
    }

    @Test
    public void hasFinish() {
        assertEquals("Antiqued Varnished Wood", viola.getFinish());
    }

    @Test
    public void hasNoise() {
        assertEquals("Omgisntthisthemostbeautifulsoundyouveeverheard", viola.getInstrumentNoise());
    }

    @Test
    public void hasSize() {
        assertEquals(16, viola.getSize());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(2500.00, viola.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(3000.00, viola.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(500.00, viola.calculateMarkup(), 0);
    }

    @Test
    public void canPlay() {
        assertEquals("Omgisntthisthemostbeautifulsoundyouveeverheard", viola.play());
    }
}
