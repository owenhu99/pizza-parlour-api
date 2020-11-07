import json

class Pizza:
    'Pizzas and their relevant data are defined here'
    price = None

    def __init__(self, p_type, size, toppings):
        with open('data.json') as f:
            self.data = json.load(f)
        if self.check_inputs(p_type, size, toppings):
            self.size = size
            self.p_type = p_type
            self.toppings = toppings
            self.price = self.get_price()

    def get_size(self):
        return self.size

    def get_type(self):
        return self.p_type

    def get_toppings(self):
        return self.toppings

    def get_price(self):
        if self.price is None:
            price = self.data['pizza'][self.p_type][self.size]
            for topping in self.toppings:
                price += self.data['topping'][topping]
            return price
        return self.price

    def manual_price_update(self, price):
        self.price = price
        return self.get_price()

    def check_inputs(self, p_type, size, toppings):
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

    def update(self, p_type, size, toppings):
        if size == -1:
            size = self.size
        if p_type == -1:
            p_type = self.p_type
        if toppings == -1:
            toppings = self.toppings
        if self.check_inputs(p_type, size, toppings):
            self.p_type = p_type
            self.size = size
            self.toppings = toppings

