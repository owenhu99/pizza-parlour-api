import json
from food_item import FoodItem

class Pizza(FoodItem):
    'Pizzas and their relevant data are defined here'

    def get_toppings(self):
        'Returns the list of pizza toppings'
        return self.toppings

    def get_price(self):
        """Returns the pizza price and reads the combined pizza 
        and toppings price from data file if price is not initialized"""
        if self.price is None:
            price = self.data['pizza'][self.item_type][self.size]
            for topping in self.toppings:
                price += self.data['topping'][topping]
            return price
        return self.price

    def set_inputs(self, pizza_data):
        """Sets the pizza variables to the pizza_data.
        Only call this if you have already checked pizza_data."""
        self.item_type = pizza_data[0]
        self.size = pizza_data[0]
        self.toppings = pizza_data[0]

    def check_inputs(self, pizza_data):
        """Returns boolean according to if there exists a valid pizza 
        and toppings under the given inputs"""
        item_type, size, toppings = pizza_data[0], pizza_data[1], pizza_data[2]
        try:
            self.data['pizza'][item_type]
            try:
                self.data['pizza'][item_type][size]
                for topping in toppings:
                    try:
                        self.data['topping'][topping]
                    except KeyError:
                        print('Error: Pizza topping ' + topping + ' does not exist.')
                        return False
                return True
            except KeyError:
                print('Error: ' + size + ' size does not exist for ' + item_type + ' pizza.')
                return False
        except KeyError:
            print('Error: ' + item_type + ' pizza does not exist.')
            return False

    def update(self, pizza_data):
        """Updates pizza values according to pizza_data and checks validity"""
        item_type, size, toppings = pizza_data[0], pizza_data[1], pizza_data[2]
        if item_type == -1:
            item_type = self.item_type
        if size == -1:
            size = self.size
        if toppings == -1:
            toppings = self.toppings
        if self.check_inputs([item_type, size, toppings]):
            self.item_type = item_type
            self.size = size
            self.toppings = toppings
            return True
        return False
