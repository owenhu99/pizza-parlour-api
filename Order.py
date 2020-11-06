import Pizza from Pizza

class Order:
    'All orders will be defined from this class'
    self.pizza = False
    
    def __init__(self, order_num, pizza_size, pizza_type, pizza_toppings, drinks):
        self.pizza = Pizza(pizza_size, pizza_type, pizza_toppings)
        self.order_num = order_num
        self.drinks = drinks

    def __init__(self, order_num):
        self.order_num = order_num


    def updatePizza(self, size, p_type, toppings):
        self.pizza.update(size, p_type, toppings)

    def addDrink(self, drink):
        self.drink.append(drink)

    def updateDrinks(self, drinks):
        self.drinks = drinks

