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
        self.skus = list(skus)

    def calculate_checkout(self):


# noinspection PyUnusedLocal
# skus = unicode string
def checklite(skus: str) -> int:
    """
    Returns the value of the basket
    Args:
        skus: String where each letter represents an item in the basket.
    """
    ...




