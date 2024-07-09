# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"

NONAME = "noname"


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_should_be_nothing_when_no_item(self):
        items = []
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, len(items))

    def test_noname_selling_0_quality(self):
        items = [Item(NONAME, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_noname_sellin_0_quality_1(self):
        items = [Item(NONAME, 0, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_sellin_0_quality_80(self):
        items = [Item(SULFURAS, 0, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_aged_brie_sellin_0_quality_0(self):
        items = [Item(AGED_BRIE, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_pass_sellin_0_quality_0(self):
        items = [Item(BACKSTAGE_PASS, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_sellin_12_quality_0(self):
        items = [Item(BACKSTAGE_PASS, 12, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_silfuras_sellin_m2_quality_80(self):
        items = [Item(SULFURAS, -2, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
