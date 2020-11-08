from order_manager import OrderManager

def test_order_manager():
    manager = OrderManager()
    assert manager.get_num_active_orders() == 0
    assert manager.num_orders == 1

def test_cancel_order():
    manager = OrderManager()
    order_num = manager.order([['pepperoni', 'medium', ['olives']]], [['coke', 'small']])

    assert manager.get_num_active_orders() == 1
    manager.cancel_order(order_num)
    assert manager.get_num_active_orders() == 0

def test_order():
    manager = OrderManager()
    order_num = manager.order([['pepperoni', 'medium', ['olives']]], [['coke', 'small']])
    order = manager.get_order(order_num)

    assert manager.get_num_active_orders() == 1
    assert order.get_pizzas()[0].get_type() == 'pepperoni'
    assert order.get_pizzas()[0].get_size() == 'medium'
    assert order.get_pizzas()[0].get_toppings() == ['olives']
    assert order.get_drinks()[0].get_type() == 'coke'
    assert order.get_drinks()[0].get_size() == 'small'

    order_num = manager.order([['vegetarian', 'small', ['beef']]], [['pepsi', 'medium']])
    order = manager.get_order(order_num)

    assert manager.get_num_active_orders() == 2
    assert order.get_pizzas()[0].get_type() == 'vegetarian'
    assert order.get_pizzas()[0].get_size() == 'small'
    assert order.get_pizzas()[0].get_toppings() == ['beef']
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'medium'

def test_get_num_active_orders():
    manager = OrderManager()
    order_num1 = manager.order([['pepperoni', 'medium', ['olives']]], [['coke', 'small']])

    assert manager.get_num_active_orders() == 1
    order_num2 = manager.order([['vegetarian', 'small', ['chicken']]], [['pepsi', 'medium']])
    assert manager.get_num_active_orders() == 2
    manager.cancel_order(order_num1)
    assert manager.get_num_active_orders() == 1
    manager.cancel_order(order_num2)
    assert manager.get_num_active_orders() == 0

def get_order():
    manager = OrderManager()
    order_num1 = manager.order([['pepperoni', 'medium', ['olives']]], [['coke', 'small']])
    order_num2 = manager.order([['vegetarian', 'small', ['beef']]], [['pepsi', 'medium']])
    assert manager.get_order(order_num1).get_pizzas()[0].get_type() == 'pepperoni'
    assert manager.get_order(order_num2).get_pizzas()[0].get_type() == 'vegetarian'
    assert manager.get_order(3) == False
