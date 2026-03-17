from products import Product


class Store:
    """
    Manages a collection of Product objects and handles bulk orders.

    Attributes:
        products (list[Product]): A list of product instances available in the store.
    """

    def __init__(self, products: list):
        self.products = products

    def add_product(self, product: str):
        self.products.append(product)

    def remove_product(self, product: str):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return len(self.products)

    def get_all_products(self) -> list:
        """
        Returns a list of all currently active products.

        Returns:
            list[Product]: A list of products where is_active() is True.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes a multiple-item purchase.

        Args:
            shopping_list (list): A list of tuples, each containing
                                  (Product, quantity).

        Returns:
            float: The total price of the entire order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
