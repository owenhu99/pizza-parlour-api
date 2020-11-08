from pizza_parlour import app
from order import Order
import random

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'



