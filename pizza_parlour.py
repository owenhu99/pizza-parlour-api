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
def page_not_found():
    """404 Response"""
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

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
            return "<h1>204</h1><p>No content found.</p>", 204
    elif itype and item and size:
        try:
            result = data[itype][item][size]
        except KeyError as err:
            print("KeyError: {0}".format(err))
            return "<h1>204</h1><p>No content found.</p>", 204
    else:
        return page_not_found()

    return jsonify(price=result)

if __name__ == "__main__":
    app.run()
