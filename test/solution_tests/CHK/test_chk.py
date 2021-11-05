from unittest import TestCase

from lib.solutions.CHK.checkout_solution import checkout


class TestChk(TestCase):
    def test_checkout__invalid_sku(self):
        self.assertEqual(-1, checkout("z"))
        self.assertEqual(-1, checkout("ABCD7"))

    def test_checkout__no_offer(self):
        self.assertEqual(50, checkout("A"))
        self.assertEqual(30, checkout("B"))
        self.assertEqual(20, checkout("C"))
        self.assertEqual(15, checkout("D"))

        self.assertEqual(115, checkout("ABCD"))
        self.assertEqual(135, checkout("AACD"))

    def test_checkout__multi_item_offer(self):
        self.assertEqual(130, checkout("AAA"))
        self.assertEqual(45, checkout("BB"))
        self.assertEqual(175, checkout("ABABA"))
        self.assertEqual(165, checkout("ACADA"))
        self.assertEqual(
            130 + 50 + 45 + 30 + 20 + 15,
            checkout("AACABADBB")
        )
        self.assertEqual(80, checkout("H" * 10))
        self.assertEqual(45, checkout("H" * 5))
        self.assertEqual(150, checkout("KK"))
        self.assertEqual(300, checkout("K" * 4))
        self.assertEqual(200, checkout("P" * 5))
        self.assertEqual(80, checkout("QQQ"))
        self.assertEqual(130, checkout("VVV"))
        self.assertEqual(90, checkout("VV"))
        self.assertEqual(220, checkout("V" * 5))

    def test_checkout__multi_item_offer__priority(self):
        self.assertEqual(250, checkout("A" * 6))
        self.assertEqual(330, checkout("A" * 8))
        self.assertEqual(380, checkout("A" * 9))

    def test_checkout__buy_x_get_y_free(self):
        self.assertEqual(80, checkout("EEB"))
        self.assertEqual(195, checkout("EEBEECDB"))
        self.assertEqual(20, checkout("FFF"))
        self.assertEqual(20, checkout("FF"))
        self.assertEqual(230, checkout(("F" * 6) + ("E" * 4) + ("B" * 3)))
        self.assertEqual(120, checkout("NNNM"))
        self.assertEqual(150, checkout("RRRQ"))
        self.assertEqual(120, checkout("UUUU"))

    def test_checkout__multi_offers(self):
        self.assertEqual(125, checkout("EEBBB"))
        self.assertEqual(220, checkout(("F" * 3) + ("A" * 5)))
        self.assertEqual(
            380 + 70,
            checkout(("F" * 10) + ("A" * 9))
        )
        self.assertEqual(
            200 + 30 + 20 + 15 + 120,
            checkout("AAEEAABBEACD")
        )
