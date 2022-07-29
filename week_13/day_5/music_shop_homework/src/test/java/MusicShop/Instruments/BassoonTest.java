package MusicShop.Instruments;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Woodwind.Bassoon;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BassoonTest {
    Bassoon bassoon;

    @Before
    public void before() {
        bassoon = new Bassoon(InstrumentType.Woodwind, InstrumentMaker.Selmer, "KA40", "Varnished Wood", "Honk honk", "Full-size", 1800.00, 2000.00);
    }

    @Test
    public void hasInstrumentType() {
        assertEquals(InstrumentType.Woodwind, bassoon.getInstrumentType());
    }

    @Test
    public void hasInstrumentMaker() {
        assertEquals(InstrumentMaker.Selmer, bassoon.getInstrumentMaker());
    }

    @Test
    public void hasModel() {
        assertEquals("KA40", bassoon.getModel());
    }

    @Test
    public void hasFinish() {
        assertEquals("Varnished Wood", bassoon.getFinish());
    }

    @Test
    public void hasNoise() {
        assertEquals("Honk honk", bassoon.getInstrumentNoise());
    }

    @Test
    public void hasSize() {
        assertEquals("Full-size", bassoon.getSize());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(1800.00, bassoon.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(2000.00, bassoon.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(200.00, bassoon.calculateMarkup(), 0);
    }

    @Test
    public void canPlay() {
        assertEquals("Honk honk", bassoon.play());
    }
}
