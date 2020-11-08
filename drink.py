import json

class Drink:
    'Drinks and their relevant data are defined here'
    price = None

    def __init__(self, drink_type, size):
        with open('data.json') as f:
            self.data = json.load(f)

        if self.check_inputs(drink_type, size):
            self.drink_type = drink_type
            self.size = size
            self.price = self.get_price()
        else:
            raise Exception('Error: Invalid drink attributes')

    def get_size(self):
        'Returns the drink size'
        return self.size

    def get_type(self):
        'Returns the drink type'
        return self.drink_type

    def get_price(self):
        """Returns the drink price and reads price from data file if price 
        is not initialized"""
        if self.price is None:
            return self.data['drink'][self.drink_type][self.size]
        else:
            return self.price

    def manual_price_update(self, price):
        'Manually updates and returns price for this drink instance'
        self.price = price
        return self.get_price()

    def check_inputs(self, drink_type, size):
        """Returns boolean according to if there exists a valid drink under the 
        given inputs"""
        try:
            self.data['drink'][drink_type]
            try: 
                self.data['drink'][drink_type][size]
                return True
            except KeyError:
                print('Error: Drink size does not exist for ' + drink_type + '.')
                return False
        except KeyError:
            print('Error: Drink type does not exist.')
            return False

    def update(self, drink_type, size):
        """Updates drink type and/or size according to parameters 
        and checks validity"""
        if drink_type == -1:
            drink_type = self.drink_type
        if size == -1:
            size = self.size
        if self.check_inputs(drink_type, size):
            self.drink_type = drink_type
            self.size = size
            return True
        return False
