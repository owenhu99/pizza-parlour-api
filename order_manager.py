from order import Order

class OrderManager:
    """The order manager holds the lost of orders and keeps track of each order number.
    Orders are added and removed here."""

    def __init__(self):
        self.orders = []
        self.num_orders = 1

    def order(self, pizza_data, drinks):
        """Makes an order using the order class and the given parameters. This order is given an 
        order number and stored in the orders list. This order's order number is returned."""
        order = Order(self.num_orders, pizza_data, drinks)
        self.orders.append(order)
        self.num_orders += 1
        return self.num_orders - 1

    def cancel_order(self, order_num):
        """Cancels the order with the given order number by removing it from the orders list.
        Returns True if order exists or False if it does not exist."""
        for order in self.orders:
            if order.get_order_number() == order_num:
                self.orders.remove(order)
                return True
        # order not found
        return False

    def change_to_delivery(self, order_json):
        """Set delivery info
        Returns False if order is not found, True otherwise"""
        order_number = order_json["order_number"]
        order = self.get_order(order_number)
        if not order:
            return False
        order.update_delivery_info(order_json)
        return True

    def change_to_pickup(self, order_num):
        """Change order method to pickup
        Returns False if order is not found, True if found"""
        order = self.get_order(order_num)
        if not order:
            return False
        order.set_pickup(True)
        return True

    def get_num_active_orders(self):
        """Returns the number of orders currently in the system and orders list"""
        return len(self.orders)

    def get_order(self, order_num):
        """Returns the order object corresponding with the given order number.
        Returns False if such an order does not exist in the orders list."""
        for order in self.orders:
            if order.get_order_number() == order_num:
                return order
        # order not found
        return False
