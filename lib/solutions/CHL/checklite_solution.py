class Basket:
    """
    Helper class to calculate checkout
    """
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    offers = [
        {"quantity": 3, "sku": "A", "price": 130},
        {"quantity": 2, "sku": "B", "price": 45},
    ]

    def __init__(self, skus: str):
        if any(sku not in prices for sku in skus):
            raise ValueError(f"Invalid basket, all skus must be one of {', '.join(sku for sku in prices)}")
        self.skus = sorted(list(skus))

    def _calculate_offers_and_remove_skus(self) -> int:
        """
        Find offers in the basket and remove them from the list of skus.
        Returns:
            The total value of offers found.
        """
        offer_value = 0
        for offer in self.offers:
            quantity = offer["quantity"]
            price = offer["price"]
            sku = offer["sku"]
            matches = self.skus.count(sku)
            offers_found = matches // quantity
            offer_value += offers_found * price
            for _ in range(matches * quantity):
                self.skus.remove(sku)
        return offer_value

    def calculate_checkout(self) -> int:
        """
        Returns
        """
        ...



# noinspection PyUnusedLocal
# skus = unicode string
def checklite(skus: str) -> int:
    """
    Returns the value of the basket
    Args:
        skus: String where each letter represents an item in the basket.
    """
    ...







