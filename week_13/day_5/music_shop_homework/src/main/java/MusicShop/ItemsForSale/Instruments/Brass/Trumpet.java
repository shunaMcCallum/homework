package MusicShop.ItemsForSale.Instruments.Brass;

import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Instruments;

public class Trumpet extends Instruments {
    private String type;
    private String size;

    public Trumpet(InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise, String type, String size, double boughtPrice, double salePrice) {
        super(boughtPrice, salePrice, instrumentType, instrumentMaker, model, finish, instrumentNoise);
        this.type = type;
        this.size = size;
    }

    public String getType() {
        return type;
    }

    public String getSize() {
        return size;
    }

}
