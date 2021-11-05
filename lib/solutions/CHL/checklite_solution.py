class Basket:
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    def __init__(self, skus: str):
        if any(sku not in prices for sku in skus):
            raise ValueError()
        self.skus = list(skus)


# noinspection PyUnusedLocal
# skus = unicode string
def checklite(skus: str) -> int:
    """
    Returns the value of the basket
    Args:
        skus: String where each letter represents an item in the basket.
    """



