package MusicShop.ItemsForSale.Instruments.Strings;

import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Instruments;

public class Viola extends Instruments {

    private int size;

    public Viola(InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise, int size, double boughtPrice, double salePrice) {
        super(boughtPrice, salePrice, instrumentType, instrumentMaker, model, finish, instrumentNoise);
        this.size = size;
    }

    public int getSize() {
        return size;
    }
}
