package MusicShop.Instruments;

import MusicShop.ItemsForSale.Instruments.Brass.Trumpet;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Percussion.Marimba;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class MarimbaTest {
    Marimba marimba;

    @Before
    public void before() {
        marimba = new Marimba(InstrumentType.Percussion, InstrumentMaker.WHD, "YM40", "African Paorosa", "Tonk tonk", 4, 400.00, 500.00);
    }

    @Test
    public void hasInstrumentType() {
        assertEquals(InstrumentType.Percussion, marimba.getInstrumentType());
    }

    @Test
    public void hasInstrumentMaker() {
        assertEquals(InstrumentMaker.WHD, marimba.getInstrumentMaker());
    }

    @Test
    public void hasModel() {
        assertEquals("YM40", marimba.getModel());
    }

    @Test
    public void hasFinish() {
        assertEquals("African Paorosa", marimba.getFinish());
    }

    @Test
    public void hasNoise() {
        assertEquals("Tonk tonk", marimba.getInstrumentNoise());
    }

    @Test
    public void hasOctaves() {
        assertEquals(4, marimba.getOctaves());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(400.00, marimba.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(500.00, marimba.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(100.00, marimba.calculateMarkup(), 0);
    }

    @Test
    public void canPlay() {
        assertEquals("Tonk tonk", marimba.play());
    }
}
