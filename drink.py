import json
from food_item import FoodItem

class Drink(FoodItem):
    'Drinks and their relevant data are defined here'

    def get_price(self):
        """Returns the drink price and reads price from data file if price 
        is not initialized"""
        if self.price is None:
            return self.data['drink'][self.item_type][self.size]
        else:
            return self.price

    def set_inputs(self, drink_data):
        """Sets the drink variables to the drink_data. 
        Only call this if you have already checked drink_data."""
        self.item_type = drink_data[0]
        self.size = drink_data[1]

    def check_inputs(self, drink_data):
        """Returns boolean according to if there exists a valid drink under the 
        given inputs"""
        try:
            self.data['drink'][drink_data[0]]
        except KeyError:
            print('type: ' + drink_data[0])
            print('Error: Drink type does not exist.')
            return False
        try: 
            self.data['drink'][drink_data[0]][drink_data[1]]
            return True
        except KeyError:
            print('size: ' + drink_data[1])
            print('Error: Drink size does not exist for ' + drink_data[1] + '.')
            return False

    def update(self, drink_data):
        """Updates drink type and/or size according to parameters 
        and checks validity"""
        if drink_data[0] == -1:
            drink_data[0] = self.item_type
        if drink_data[1] == -1:
            drink_data[1] = self.size
        if self.check_inputs(drink_data):
            self.set_inputs(drink_data)
            return True
        return False
