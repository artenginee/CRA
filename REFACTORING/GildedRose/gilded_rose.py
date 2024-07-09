# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"


class GildedRoseItem(metaclass=ABCMeta):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update_quality(self):
        pass

    @abstractmethod
    def update_sell_in(self):
        item = self.item
        item.sell_in -= 1


class AgedBrieItem(GildedRoseItem):

    def update_quality(self):
        item = self.item
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1


class BackstageItem(GildedRoseItem):
    def update_quality(self):
        item = self.item
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality += 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality += 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasItem(GildedRoseItem):
    def update_quality(self):
        item = self.item
        item.sell_in -= 1

    def update_sell_in(self):
        pass


class NormalItem(GildedRoseItem):
    def update_quality(self):
        item = self.item
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            gilded_rose_item = self.gilded_rose_item_generator(item)

            gilded_rose_item.update_quality()
            gilded_rose_item.update_sell_in()

    def gilded_rose_item_generator(self, item):
        if item.name == "Aged Brie":
            gilded_rose_item = AgedBrieItem(item)

        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            gilded_rose_item = BackstageItem(item)

        elif item.name == "Sulfuras, Hand of Ragnaros":
            gilded_rose_item = SulfurasItem(item)

        else:  # 일반아이템
            gilded_rose_item = NormalItem(item)
        return gilded_rose_item


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
