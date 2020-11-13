from pizza_parlour import app
from order import Order

def test_pizza():
    """Test index page routing"""
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Welcome to the Pizza Parlour'

def test_menu():
    """Test full menu GET request"""
    response = app.test_client().get('/v1/resources/menu/all')

    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_item():
    """Test specific item GET request"""
    # 404 reponses
    response = app.test_client().get('/v1/resources/menu?')
    assert response.status_code == 404

    response = app.test_client().get('/v1/resources/menu?itype=pizza')
    assert response.status_code == 404

    response = app.test_client().get('/v1/resources/menu?itype=pizza&item=pepperoni')
    assert response.status_code == 404

    response = app.test_client().get('/v1/resources/menu?item=pepperoni')
    assert response.status_code == 404

    # 204 responses
    response = app.test_client().get('/v1/resources/menu?item=p&itype=pizza&size=small')
    assert response.status_code == 204

    response = app.test_client().get('/v1/resources/menu?item=pepperoni&itype=p&size=small')
    assert response.status_code == 204

    response = app.test_client().get('/v1/resources/menu?item=pepperoni&itype=pizza&size=s')
    assert response.status_code == 204

    response = app.test_client().get('/v1/resources/menu?itype=topping&item=b')
    assert response.status_code == 204

    # 200 responses
    response = app.test_client().get('/v1/resources/menu?itype=topping&item=beef')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance((response.json)['price'], int)

    response = app.test_client().get('/v1/resources/menu?itype=pizza&item=pepperoni&size=small')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance((response.json)['price'], int)
