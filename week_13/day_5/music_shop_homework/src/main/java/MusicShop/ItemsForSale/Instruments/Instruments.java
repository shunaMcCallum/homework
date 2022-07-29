package MusicShop.ItemsForSale.Instruments;

import MusicShop.ItemsForSale.ItemsForSale;

public abstract class Instruments extends ItemsForSale implements IPlay {
    private InstrumentType instrumentType;
    private InstrumentMaker instrumentMaker;
    private String model;
    private String finish;
    private String instrumentNoise;

    public Instruments(double boughtPrice, double salePrice, InstrumentType instrumentType, InstrumentMaker instrumentMaker, String model, String finish, String instrumentNoise) {
        super(boughtPrice, salePrice);
        this.instrumentType = instrumentType;
        this.instrumentMaker = instrumentMaker;
        this.model = model;
        this.finish = finish;
        this.instrumentNoise = instrumentNoise;
    }

    public String play() {
        return this.instrumentNoise;
    }

    public InstrumentType getInstrumentType() {
        return instrumentType;
    }

    public InstrumentMaker getInstrumentMaker() {
        return instrumentMaker;
    }

    public String getModel() {
        return model;
    }

    public String getFinish() {
        return finish;
    }

    public String getInstrumentNoise() {
        return instrumentNoise;
    }
}
