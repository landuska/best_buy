from products import Product
from store import Store


def print_menu_and_select_from_the_main_menu():
    """
    Displays the main store menu and captures user input.

    Returns:
        str: The cleaned and lowercase string of the user's menu choice.
    """
    print("   Store Menu")
    print("-" * 10)
    select_from_the_main_menu = input("1. List all products in store\n"
                                      "2. Show total amount in store\n"
                                      "3. Make an order\n"
                                      "4. Quit\n"
                                      "Enter your choice: ").lower().strip()
    return select_from_the_main_menu


def order_from_user(best_buy):
    """
    Handles the interactive process of creating a shopping list.

    The user can search for products by name and specify quantities.
    The loop continues until the user enters '0'.

    Args:
        best_buy (Store): The store instance to fetch available products from.

    Returns:
        list: A list of tuples, each containing a (Product object, quantity).
    """
    available_products = best_buy.get_all_products()
    shopping_list = []
    found_product = ""

    while True:
        user_choice_product = input(
            "Enter a name of product do you want to buy or '0' to see a total price of your order "
        ).strip()

        if user_choice_product == "0":
            break

        if not user_choice_product:
            print("Please enter a valid option")
            continue

        for product in available_products:
            if user_choice_product.lower() in product.name.lower():
                found_product = product
                break

        user_choice_amount = int(input("How many do you want to buy?: ").strip())

        if not isinstance(user_choice_amount, int) or user_choice_amount < 0:
            print("Please enter a valid option")
            continue

        if found_product:
            shopping_list.append((found_product, user_choice_amount))
        else:
            print("Product not found!")

    return shopping_list


def user_select_command(best_buy):
    """
    Main controller loop for user interaction with the store.

    Args:
        best_buy (Store): The store instance to be managed.
    """
    while True:
        select_option = print_menu_and_select_from_the_main_menu()

        if select_option == "4":
            break

        if select_option == "1":
            print("-" * 6)
            for i in range(len(best_buy.get_all_products())):
                print(f"{i + 1}. {best_buy.get_all_products()[i].show()}")
            print("-" * 6)

        elif select_option == "2":
            print("-" * 6)
            print(f"{best_buy.get_total_quantity()} items in store")
            print("-" * 6)

        elif select_option == "3":
            list_of_order = order_from_user(best_buy)
            print("-" * 6)
            print(f"Total price of your order is: {best_buy.order(list_of_order)}")
            print("-" * 6)
        else:
            print("The number is out of menu")
            continue


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
