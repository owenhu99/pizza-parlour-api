import json
from flask import Flask, request, jsonify
from src.order_manager import OrderManager
from src.custom_exception import InvalidInputException

app = Flask("Assignment 2")
orderManager = OrderManager()
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def index():
    """Index page"""
    return 'Welcome to the Pizza Parlour'

@app.errorhandler(404)
def page_not_found(err):
    """404 Response"""
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(400)
def bad_request(err):
    """400 Response"""
    return "<h1>400</h1><p>Bad Request.</p>", 400

def no_content_found():
    """204 Response"""
    return "<h1>204</h1><p>No content found.</p>", 204

@app.route('/v1/orders/<int:order_number>', methods=['GET'])
def api_get_order(order_number):
    """Get order by order number"""
    order = orderManager.get_order(order_number)
    if order:
        return jsonify({
            'order_number': order_number,
            'pizzas': [pizza.get_dict() for pizza in order.get_pizzas()],
            'drinks': [drink.get_dict() for drink in order.get_drinks()],
            'total': order.get_price(),
            'pickup': order.get_pickup(),
            "delivery_info": order.get_delivery_info()
        })
    print("Error: No order found with the order number: " + str(order_number))
    return no_content_found()

@app.route('/v1/orders/<int:order_number>', methods=['PUT'])
def api_update_order(order_number):
    """Update order by order number

    json must contain key "pizzas" or "drinks",
    "pizzas" must be a json array with the format:
    {"type": str, "size": str, "toppings": comma-separated-str}
    "drinks" must be a json array with the format:
    {"type": str, "size": str}

    The value of "pizzas" and "drinks" OVERWRITES those of the order
    """
    order = orderManager.get_order(order_number)
    if not order:
        return no_content_found()
    if not request.json or ("pizzas" not in request.json and "drinks" not in request.json):
        return bad_request(400)
    if "pizzas" in request.json:
        try:
            order.update_pizzas(_parse_dict_to_array(request.json["pizzas"]))
        except InvalidInputException:
            return no_content_found()
    if "drinks" in request.json:
        try:
            order.update_drinks(_parse_dict_to_array(request.json["drinks"]))
        except InvalidInputException:
            return no_content_found()
    return jsonify({})

@app.route('/v1/orders/<int:order_number>', methods=['DELETE'])
def api_cancel_order(order_number):
    """Cancel order by order number"""
    if orderManager.cancel_order(order_number):
        return jsonify({'cancelled_order': order_number})
    return no_content_found()

@app.route('/v1/orders', methods=['POST'])
def api_create_order():
    """Create an order
    json format:
    {
        'pizzas': [
            {'type': '<type>", 'size': '<size>', 'toppings': '<topping1>, <topping2>, ...'},
            {'type': '<type>", 'size': '<size>', 'toppings': '<topping1>, <topping2>, ...'},
            ...
        ],
        'drinks': [
            {'type': '<type>', 'size': '<size>'},
            {'type': '<type>', 'size': '<size>'},
            ...
        ]
    }
    """
    if not request.json or not 'pizzas' in request.json or not 'drinks' in request.json:
        return bad_request(400)
    pizzas = _parse_dict_to_array(request.json["pizzas"])
    drinks = _parse_dict_to_array(request.json["drinks"])
    if KeyError in (pizzas, drinks):
        return bad_request(400)
    try:
        order_num = orderManager.order(pizzas, drinks)
    except InvalidInputException:
        return no_content_found()
    return jsonify({'order_number': order_num})

@app.route('/v1/orders/pickup', methods=['POST'])
def api_pickup():
    """Change order to be picked up
    json format:
    {
        "order_number": "<system order number>"
    }
    """
    if not request.json or "order_number" not in request.json:
        return bad_request(400)
    if orderManager.change_to_pickup(request.json["order_number"]):
        return api_get_order(request.json["order_number"])
    return no_content_found()

@app.route('/v1/orders/ubereats', methods=['POST'])
def api_ubereats_delivery():
    """Change order to be delivered
    json format:
    {
        "order_number": "<system order number>",
        "address": "<address>",
        "details": "<order details>",
        "delivery_number": "<partner order number>"
    }
    """
    keys = ["order_number", "address", "details", "delivery_number"]
    if (not request.json) or (not all(key in request.json for key in keys)):
        return bad_request(400)
    request.json["platform"] = "ubereats"
    if orderManager.change_to_delivery(request.json):
        return api_get_order(request.json["order_number"])
    return no_content_found()

@app.route('/v1/orders/foodora', methods=['POST'])
def api_foodora_delivery():
    """Change order to be delivered via UberEats"""
    body = request.data.decode("utf-8").splitlines()
    header = [x.strip() for x in body[0].split(',')]
    if set(header) != set(["order_number", "address", "details", "delivery_number"]):
        return bad_request(400)
    info = [x.strip() for x in body[1].split(',')]
    delivery_info = {}
    for i in range(len(header)):
        delivery_info[header[i]] = info[i]
    delivery_info["platform"] = "foodora"
    delivery_info["order_number"] = int(delivery_info["order_number"])
    if orderManager.change_to_delivery(delivery_info):
        return api_get_order(delivery_info["order_number"])
    return no_content_found()

@app.route('/v1/orders/inhouse', methods=['POST'])
def api_inhouse_delivery():
    """Change order to be delivered in-house"""
    keys = ["order_number", "address", "details", "delivery_number"]
    if (not request.json) or (not all(key in request.json for key in keys)):
        return bad_request(400)
    request.json["platform"] = "inhouse"
    if orderManager.change_to_delivery(request.json):
        return api_get_order(request.json["order_number"])
    return no_content_found()

@app.route('/v1/resources/menu/all', methods=['GET'])
def api_all():
    """Return full menu as JSON"""
    return jsonify(data)

@app.route('/v1/resources/menu', methods=['GET'])
def api_item():
    """Return price for specific item"""
    query_parameters = request.args

    itype = query_parameters.get('itype')
    item = query_parameters.get('item')
    size = query_parameters.get('size')

    if itype == 'topping' and item:
        try:
            result = data[itype][item]
        except KeyError as err:
            print("KeyError: {0}".format(err))
            return no_content_found()
    elif itype and item and size:
        try:
            result = data[itype][item][size]
        except KeyError as err:
            print("KeyError: {0}".format(err))
            return no_content_found()
    else:
        return page_not_found(404)

    return jsonify(price=result)

def _parse_dict_to_array(item_list):
    """Helper function that changes a list of dicts to a list of arrays
    Input:
    [{"type": type_str, "size": size_str, "toppings": toppings_str}, {...}, ...]
    Output:
    [[type_str, size_str, [topping1, topping2, ...]], [...], ...]

    Input must have keys "type" and "size'
    "toppings" must be comma separated (whitespace ok) and is optional
    """
    out = []
    if len(item_list) == 0:
        return out
    if "type" not in item_list[0] or "size" not in item_list[0]:
        return KeyError
    if "toppings" in item_list[0]:
        # for pizza
        for pizza in item_list:
            out.append([
                pizza['type'],
                pizza['size'],
                [x.strip() for x in pizza['toppings'].split(',') if x != '']
            ])
    else:
        for drink in item_list:
            out.append([
                drink['type'],
                drink['size']
            ])
    return out

if __name__ == "__main__":
    app.run()
