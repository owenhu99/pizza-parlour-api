from pizza_parlour import app


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

def test_crud():
    ## Create order ##
    # 200 response
    order = {
        "pizzas": [
            {"type": "pepperoni", "size": "small", "toppings": "mushrooms"}
        ],
        "drinks": [
            {"type": "coke", "size": "medium"}
        ]
    }
    response = app.test_client().post('/v1/orders', json=order)
    assert response.status_code == 200
    assert isinstance((response.json)['order_number'], int)

    # 400 responses
    order = {
        "pizzas": [
            {"size": "small", "toppings": "mushrooms"}
        ],
        "drinks": [
            {"type": "coke", "size": "medium"}
        ]
    }
    response = app.test_client().post('/v1/orders', json=order)
    assert response.status_code == 400

    response = app.test_client().post('/v1/orders')
    assert response.status_code == 400

    # 204 responses
    order = {
        "pizzas": [
            {"type": "pepperon", "size": "small", "toppings": "mushrooms"}
        ],
        "drinks": [
            {"type": "coke", "size": "medium"}
        ]
    }
    response = app.test_client().post('/v1/orders', json=order)
    assert response.status_code == 204


    ## Read order ##
    # 200 response
    response = app.test_client().get('/v1/orders/1')
    assert response.status_code == 200


    ## Update order ##
    # 200 response
    order = {
        "pizzas": [
            {"type": "pepperoni", "size": "medium", "toppings": "mushrooms"}
        ],
        "drinks": []
    }
    response = app.test_client().put('/v1/orders/1', json=order)
    assert response.status_code == 200

    # 204 response
    order = {
        "pizzas": [
            {"type": "pepperon", "size": "medium", "toppings": "mushrooms"}
        ],
        "drinks": []
    }
    response = app.test_client().put('/v1/orders/1', json=order)
    assert response.status_code == 204


    ## Delivery ##
    # 200 response
    delivery_info = {
        "order_number": 1,
        "address": "1001 bay",
        "details": "no green onions",
        "delivery_number": "inhouse2"
    }
    response = app.test_client().post('/v1/orders/inhouse', json=delivery_info)
    assert response.status_code == 200

    delivery_info = {
        "order_number": 1,
        "address": "1001 bay",
        "details": "no green onions",
        "delivery_number": "ubereats14"
    }
    response = app.test_client().post('/v1/orders/ubereats', json=delivery_info)
    assert response.status_code == 200

    delivery_info = "order_number,address,details,delivery_number\n1,1001 bay,no green onions,foodora13"
    response = app.test_client().post('/v1/orders/foodora', data=delivery_info)
    assert response.status_code == 200

    # 204 responses
    delivery_info = {
        "order_number": 2,
        "address": "1001 bay",
        "details": "no green onions",
        "delivery_number": "ubereats14"
    }
    response = app.test_client().post('/v1/orders/ubereats', json=delivery_info)
    assert response.status_code == 204
    response = app.test_client().post('/v1/orders/inhouse', json=delivery_info)
    assert response.status_code == 204

    delivery_info = "order_number,address,details,delivery_number\n2,1001 bay,no green onions,foodora13"
    response = app.test_client().post('/v1/orders/foodora', data=delivery_info)
    assert response.status_code == 204

    # 400 responses
    delivery_info = {
        "order_numbe": 2,
        "address": "1001 bay",
        "details": "no green onions",
        "delivery_number": "ubereats14"
    }
    response = app.test_client().post('/v1/orders/ubereats', json=delivery_info)
    assert response.status_code == 400
    response = app.test_client().post('/v1/orders/inhouse', json=delivery_info)
    assert response.status_code == 400

    ## Delete order ##
    response = app.test_client().delete('/v1/orders/1')
    assert response.status_code == 200
    response = app.test_client().delete('/v1/orders/1')
    assert response.status_code == 204