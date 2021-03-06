from pprint import PrettyPrinter
from src.cli_helper import CLIHelper as Helper

## Setup prettyprinting tool ##

pp = PrettyPrinter(width=100, compact=True, indent=2)

## Declaring constants ##

VALID_PIZZAS = {"pepperoni", "margherita", "vegetarian", "neapolitan"}
VALID_TOPPINGS = {"olives", "tomatoes", "mushrooms", "jalapenos", "chicken", "beef",
    "pepperoni", ""}
VALID_SIZES = {"small", "medium"}
VALID_DRINKS = {'coke', 'diet coke', 'coke zero', 'pepsi', 'diet pepsi', 'dr pepper',
    'water', 'juice'}
VALID_ITYPES = {'pizzas', 'drinks', 'toppings'}

## Helper Functions ##

def _print_result(result, request_type):
    print("\n[Request]:")
    print("Type: " + request_type)
    print("Sent to: " + result["url"])
    if result["body"] is None:
        print("Body JSON: <empty>")
    else:
        print("Body JSON:")
        pp.pprint(result["body"])
    print("\n[Response]:")
    print("Status code: " + str(result["status_code"]))
    if result["response"] is None:
        print("Body JSON: <empty>")
    else:
        print("Body JSON:")
        pp.pprint(result["response"])
    print("")

def _ask_for_pizza():
    pizza, size, toppings = None, None, None
    print("-----------------------------------------------")
    print("Available: pepperoni, margherita, vegetarian, neapolitan")
    print("Enter a pizza: ", end='')
    while True:
        pizza = input()
        if pizza in VALID_PIZZAS:
            break
        print("Please enter a valid pizza type: ", end='')
    print("-----------------------------------------------")
    print("Available: small, medium")
    print("Enter a size: ", end='')
    while True:
        size = input()
        if size in VALID_SIZES:
            break
        print("Please enter a valid size: ", end='')
    print("-----------------------------------------------")
    print("Available: olives, tomatoes, mushrooms, jalapenos, chicken, beef, pepperoni")
    print("Enter zero or more toppings (comma separated)\n: ", end='')
    while True:
        toppings = input()
        if set([x.strip() for x in toppings.split(",")]).issubset(VALID_TOPPINGS):
            break
        print("Please enter a valid topping (comma separated)\n: ", end='')
    return pizza, size, toppings

def _ask_for_drink():
    drink, size = None, None
    print("-----------------------------------------------")
    print("Available: coke, diet coke, coke zero, pepsi, diet pepsi, dr pepper, water, juice")
    print("Enter a drink: ", end='')
    while True:
        drink = input()
        if drink in VALID_DRINKS:
            break
        print("Please enter a valid drink: ", end='')
    print("-----------------------------------------------")
    print("Available: small, medium")
    print("Enter a size: ", end='')
    while True:
        size = input()
        if size in VALID_SIZES:
            break
        print("Please enter a valid size: ", end='')
    return drink, size

def _get_delivery_info():
    print("Enter an address: ", end='')
    address = input()
    while address == "":
        print("Please enter an address: ", end='')
        address = input()
    print("Enter order instructions: ", end='')
    order_details = input()
    while order_details == "":
        print("Please enter order instructions: ", end='')
        order_details = input()
    print("Enter a delivery number: ", end='')
    delivery_number = input()
    while delivery_number == "":
        print("Please enter a delivery_number: ", end='')
        delivery_number = input()
    return address, order_details, delivery_number

## Command options ##

def create_order():
    """Create an order, prints API-call data"""
    order = {"pizzas": [], "drinks": []}
    print("-----------------------------------------------")
    while True:
        print("Enter 'pizza' or 'drink' to add to order, or 'end' to finish (e to exit)"
            + "\n: ", end='')
        option = input()
        if option == "e":
            return
        if option == "pizza":
            pizza, size, toppings = _ask_for_pizza()
            order["pizzas"].append({"type": pizza, "size": size, "toppings": toppings})
        elif option == "drink":
            drink, size = _ask_for_drink()
            order["drinks"].append({"type": drink, "size": size})
        elif option == "end":
            break
    _print_result(Helper.send_order(order), "POST")

def read_order():
    """Get an order, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to retrieve (e to exit): ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    _print_result(Helper.get_order(order_num), "GET")

def update_order():
    """Update an order, prints API-call data"""
    order_num, order = None, {"pizzas": [], "drinks": []}
    print("-----------------------------------------------")
    print("Enter an order number to update (e to exit): ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    while True:
        print("Enter 'pizza' or 'drink' to replace current order, 'end' to finish (e to exit)"
            + "\n: ", end='')
        option = input()
        if option == "pizza":
            pizza, size, toppings = _ask_for_pizza()
            order["pizzas"].append({"type": pizza, "size": size, "toppings": toppings})
        elif option == "drink":
            drink, size = _ask_for_drink()
            order["drinks"].append({"type": drink, "size": size})
        elif option == "end":
            break
    _print_result(Helper.update_order(order, order_num), "PUT")

def delete_order():
    """Delete an order, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to cancel (e to exit): ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    _print_result(Helper.delete_order(order_num), "DELETE")

def pickup_order():
    """Change an order to pickup, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to change to pickup (e to exit)"
        + "\n: ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    _print_result(Helper.pickup_order(int(order_num)), "POST")

def deliver_inhouse():
    """Change order to inhouse deliver, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to be delivered inhouse (e to exit)"
        + "\n: ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    address, order_details, delivery_number = _get_delivery_info()
    order = {
        "order_number": int(order_num),
        "address": address,
        "details": order_details,
        "delivery_number": delivery_number
    }
    _print_result(Helper.deliver_order_json(order, "inhouse"), "POST")

def deliver_ubereats():
    """Change order to ubereats delivery, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to be delivered UberEats (e to exit)"
        + "\n: ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    address, order_details, delivery_number = _get_delivery_info()
    order = {
        "order_number": int(order_num),
        "address": address,
        "details": order_details,
        "delivery_number": delivery_number
    }
    _print_result(Helper.deliver_order_json(order, "ubereats"), "POST")

def deliver_foodora():
    """Change order to foodora delivery, prints API-call data"""
    order_num = None
    print("-----------------------------------------------")
    print("Enter an order number to be delivered Foodora (e to exit)"
        + "\n: ", end='')
    while True:
        order_num = input()
        if order_num == "e":
            return
        if order_num.isdigit():
            break
        print("Enter a valid number: ", end='')
    address, order_details, delivery_number = _get_delivery_info()
    order = "order_number,address,details,delivery_number\n" + \
        "{0},{1},{2},{3}".format(order_num, address, order_details, delivery_number)
    _print_result(Helper.deliver_order_csv(order), "POST")

def get_menu():
    """Get full menu, prints API-call data"""
    _print_result(Helper.get_menu(), "GET")

def get_item():
    """Get a menu item, prints API-call data"""
    item = {"itype": "", "item": "", "size": ""}
    print("-----------------------------------------------")
    print("Use command 'me' to view menu")
    print("    First layer are item types: 'drink', 'pizza', 'topping'")
    print("    Second layer are item names: 'coke', 'margherita', 'beef', etc.")
    print("    Third layer, when applicable, are sizes: 'small', 'medium'")
    print("Enter item type (e to exit): ", end='')
    option = input()
    if option == "e":
        return
    item["itype"] = option
    print("Enter item name: ", end='')
    item["item"] = input()
    print("Enter size if applicable: ", end='')
    item["size"] = input()
    _print_result(Helper.get_menu(item), "GET")

def print_commands():
    """Prints list of commands"""
    print("\n-----------------------------------------------")
    print("------------PIZZA PARLOUR API DEMO-------------")
    print("-----------------------------------------------")
    print("Commands:")
    print("help: print commands")
    print("----------------CRUD Operations----------------")
    print("cr: create order")
    print("re: get order")
    print("up: update order")
    print("de: delete order")
    print("----------------Delivery Options---------------")
    print("pu: pick up an existing order")
    print("ih: get an order delivered in-house")
    print("ub: get an order delivered with ubereats")
    print("fd: get an order delivered with foodora")
    print("-----------------Get Resources-----------------")
    print("me: get full menu")
    print("it: get a menu item\n")

def get_prompt():
    """Prints command prompt and run function accordingly"""
    print("> ", end='')
    user_input = input()
    option = options.get(user_input, "err")
    if option == "err":
        print("Please enter a valid command")
    else:
        option()

if __name__ == "__main__":
    options = {
        "help": print_commands,
        "cr": create_order,
        "re": read_order,
        "up": update_order,
        "de": delete_order,
        "pu": pickup_order,
        "ih": deliver_inhouse,
        "ub": deliver_ubereats,
        "fd": deliver_foodora,
        "me": get_menu,
        "it": get_item
    }

    print_commands()

    while True:
        get_prompt()
