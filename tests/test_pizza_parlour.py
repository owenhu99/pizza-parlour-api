from pizza_parlour import app
from order import Order
import random

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'


def test_order():
    first_rand = random.randint(1, 100)
    first_order = Order(first_rand)

    assert first_order.get_pizza() is False
    assert first_order.get_order_number() == first_rand
    assert first_order.get_drinks() == []

def test_update_pizza():
    assert True

def test_addDrink():
    assert True

def test_updateDrinks():
    assert True

def test_ready():
    assert True

