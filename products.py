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
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a specific quantity.

        Args:
            quantity (int): The amount of items to buy.

        Returns:
            float: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.quantity:
            raise ValueError(
                f"Quantity is not enough: {self.quantity} in stock"
            )

        new_stock = self.quantity - quantity
        self.set_quantity(new_stock)

        total_price = self.price * quantity
        return total_price
