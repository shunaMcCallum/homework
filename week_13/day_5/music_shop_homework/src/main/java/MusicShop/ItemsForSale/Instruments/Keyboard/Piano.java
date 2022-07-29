package MusicShop.ItemsForSale.Instruments.Keyboard;

import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Instruments;

public class Piano extends Instruments {
    private String type;
    private int numOfKeys;

    public Piano(InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise, String type, int numOfKeys, double boughtPrice, double salePrice) {
        super(boughtPrice, salePrice, instrumentType, instrumentMaker, model, finish, instrumentNoise);
        this.type = type;
        this.numOfKeys = numOfKeys;
    }

    public String getType() {
        return type;
    }

    public int getNumOfKeys() {
        return numOfKeys;
    }
}
