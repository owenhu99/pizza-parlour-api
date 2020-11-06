from pizza import Pizza

class Order:
    'All orders will be defined from this class'
    
    def __init__(self, order_num, pizza_size, pizza_type, pizza_toppings, drinks):
        self.pizza = Pizza(pizza_size, pizza_type, pizza_toppings)
        self.order_num = order_num
        self.drinks = drinks
        self.order_complete = False

    def __init__(self, order_num):
        self.pizza = False
        self.order_num = order_num
        self.drinks = []
        self.order_complete = False


    def updatePizza(self, size, p_type, toppings):
        if pizza is False:
            self.pizza = Pizza(size, p_type, toppings)
        else:
            self.pizza.update(size, p_type, toppings)

    def addDrink(self, drink):
        self.drink.append(drink)

    def updateDrinks(self, drinks):
        self.drinks = drinks

    def get_order_number(self):
        return self.order_num

    def get_pizza(self):
        return self.pizza

    def get_drinks(self):
        return self.drinks

    def ready(self):
        self.order_complete = True

