package MusicShop;

import MusicShop.ItemsForSale.ISell;

import java.util.ArrayList;

public class MusicShop {
    private ArrayList<ISell> itemsForSale;
    private String name;

    public MusicShop(String name) {
        this.name = name;
        itemsForSale = new ArrayList<ISell>();
    }

    public String getName() {
        return name;
    }

    public void addItemForSale(ISell item) {
        this.itemsForSale.add(item);
    }

    public void removeItemForSale(ISell item) {
        this.itemsForSale.remove(item);
    }

    public ArrayList<ISell> getItemsForSale() {
        return itemsForSale;
    }

    public int calculateTotalMarkup() {
        int total = 0;
        for(ISell item : itemsForSale) {
            total += item.calculateMarkup();
        }
        return total;
    }
}
