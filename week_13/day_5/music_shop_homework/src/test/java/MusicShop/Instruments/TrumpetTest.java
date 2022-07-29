package MusicShop.Instruments;
import MusicShop.ItemsForSale.Instruments.Brass.Trumpet;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TrumpetTest {
    Trumpet trumpet;

    @Before
    public void before() {
        trumpet = new Trumpet(InstrumentType.Brass, InstrumentMaker.Yamaha, "YTR2330", "Gold Lacquer", "Toot toot", "Bb", "Full-size", 300.00, 400.00);
    }

    @Test
    public void hasInstrumentType() {
        assertEquals(InstrumentType.Brass, trumpet.getInstrumentType());
    }

    @Test
    public void hasInstrumentMaker() {
        assertEquals(InstrumentMaker.Yamaha, trumpet.getInstrumentMaker());
    }

    @Test
    public void hasModel() {
        assertEquals("YTR2330", trumpet.getModel());
    }

    @Test
    public void hasFinish() {
        assertEquals("Gold Lacquer", trumpet.getFinish());
    }

    @Test
    public void hasNoise() {
        assertEquals("Toot toot", trumpet.getInstrumentNoise());
    }

    @Test
    public void hasType() {
        assertEquals("Bb", trumpet.getType());
    }

    @Test
    public void hasSize() {
        assertEquals("Full-size", trumpet.getSize());
    }

    @Test
    public void hasBoughtPrice() {
        assertEquals(300.00, trumpet.getBoughtPrice(), 0);
    }

    @Test
    public void hasSalePrice() {
        assertEquals(400.00, trumpet.getSalePrice(), 0);
    }

    @Test
    public void canCalculateMarkup() {
        assertEquals(100.00, trumpet.calculateMarkup(), 0);
    }

    @Test
    public void canPlay() {
        assertEquals("Toot toot", trumpet.play());
    }

}
