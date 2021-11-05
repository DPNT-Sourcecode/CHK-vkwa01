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

    def test_checkout__offer(self):
        self.assertEqual(130, checkout("AAA"))
        self.assertEqual(45, checkout("BB"))
        self.assertEqual(175, checkout("ABABA"))
        self.assertEqual(165, checkout("ACADA"))
        self.assertEqual(
            130 + 45 + 50 +30 + 20 + 15,
            checkout("AACABADBB")
        )

