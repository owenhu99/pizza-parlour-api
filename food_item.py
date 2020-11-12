import json
import abc

class FoodItem:
    'Food items (pizzas and drinks) and their relevant data are defined here'
    __metaclass__ = abc.ABCMeta
    price = None
    item_type = None
    size = None

    def __init__(self, item_data):
        with open('data.json') as file_menu:
            self.data = json.load(file_menu)
        if self.check_inputs(item_data):
            self.set_inputs(item_data)
            self.price = self.get_price()
        else:
            raise Exception('Error: Invalid attributes')

    def get_size(self):
        'Returns the food item size'
        return self.size

    def get_type(self):
        'Returns the food item type'
        return self.item_type

    def manual_price_update(self, price):
        'Manually updates and returns price for this food item instance'
        self.price = price
        return self.get_price()

    @abc.abstractmethod
    def get_price(self):
        """Gets price of item: to be implemented"""

    @abc.abstractmethod
    def set_inputs(self, item_data):
        """Sets input: to be implemented"""

    @abc.abstractmethod
    def check_inputs(self, item_data):
        """Checks input: to be implemented"""
