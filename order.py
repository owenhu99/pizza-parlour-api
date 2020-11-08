from pizza import Pizza
from drink import Drink

class Order:
    'All orders will be defined from this class'
    
    def __init__(self, order_num, pizzas=None, drinks=None):
        self.order_num = order_num

        if pizzas is not None:
            self.update_pizzas(pizzas)

        if drinks is not None:
            self.update_drinks(drinks)

    def update_pizzas(self, pizzas):
        self.pizzas = []
        for pizza in pizzas:
            self.add_pizza(pizza)
            
    def add_pizza(self, pizza_info):
        pizza = Pizza(pizza_info)
        self.pizzas.append(pizza)

    def update_drinks(self, drinks):
        """Replaces the self.drinks list with drinks"""
        self.drinks = []
        for drink in drinks:
            self.add_drink(drink)

    def add_drink(self, drink_info):
        """Attempts to create a new drink using drink_info and adds 
        it to self.drinks. May Throw Exception if drink_info is invalid"""
        drink = Drink(drink_info[0], drink_info[1])
        self.drinks.append(drink)

    def get_order_number(self):
        """Returns the order number for this order"""
        return self.order_num

    def get_pizzas(self):
        """Returns the pizza object for this order"""
        return self.pizzas

    def get_drinks(self):
        """Returns the list of drink objects for this order"""
        return self.drinks

    def get_price(self):
        """Returns the price of this order"""
        price = 0
        for pizza in self.pizzas:
            price += pizza.get_price()
        for drink in self.drinks:
            price += drink.get_price()
        return price
