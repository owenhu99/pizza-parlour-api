import json

class Pizza:
    'Pizzas and their relevant data are defined here'
    price = None

    def __init__(self, pizza_data):
        with open('data.json') as f:
            self.data = json.load(f)
            
        if self.check_inputs(pizza_data):
            self.p_type = pizza_data[0]
            self.size = pizza_data[1]
            self.toppings = pizza_data[2]
            self.price = self.get_price()
        else:
            raise Exception('Error: Invalid pizza attributes')

    def get_size(self):
        'Returns the pizza size'
        return self.size

    def get_type(self):
        'Returns the pizza type'
        return self.p_type

    def get_toppings(self):
        'Returns the list of pizza toppings'
        return self.toppings

    def get_price(self):
        """Returns the pizza price and reads the combined pizza 
        and toppings price from data file if price is not initialized"""
        if self.price is None:
            price = self.data['pizza'][self.p_type][self.size]
            for topping in self.toppings:
                price += self.data['topping'][topping]
            return price
        return self.price

    def manual_price_update(self, price):
        'Manually updates and returns price for this pizza instance'
        self.price = price
        return self.get_price()

    def check_inputs(self, pizza_data):
        """Returns boolean according to if there exists a valid pizza 
        and toppings under the given inputs"""
        p_type, size, toppings = pizza_data[0], pizza_data[1], pizza_data[2]
        try:
            self.data['pizza'][p_type]
            try:
                self.data['pizza'][p_type][size]
                for topping in toppings:
                    try:
                        self.data['topping'][topping]
                    except KeyError:
                        print('Error: Pizza topping ' + topping + ' does not exist.')
                        return False
                return True
            except KeyError:
                print('Error: ' + size + ' size does not exist for ' + p_type + ' pizza.')
                return False
        except KeyError:
            print('Error: ' + p_type + ' pizza does not exist.')
            return False

    def update(self, pizza_data):
        """Updates pizza values according to pizza_data and checks validity"""
        p_type, size, toppings = pizza_data[0], pizza_data[1], pizza_data[2]
        if p_type == -1:
            p_type = self.p_type
        if size == -1:
            size = self.size
        if toppings == -1:
            toppings = self.toppings
        if self.check_inputs([p_type, size, toppings]):
            self.p_type = p_type
            self.size = size
            self.toppings = toppings
            return True
        return False
