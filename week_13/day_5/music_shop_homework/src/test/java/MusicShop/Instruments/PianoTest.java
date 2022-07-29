package MusicShop.Instruments;
import MusicShop.ItemsForSale.Instruments.Brass.Trumpet;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Keyboard.Piano;
import org.junit.Before;
import org.junit.Test;

import javax.sound.midi.Instrument;

import static org.junit.Assert.assertEquals;

public class PianoTest {
    Piano piano;

    @Before
    public void before() {
        piano = new Piano(InstrumentType.Keyboard, InstrumentMaker.Kawai, "RX1", "Polished Mahogany", "Plinky plonky", "Grand Piano", 88, 1500.00, 1800.00);
    }

    @Test
    public void hasInstrumentType() {
        assertEquals(InstrumentType.Keyboard, piano.getInstrumentType());
    }

    @Test
    public void hasInstrumentMaker() {
        assertEquals(InstrumentMaker.Kawai, piano.getInstrumentMaker());
    }

    @Test
    public void hasModel() {
        assertEquals("RX1", piano.getModel());
    }

    @Test
    public void hasFinish() {
        assertEquals("Polished Mahogany", piano.getFinish());
    }

    @Test
    public void hasNoise() {
        assertEquals("Plinky plonky", piano.getInstrumentNoise());
    }

    @Test
    public void hasType() {
        assertEquals("Grand Piano", piano.getType());
    }

    @Test
    public void hasNumOfKeys() {
        assertEquals(88, piano.getNumOfKeys());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(1500.00, piano.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(1800.00, piano.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(300.00, piano.calculateMarkup(), 0);
    }

    @Test
    public void canPlay() {
        assertEquals("Plinky plonky", piano.play());
    }


}
