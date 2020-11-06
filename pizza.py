class Pizza:
    'Pizzas and their relevant data are defined here'

    def __init__(self, size, p_type, toppings):
        self.size = size
        self.p_type = p_type
        self.toppings = toppings

    def update(self, size, p_type, toppings):
        if size != -1:
            self.size = size
        if p_type != -1:
            self.p_type = p_type
        if toppings != -1:
            self.toppings = toppings
