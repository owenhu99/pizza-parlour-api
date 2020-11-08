from pizza import Pizza
import random
import os.path
import json

def test_get_size():
    pizza = Pizza(['pepperoni', 'small', ['chicken', 'olives']])
    assert pizza.get_type() == 'pepperoni'

    pizza = Pizza(['vegetarian', 'medium', ['beef', 'olives']])
    assert pizza.get_type() == 'vegetarian'

def test_get_type():
    pizza = Pizza(['pepperoni', 'small', ['chicken', 'olives']])
    assert pizza.get_size() == 'small'

    pizza = Pizza(['vegetarian', 'medium', ['beef', 'olives']])
    assert pizza.get_size() == 'medium'

def test_get_toppings():
    pizza = Pizza(['pepperoni', 'small', ['chicken', 'olives']])
    assert pizza.get_toppings() == ['chicken', 'olives']

    pizza = Pizza(['vegetarian', 'medium', ['beef', 'olives']])
    assert pizza.get_toppings() == ['beef', 'olives']

def test_update():
    pizza = Pizza(['pepperoni', 'small', ['chicken', 'olives']])
    assert pizza.get_size() == 'small' 
    pizza.update([-1, 'medium', -1])
    assert pizza.get_size() == 'medium'

    pizza = Pizza(['vegetarian', 'medium', ['beef', 'olives']])
    assert pizza.get_type() == 'vegetarian'
    pizza.update(['pepperoni', -1, -1])
    assert pizza.get_type() == 'pepperoni'

    pizza = Pizza(['vegetarian', 'small', ['chicken', 'beef']])
    assert pizza.get_toppings() == ['chicken', 'beef']
    pizza.update([-1, -1, ['olives']])
    assert pizza.get_toppings() == ['olives']

def test_get_price():
    with open(os.path.dirname(__file__) + '/../data.json')  as f:
        data = json.load(f)
    pizza = Pizza(['vegetarian', 'medium', ['beef', 'olives']])
    price = data['pizza']['vegetarian']['medium']
    price += data['topping']['beef']
    price += data['topping']['olives']
    assert pizza.get_price() == price

    pizza = Pizza(['vegetarian', 'small', ['chicken', 'beef']])
    price = data['pizza']['vegetarian']['small']
    price += data['topping']['chicken']
    price += data['topping']['beef']
    assert pizza.get_price() == price

def test_check_inputs():
    pizza = Pizza(['pepperoni', 'medium', ['olives', 'beef']])
    assert pizza.check_inputs(['pepperoni', 'medium', ['olives', 'beef']]) == True
    assert pizza.check_inputs(['vegetarian', 'small', ['chicken']]) == True
    assert pizza.check_inputs(['pepperoni', 'medium', []]) == True
    assert pizza.check_inputs(['invalid', 'medium', ['olives', 'beef']]) == False
    assert pizza.check_inputs(['invalid', 'invalid', ['olives', 'beef']]) == False
    assert pizza.check_inputs(['invalid', 'medium', ['invalid', 'beef']]) == False
    assert pizza.check_inputs(['invalid', 'medium', 'invalid']) == False

def manual_price_update():
    pizza = Pizza(['vegetarian', 'medium', ['chicken', 'beef']])
    rand1 = random.randint(1,100)
    price1 = pizza.manual_price_update(rand1)
    assert price1 == rand1

    rand2 = random.randint(1,100)
    price2 = pizza.manual_price_update(rand2)
    assert price2 == rand2
