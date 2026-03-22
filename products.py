class Product:
    """
    Represents a product available in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price per unit of the product.
        quantity (int): The current stock level.
        active (bool): Status indicating if the product is available for sale.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product. Must be non-negative.
            quantity (int): Initial stock level. Must be non-negative.

        Raises:
            ValueError: If name is empty, or if price or quantity are negative.
        """
        if not name:
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product in stock.

        Returns:
            int: The current stock level.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Updates the stock level and manages the product's active status.
        Deactivates the product automatically if quantity reaches zero.

        Args:
            quantity (int): The new stock level.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """
        Checks if the product is currently active and available for sale.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Sets the product status to active."""
        self.active = True

    def deactivate(self):
        """Sets the product status to inactive."""
        self.active = False

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A formatted string containing name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.get_quantity()}"

    def buy(self, requested_quantity: int) -> float:
        """
        Processes a purchase of a specific quantity.

        Args:
            requested_quantity (int): The amount of items to buy.

        Returns:
            float: The total price of the purchase.
        """
        if requested_quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if requested_quantity > self.get_quantity():
            raise ValueError(
                f"Quantity of {self.name} is not enough: {self.get_quantity()} in stock"
            )
        if not self.is_active():
            raise ValueError(
                f"Product {self.name} is not available"
            )

        new_stock = self.get_quantity() - requested_quantity
        self.set_quantity(new_stock)
        total_price = self.price * requested_quantity

        return total_price
