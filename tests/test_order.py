from src.order import Order
import json

def test_order():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_order_number() == 1
    assert order.get_pizzas()[0].get_type() == 'pepperoni'
    assert order.get_pizzas()[0].get_size() == 'medium'
    assert order.get_pizzas()[0].get_toppings() == ['olives', 'chicken']
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'

    order = Order(2, [['vegetarian', 'small', ['beef']]], 
            [['pepsi', 'small'], ['coke', 'medium']])
    assert order.get_order_number() == 2
    assert order.get_pizzas()[0].get_type() == 'vegetarian'
    assert order.get_pizzas()[0].get_size() == 'small'
    assert order.get_pizzas()[0].get_toppings() == ['beef']
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'coke'
    assert order.get_drinks()[1].get_size() == 'medium'

    try:
        order = Order(3, [['invalid', 'invalid', ['invalid']]], [['invalid', 'invalid']])
        assert False
    except:
        assert True

    try:
        order = Order(4, [['pepperoni', 'small', 'invalid']], [['coke', 'small']])
        assert False
    except:
        assert True

    try:
        order = Order(5, [['pepperoni', 'small', ['beef']]], ['invalid'])
        assert False
    except:
        assert True

    try:
        order = Order(6, [['pepperoni', 'small', ['beef']]], 'invalid')
        assert False
    except:
        assert True

def test_add_pizza():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    pizza_info = ['vegetarian', 'small', ['beef', 'chicken']]
    order.add_pizza(pizza_info)
    assert order.get_pizzas()[0].get_type() == 'pepperoni'
    assert order.get_pizzas()[0].get_size() == 'medium'
    assert order.get_pizzas()[0].get_toppings() == ['olives', 'chicken']

    assert order.get_pizzas()[1].get_type() == 'vegetarian'
    assert order.get_pizzas()[1].get_size() == 'small'
    assert order.get_pizzas()[1].get_toppings() == ['beef', 'chicken']

    pizza_info = ['pepperoni', 'small', ['beef']]
    order.add_pizza(pizza_info)
    assert order.get_pizzas()[2].get_type() == 'pepperoni'
    assert order.get_pizzas()[2].get_size() == 'small'
    assert order.get_pizzas()[2].get_toppings() == ['beef']

def test_update_pizzas():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    order.update_pizzas([['vegetarian', 'small', ['beef']]])
    assert order.get_pizzas()[0].get_type() == 'vegetarian'
    assert order.get_pizzas()[0].get_size() == 'small'
    assert order.get_pizzas()[0].get_toppings() == ['beef']
    
    order.update_pizzas([['margherita', 'medium', ['tomatoes', 'olives']]])
    assert order.get_pizzas()[0].get_type() == 'margherita'
    assert order.get_pizzas()[0].get_size() == 'medium'
    assert order.get_pizzas()[0].get_toppings() == ['tomatoes', 'olives']

def test_add_drink():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    order.add_drink(['coke','medium'])
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'coke'
    assert order.get_drinks()[1].get_size() == 'medium'

def test_update_drinks():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    order.update_drinks([['coke', 'small'], ['pepsi', 'medium']])
    assert order.get_drinks()[0].get_type() == 'coke'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'pepsi'
    assert order.get_drinks()[1].get_size() == 'medium'

def test_update_delivery_info():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    delivery_info = {'order_number': 1, 'address': '200 college street Toronto ON', 
            'details': 'Please meet me downstairs', 'delivery_number': 15}
    order.update_delivery_info(delivery_info)
    assert order.delivery_info is delivery_info
    assert not order.pickup

    delivery_info = {'order_number': 1, 'address': '300 college street Toronto ON', 
            'details': 'Please meet me outside', 'delivery_number': 16}
    order.update_delivery_info(delivery_info)
    assert order.delivery_info is delivery_info
    assert not order.pickup

def test_get_delivery_info():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_delivery_info() == {}
    delivery_info = {'order_number': 1, 'address': '200 college street Toronto ON', 
            'details': 'Please meet me downstairs', 'delivery_number': 15}
    order.update_delivery_info(delivery_info)
    assert order.get_delivery_info() is delivery_info

def test_get_pickup():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert not order.get_pickup()
    order.pickup = False
    assert not order.get_pickup()
    order.pickup = True
    assert order.get_pickup()

def test_set_pickup():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    order.set_pickup(True)
    assert order.pickup
    order.set_pickup(False)
    assert not order.pickup

def test_get_order_number():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_order_number() == 1

    order = Order(2, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_order_number() == 2

def test_get_pizzas():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_pizzas()[0].get_type() == 'pepperoni'
    assert order.get_pizzas()[0].get_size() == 'medium'
    assert order.get_pizzas()[0].get_toppings() == ['olives', 'chicken']
    
    order = Order(2, [['vegetarian', 'small', ['chicken']]], 
            [['pepsi', 'small']])
    assert order.get_pizzas()[0].get_type() == 'vegetarian'
    assert order.get_pizzas()[0].get_size() == 'small'
    assert order.get_pizzas()[0].get_toppings() == ['chicken']

    order.add_pizza(['pepperoni', 'small', ['beef']])
    assert order.get_pizzas()[1].get_type() == 'pepperoni'
    assert order.get_pizzas()[1].get_size() == 'small'
    assert order.get_pizzas()[1].get_toppings() == ['beef']

def test_get_drinks():
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'

    order = Order(2, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['coke', 'medium'], ['pepsi', 'medium']])
    assert order.get_drinks()[0].get_type() == 'coke'
    assert order.get_drinks()[0].get_size() == 'medium'
    assert order.get_drinks()[1].get_type() == 'pepsi'
    assert order.get_drinks()[1].get_size() == 'medium'

    order.add_drink(['coke', 'small'])
    assert order.get_drinks()[2].get_type() == 'coke'
    assert order.get_drinks()[2].get_size() == 'small'

def test_get_price():
    with open('data.json') as f:
        data = json.load(f)
    order = Order(1, [['pepperoni', 'medium', ['olives', 'chicken']]], 
            [['pepsi', 'small']])
    price = data['pizza']['pepperoni']['medium']
    price += data['topping']['olives']
    price += data['topping']['chicken']
    price += data['drink']['pepsi']['small']
    assert order.get_price() == price

    order = Order(2, [['vegetarian', 'small', ['beef']]], 
            [['pepsi', 'small'], ['coke', 'medium']])
    price = data['pizza']['vegetarian']['small']
    price += data['topping']['beef']
    price += data['drink']['pepsi']['small']
    price += data['drink']['coke']['medium']
    assert order.get_price() == price
