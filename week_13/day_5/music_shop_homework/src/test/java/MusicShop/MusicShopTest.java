package MusicShop;

import MusicShop.ItemsForSale.ISell;
import MusicShop.ItemsForSale.Instruments.Brass.Trumpet;
import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Keyboard.Piano;
import MusicShop.ItemsForSale.Instruments.Percussion.Marimba;
import MusicShop.ItemsForSale.Instruments.Strings.Viola;
import MusicShop.ItemsForSale.Instruments.Woodwind.Bassoon;
import MusicShop.ItemsForSale.SheetMusic.ABRSM;
import MusicShop.ItemsForSale.SheetMusic.ComposerCollections;
import MusicShop.ItemsForSale.SheetMusic.Publisher;
import MusicShop.ItemsForSale.SheetMusic.SheetMusicType;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class MusicShopTest {
    MusicShop musicShop;
    Trumpet trumpet;
    Piano piano;
    Marimba marimba;
    Viola viola;
    Bassoon bassoon;
    ABRSM abrsm;
    ComposerCollections composerCollection;

    @Before
    public void before() {
        trumpet = new Trumpet(InstrumentType.Brass, InstrumentMaker.Yamaha, "YTR2330", "Gold Lacquer", "Toot toot", "Bb", "Full-size", 300.00, 400.00);
        piano = new Piano(InstrumentType.Keyboard, InstrumentMaker.Kawai, "RX1", "Polished Mahogany", "Plinky plonky", "Grand Piano", 88, 1500.00, 1800.00);
        marimba = new Marimba(InstrumentType.Percussion, InstrumentMaker.WHD, "YM40", "African Paorosa", "Tonk tonk", 4, 400.00, 500.00);
        viola = new Viola(InstrumentType.Strings, InstrumentMaker.Amati, "Maggini", "Antiqued Varnished Wood", "Omgisntthisthemostbeautifulsoundyouveeverheard", 16, 2500.00, 3000.00);
        bassoon = new Bassoon(InstrumentType.Woodwind, InstrumentMaker.Selmer, "KA40", "Varnished Wood", "Honk honk", "Full-size", 1800.00, 2000.00);
        abrsm = new ABRSM(4.50, 7.50, "Grade 1 Scales", Publisher.ABRSM, "Piano", 2016, SheetMusicType.Scales, 1);
        composerCollection = new ComposerCollections(10.50, 15.50, "The Best of Bach", Publisher.BooseyAndHawkes, "Viola", 2008, SheetMusicType.Collection);
        musicShop = new MusicShop("Music Music Music");
    }

    @Test
    public void hasName() {
        assertEquals("Music Music Music", musicShop.getName());
    }

    @Test
    public void hasItemsForSaleList() {
        assertEquals(0, musicShop.getItemsForSale().size());
    }

    @Test
    public void canAddItemForSale() {
        musicShop.addItemForSale(trumpet);
        assertEquals(1, musicShop.getItemsForSale().size());
    }

    @Test
    public void canRemoveItemForSale () {
        musicShop.addItemForSale(piano);
        musicShop.addItemForSale(marimba);
        musicShop.removeItemForSale(marimba);
        assertEquals(1, musicShop.getItemsForSale().size());
    }

    @Test
    public void canCalculateItemMarkup() {
        musicShop.addItemForSale(piano);
        assertEquals(300.00, musicShop.getItemsForSale().get(0).calculateMarkup(), 0);
    }

    @Test
    public void canCalculateTotalMarkupOfAllItems() {
        musicShop.addItemForSale(trumpet);
        musicShop.addItemForSale(piano);
        musicShop.addItemForSale(marimba);
        musicShop.addItemForSale(viola);
        musicShop.addItemForSale(bassoon);
        musicShop.addItemForSale(abrsm);
        musicShop.addItemForSale(composerCollection);
        assertEquals(1208.00, musicShop.calculateTotalMarkup(), 0);
    }

}
