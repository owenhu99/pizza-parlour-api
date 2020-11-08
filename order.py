from pizza import Pizza
from drink import Drink

class Order:
    'All orders will be defined from this class'
    
    def __init__(self, order_num, pizza_type=None, pizza_size=None, 
            pizza_toppings=None, drinks=None):
        self.order_num = order_num
        self.pizza = Pizza(pizza_type, pizza_size, pizza_toppings)
        self.update_pizza(pizza_type, pizza_size, pizza_toppings)
        self.update_drinks(drinks)

    def add_drink(self, drink_info):
        """Attempts to create a new drink using drink_info and adds 
        it to self.drinks. May Throw Exception if drink_info is invalid"""
        drink = Drink(drink_info[0], drink_info[1])
        self.drinks.append(drink)

    def update_pizza(self, p_type, size, toppings):
        """Replaces self.pizza with a new pizza. May throw Exception if pizza parameters
        are invalid."""
        self.pizza = Pizza(p_type, size, toppings)

    def update_drinks(self, drinks):
        """Replaces the self.drinks list with drinks"""
        self.drinks = []
        for drink in drinks:
            self.add_drink(drink)

    def get_order_number(self):
        """Returns the order number for this order"""
        return self.order_num

    def get_pizza(self):
        """Returns the pizza object for this order"""
        return self.pizza

    def get_drinks(self):
        """Returns the list of drink objects for this order"""
        return self.drinks

    def get_price(self):
        """Returns the price of this order"""
        price = self.pizza.get_price()
        for drink in self.drinks:
            price += drink.get_price()
        return price
