from products import Product
from store import Store


def print_menu():
    """
    Prints the main store menu.

    Returns:
        str: main menu
    """
    print("-" * 10)
    print("Store Menu")
    print("-" * 10)
    print("1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit\n")


def get_user_input(string: str):
    """
    Captures user input.

    Returns:
        str: The cleaned and lowercase string of the user's input.
    """
    while True:
        user_input = input(f"{string}: ").lower().strip()

        if user_input:
            return user_input
        print("Please enter a valid input")


def print_list_of_product(store_instance):
    """ Prints the list of products available to the user

    Args:
        store_instance (Store): The store instance to fetch available products from.

    Returns:
        list: A list of tuples, each containing a (Product object, quantity)."""
    products = store_instance.get_all_products()
    for i in range(len(products)):
        print(f"{i + 1}. {products[i].show()}")


def order_from_user(store_instance):
    """
    Handles the interactive process of creating a shopping list.

    The user can search for products by index number of a product and specify quantities.
    The loop continues until the user enters '0'.

    Args:
        store_instance (Store): The store instance to fetch available products from.

    Returns:
        list: A list of tuples, each containing a (Product object, quantity).
    """
    shopping_list_from_user = []
    ask_product_number = "Enter the index number of a product do you want to buy or '0' to see a total price of your order: "
    ask_amount = "How many do you want to buy?: "

    while True:
        available_products_in_store = store_instance.get_all_products()
        print("\nAvailable Products:")
        print("-" * 10)
        print_list_of_product(store_instance)

        if not available_products_in_store:
            print("The store is currently empty.")
            break

        while True:
            try:
                user_selected_product = int(get_user_input(ask_product_number))
                break
            except ValueError:
                print("Please enter a valid number")

        if user_selected_product == 0:
            break

        if user_selected_product < 1 or user_selected_product > len(available_products_in_store):
            print("Please enter a valid number")
            continue

        found_product = None
        for i in range(len(available_products_in_store)):
            if i == user_selected_product - 1:
                found_product = available_products_in_store[i]
                break

        while True:
            try:
                user_choice_amount = int(get_user_input(ask_amount))
                break
            except ValueError:
                print("Please enter a valid amount")

        if user_choice_amount <= 0:
            print("Please enter a valid amount")
            continue

        if found_product:
            shopping_list_from_user.append((found_product, user_choice_amount))

            print("-" * 10)
            print(f"Added {user_choice_amount} x {found_product.name} to cart.")

    try:
        total_cost = store_instance.order(shopping_list_from_user)
        return total_cost
    except ValueError as e:
        print(f"Order failed: {e}")
        return 0.0


def user_select_command(store_instance):
    """
    Main controller loop for user interaction with the store.

    Args:
        store_instance (Store): The store instance to be managed.
    """
    while True:
        print_menu()
        select_option = get_user_input("Enter your option: ")

        if select_option == "4":
            break

        if select_option == "1":
            print("-" * 10)
            print("We have the following products:")
            print("-" * 10)
            print_list_of_product(store_instance)
            print("-" * 10)

        elif select_option == "2":
            print("-" * 10)
            print(f"We have in total {store_instance.get_total_quantity()} items in the store")
            print("-" * 10)

        elif select_option == "3":
            print("-" * 10)
            print(f"Total price of your order is: {order_from_user(store_instance)}")
            print("-" * 10)

        else:
            print("The number is out of menu")


def main():
    # setup initial stock of inventory
    try:
        product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Product("Google Pixel 7", price=500, quantity=250)
                        ]
        best_buy = Store(product_list)
        user_select_command(best_buy)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
