package MusicShop.ItemsForSale.Instruments.Percussion;

import MusicShop.ItemsForSale.Instruments.InstrumentMaker;
import MusicShop.ItemsForSale.Instruments.InstrumentType;
import MusicShop.ItemsForSale.Instruments.Instruments;

public class Marimba extends Instruments {
    private int octaves;

    public Marimba(InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise, int octaves, double boughtPrice, double salePrice) {
        super(boughtPrice, salePrice, instrumentType, instrumentMaker, model, finish, instrumentNoise);
        this.octaves = octaves;
    }

    public int getOctaves() {
        return octaves;
    }

}
