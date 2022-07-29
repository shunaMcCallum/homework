package MusicShop.ItemsForSale.Instruments.Woodwind;

import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Instruments;

public class Bassoon extends Instruments {
    private String size;

    public Bassoon(InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise, String size, double boughtPrice, double salePrice) {
        super(boughtPrice, salePrice, instrumentType, instrumentMaker, model, finish, instrumentNoise);
        this.size = size;
    }

    public String getSize() {
        return size;
    }
}
