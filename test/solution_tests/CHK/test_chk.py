from unittest import TestCase

from lib.solutions.CHK.checkout_solution import checkout


class TestChk(TestCase):
    def test_checkout__invalid_sku(self):
        self.assertEqual(-1, checkout("Z"))
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

    def test_checkout__multi_item_offer__priority(self):
        self.assertEqual(250, checkout("AAAAAA"))
        self.assertEqual(330, checkout("AAAAAAAA"))
        self.assertEqual(380, checkout("AAAAAAAAA"))

    def test_checkout__buy_x_get_y_free(self):
        self.assertEqual(80, checkout("EEB"))
        self.assertEqual(195, checkout("EEBEECDB"))
        self.assertEqual(20, checkout("FFF"))
        self.assertEqual(20, checkout("FF"))
        self.assertEqual(230, checkout("FFFFFFEEEEBBB"))

    def test_checkout__multi_offers(self):
        self.assertEqual(125, checkout("EEBBB"))
        self.assertEqual(220, checkout("FFFAAAAA"))
        self.assertEqual(
            380 + 70,
            checkout("FFFFFFFFFFAAAAAAAAA")
        )
        self.assertEqual(
            200 + 30 + 20 + 15 + 120,
            checkout("AAEEAABBEACD")
        )


