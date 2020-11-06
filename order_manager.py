from order import Order

class OrderManager:

    def __init__(self):
        self.orders = []
        self.order_num = 1

    def order(self):
        order = Order(self.order_num)
        self.orders.append(order)
        self.order_num += 1
        return self.order_num - 1

    def order(self, pizza_size, pizza_type, pizza_toppings, drinks):
        order = Order(self.order_num, pizza_size, pizza_type, pizza_toppings, drinks)
        self.orders.append(order)
        self.order_num += 1
        return self.order_num - 1

    def cancel_order(self, order_num):
        for order in orders:
            if order.get_order_number() == order_num:
                return orders.remove(order)
        # order not found
        return False

    def get_order(self, order_num):
        for order in orders:
            if order.get_order_number() == order_num:
                return order
        # order not found
        return False
