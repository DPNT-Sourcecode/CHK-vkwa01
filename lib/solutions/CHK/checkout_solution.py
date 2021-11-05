class Basket:
    """
    Helper class to calculate checkout
    """
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }
    # The offers are run in order, so the most attractive offer should be at the top.
    buy_x_get_y_free_offers = [
        {"quantity": 2, "sku": "E", "free": "B"},
        {"quantity": 3, "sku": "F", "free": "F"},
        {"quantity": 3, "sku": "N", "free": "M"},
        {"quantity": 3, "sku": "R", "free": "Q"},
        {"quantity": 4, "sku": "U", "free": "U"},
    ]
    # The offers are run in order, so the most attractive offer should be at the top.
    multi_item_offers = [
        {"quantity": 5, "sku": "A", "price": 200},
        {"quantity": 3, "sku": "A", "price": 130},
        {"quantity": 2, "sku": "B", "price": 45},
        {"quantity": 10, "sku": "H", "price": 80},
        {"quantity": 5, "sku": "H", "price": 45},
        {"quantity": 2, "sku": "K", "price": 150},
        {"quantity": 5, "sku": "P", "price": 200},
        {"quantity": 3, "sku": "Q", "price": 80},
        {"quantity": 3, "sku": "V", "price": 130},
        {"quantity": 2, "sku": "V", "price": 90},
    ]

    def __init__(self, skus: str):
        if any(sku not in self.prices for sku in skus):
            raise ValueError(f"Invalid basket, all skus must be one of {', '.join(sku for sku in self.prices)}")
        self.skus = sorted(list(skus))

    def _calculate_offers_and_remove_skus(self) -> int:
        """
        Find offers in the basket and remove them from the list of skus.
        Returns:
            The total value of offers found.
        """
        offer_value = 0

        for offer in self.buy_x_get_y_free_offers:
            quantity = offer["quantity"]
            remove = offer["free"]
            sku = offer["sku"]
            matches = self.skus.count(sku)
            offers_found = matches // quantity
            skus_to_remove = remove * offers_found
            for sku_to_remove in skus_to_remove:
                try:
                    self.skus.remove(sku_to_remove)
                except ValueError:
                    pass

        for offer in self.multi_item_offers:
            quantity = offer["quantity"]
            price = offer["price"]
            sku = offer["sku"]
            matches = self.skus.count(sku)
            offers_found = matches // quantity
            offer_value += offers_found * price
            for _ in range(offers_found * quantity):
                self.skus.remove(sku)

        return offer_value

    def calculate_checkout(self) -> int:
        """
        Returns
        """
        checkout_value = self._calculate_offers_and_remove_skus()
        checkout_value += sum(self.prices[sku] for sku in self.skus)
        return checkout_value


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    Returns the value of the basket
    Args:
        skus: String where each letter represents an item in the basket.
    """
    try:
        basket = Basket(skus)
        return basket.calculate_checkout()
    except ValueError:
        return -1



