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
            try: 
                self.data['drink'][drink_data[0]][drink_data[1]]
                return True
            except KeyError:
                print('Error: Drink size does not exist for ' + item_type + '.')
                return False
        except KeyError:
            print('Error: Drink type does not exist.')
            return False

    def update(self, drink_data):
        """Updates drink type and/or size according to parameters 
        and checks validity"""
        item_type, size = drink_data[0], drink_data[1]
        if item_type == -1:
            item_type = self.item_type
        if size == -1:
            size = self.size
        if self.check_inputs(item_type, size):
            self.item_type = item_type
            self.size = size
            return True
        return False
