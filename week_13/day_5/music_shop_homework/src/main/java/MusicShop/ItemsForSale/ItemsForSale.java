package MusicShop.ItemsForSale;

public abstract class ItemsForSale implements ISell {

    private double boughtPrice;
    private double salePrice;

    public ItemsForSale(double boughtPrice, double salePrice) {
        this.boughtPrice = boughtPrice;
        this.salePrice = salePrice;
    }

    public double getBoughtPrice() {
        return boughtPrice;
    }

    public double getSalePrice() {
        return salePrice;
    }

    public double calculateMarkup() {
        return this.salePrice - this.boughtPrice;
    }
}
