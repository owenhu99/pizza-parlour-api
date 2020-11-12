import json
from flask import Flask, request, jsonify
from order_manager import OrderManager
from order import Order

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
    pizzas, drinks = [], []
    for pizza in request.json['pizzas']:
        pizzas.append([
            pizza['type'],
            pizza['size'],
            [x.strip() for x in pizza['toppings'].split()]
        ])
    for drink in request.json['drinks']:
        drinks.append([
            drink['type'],
            drink['size']
        ])
    order_num = orderManager.order(pizzas, drinks)
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
        return jsonify({})
    return no_content_found()

@app.route('/v1/orders/delivery', methods=['POST'])
def api_delivery():
    """Change order to be delivered
    json format:
    {
        "order_number": "<system order number>",
        "address": "<address>",
        "details": "<order details>",
        "delivery_number": "<partner order number>",
        "platform": "<delivery platform>"
    }
    """
    keys = ["order_number", "address", "details", "delivery_number", "platform"]
    if (not request.json) or (not all(key in request.json for key in keys)) \
    or (request.json["platform"] not in ["foodora", "ubereats", "in-house"]):
        return bad_request(400)
    if orderManager.change_to_delivery(request.json):
        return jsonify({})
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

if __name__ == "__main__":
    app.run()
