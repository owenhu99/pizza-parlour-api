from drink import Drink
import random
import os.path
import json

def test_get_size():
    drink = Drink(['coke', 'medium'])
    assert drink.get_size() == 'medium'

    drink = Drink(['coke', 'small'])
    assert drink.get_size() == 'small'

def test_get_type():
    drink = Drink(['coke', 'medium'])
    assert drink.get_type() == 'coke'

    drink = Drink(['pepsi', 'medium'])
    assert drink.get_type() == 'pepsi'

def test_get_price():
    drink = Drink(['coke', 'medium'])
    with open(os.path.dirname(__file__) + '/../data.json') as f:
        data = json.load(f)
    assert drink.get_price() == data['drink']['coke']['medium']

    drink = Drink(['pepsi', 'small'])
    assert drink.get_price() == data['drink']['pepsi']['small']

def test_manual_price_update():
    drink = Drink(['coke', 'medium'])
    rand1 = random.randint(1,100)
    price1 = drink.manual_price_update(rand1)
    assert price1 == rand1

    rand2 = random.randint(1,100)
    price2 = drink.manual_price_update(rand2)
    assert price2 == rand2

def test_update():
    drink = Drink(['coke', 'medium'])
    drink.update(['pepsi', -1])
    assert drink.get_type() == 'pepsi'

    drink.update([-1, 'small'])
    assert drink.get_size() == 'small'
    
    drink.update(['invalid', 'invalid'])
    assert drink.get_type() == 'pepsi'
    assert drink.get_size() == 'small'

def test_check_inputs():
    drink = Drink(['coke', 'small'])
    assert drink.check_inputs(['coke', 'small'])
    assert drink.check_inputs(['pepsi', 'medium'])
    assert not drink.check_inputs(['invalid', 'small'])
    assert not drink.check_inputs(['coke', 'invalid'])

