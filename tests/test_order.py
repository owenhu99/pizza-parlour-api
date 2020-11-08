from order import Order
import json

def test_order():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    assert order.get_order_number() == 1
    assert order.get_pizza().get_type() == 'pepperoni'
    assert order.get_pizza().get_size() == 'medium'
    assert order.get_pizza().get_toppings() == ['olives', 'chicken']
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'

    order = Order(2, 'vegetarian', 'small', ['beef'], [['pepsi', 'small'], ['coke', 'medium']])
    assert order.get_order_number() == 2
    assert order.get_pizza().get_type() == 'vegetarian'
    assert order.get_pizza().get_size() == 'small'
    assert order.get_pizza().get_toppings() == ['beef']
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'coke'
    assert order.get_drinks()[1].get_size() == 'medium'

    try:
        order = Order(3, 'invalid', 'invalid', ['invalid'], [['invalid', 'invalid']])
        assert False
    except:
        assert True

    try:
        order = Order(4, 'pepperoni', 'small', 'invalid', [['coke', 'small']])
        assert False
    except:
        assert True

    try:
        order = Order(5, 'pepperoni', 'small', ['beef'], ['invalid'])
        assert False
    except:
        assert True

    try:
        order = Order(6, 'pepperoni', 'small', ['beef'], 'invalid')
        assert False
    except:
        assert True

def test_update_pizza():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    order.update_pizza('vegetarian', 'small', ['beef'])
    assert order.get_pizza().get_type() == 'vegetarian'
    assert order.get_pizza().get_size() == 'small'
    assert order.get_pizza().get_toppings() == ['beef']
    
    order.update_pizza('margherita', 'medium', ['tomatoes', 'olives'])
    assert order.get_pizza().get_type() == 'margherita'
    assert order.get_pizza().get_size() == 'medium'
    assert order.get_pizza().get_toppings() == ['tomatoes', 'olives']

def test_add_drink():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    order.add_drink(['coke','medium'])
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'coke'
    assert order.get_drinks()[1].get_size() == 'medium'

def test_update_drinks():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    order.update_drinks([['coke', 'small'], ['pepsi', 'medium']])
    assert order.get_drinks()[0].get_type() == 'coke'
    assert order.get_drinks()[0].get_size() == 'small'
    assert order.get_drinks()[1].get_type() == 'pepsi'
    assert order.get_drinks()[1].get_size() == 'medium'

def test_get_order_number():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    assert order.get_order_number() == 1

    order = Order(2, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    assert order.get_order_number() == 2

def test_get_pizza():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    assert order.get_pizza().get_type() == 'pepperoni'
    assert order.get_pizza().get_size() == 'medium'
    assert order.get_pizza().get_toppings() == ['olives', 'chicken']
    
    order = Order(2, 'vegetarian', 'small', ['chicken'], [['pepsi', 'small']])
    assert order.get_pizza().get_type() == 'vegetarian'
    assert order.get_pizza().get_size() == 'small'
    assert order.get_pizza().get_toppings() == ['chicken']

def test_get_drinks():
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    assert order.get_drinks()[0].get_type() == 'pepsi'
    assert order.get_drinks()[0].get_size() == 'small'

    order = Order(2, 'pepperoni', 'medium', ['olives', 'chicken'], [['coke', 'medium'], ['pepsi', 'medium']])
    assert order.get_drinks()[0].get_type() == 'coke'
    assert order.get_drinks()[0].get_size() == 'medium'
    assert order.get_drinks()[1].get_type() == 'pepsi'
    assert order.get_drinks()[1].get_size() == 'medium'

def test_get_price():
    with open('data.json') as f:
        data = json.load(f)
    order = Order(1, 'pepperoni', 'medium', ['olives', 'chicken'], [['pepsi', 'small']])
    price = data['pizza']['pepperoni']['medium']
    price += data['topping']['olives']
    price += data['topping']['chicken']
    price += data['drink']['pepsi']['small']
    assert order.get_price() == price

    order = Order(2, 'vegetarian', 'small', ['beef'], 
            [['pepsi', 'small'], ['coke', 'medium']])
    price = data['pizza']['vegetarian']['small']
    price += data['topping']['beef']
    price += data['drink']['pepsi']['small']
    price += data['drink']['coke']['medium']
    assert order.get_price() == price


