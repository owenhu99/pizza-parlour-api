from src.food_item import FoodItem

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

    def set_inputs(self, item_data):
        """Sets the pizza variables to the pizza_data.
        Only call this if you have already checked pizza_data."""
        self.item_type = item_data[0]
        self.size = item_data[1]
        self.toppings = item_data[2]

    def check_inputs(self, item_data):
        """Returns boolean according to if there exists a valid pizza
        and toppings under the given inputs"""
        if not item_data[0] in self.data['pizza']:
            print('Error: ' + item_data[0] + ' pizza does not exist.')
            return False

        if not item_data[1] in self.data['pizza'][item_data[0]]:
            print('Error: ' + item_data[1] + ' size does not exist for '
                    + item_data[0] + ' pizza.')
            return False

        for topping in item_data[2]:
            if not topping in self.data['topping']:
                print('Error: Pizza topping ' + topping + ' does not exist.')
                return False
        return True

    def update(self, pizza_data):
        """Updates pizza values according to pizza_data and checks validity"""
        if pizza_data[0] == -1:
            pizza_data[0] = self.item_type
        if pizza_data[1] == -1:
            pizza_data[1] = self.size
        if pizza_data[2] == -1:
            pizza_data[2] = self.toppings
        if self.check_inputs(pizza_data):
            self.set_inputs(pizza_data)
            return True
        return False

    def get_dict(self):
        """Return pizza data in dictionary format"""
        return {
            "type": self.item_type,
            "size": self.size,
            "toppings": self.toppings,
            "price": self.get_price()
        }
