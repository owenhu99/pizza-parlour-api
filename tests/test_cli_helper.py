from src.cli_helper import CLIHelper

def test_send_order():
    order_dict = { 'pizzas': 
                    [ {'type': 'pepperoni', 'size': 'medium', 
                        'toppings': 'beef', 'chicken'}, 
                    {'type': 'vegetarian', 'size': 'small', 
                        'toppings': 'pepperoni'}], 
                    'drinks': 
                        [ {'type': 'coke', 'size': 'small'}, 
                        {'type': 'pepsi', 'size': 'medium'}]}
    response_info = CLIHelper.send_order(order_dict)
    assert response_info['response'] is not None
    assert response_info['status_code'] == 200
    assert response_info['body'] == order_dict

    order_dict = { 'pizzas': 
                    [ {'type': 'invalid', 'size': 'invalid', 
                        'toppings': 'pepperoni'}], 
                    'drinks': 
                        [ {'type': 'coke', 'size': 'small'}]}
    response_info = CLIHelper.send_order(order_dict)
    assert response_info['response'] is None
    assert response_info['body'] == order_dict

def test_get_order():
    assert True

def test_update_order():
    assert True

def test_delete_order():
    assert True

def test_pickup_order():
    assert True

def test_deliver_order_json():
    assert True

def test_deliver_order_csv():
    assert True

def test_get_menu():
    assert True
