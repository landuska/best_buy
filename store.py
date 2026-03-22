from products import Product


class Store:
    """
    Manages a collection of Product objects and handles bulk orders.

    Attributes:
        products (list[Product]): A list of product instances available in the store.
    """

    def __init__(self, products: list):
        """
        Initializes the store with a list of products.

        Args:
            products (list): A list of Product instances.

        Raises:
            ValueError: If the product list is empty or contains non-Product objects.
        """
        if not products:
            raise ValueError("The product list is empty.")

        for product in products:
            if not isinstance(product, Product):
                raise ValueError("All items in the list must be instances of the Product class.")

        self.products = products

    def add_product(self, product):
        """
        Adds a single product to the store's inventory.

        Args:
            product (Product): The product instance to add.

        Raises:
            ValueError: If the provided object is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the store.")

        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a specific product from the store's inventory.

        Args:
            product (Product): The product instance to remove.
        """
        if product not in self.products:
            raise ValueError("Product not found in the store.")

        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all items in the store.

        Returns:
            int: The sum of the quantities of all products.
        """
        total_quantity = 0

        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

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

        if not shopping_list:
            return 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
