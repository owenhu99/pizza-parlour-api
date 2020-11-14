
# Pizza Parlour API

CSC301 Introduction to Software Engineering - Assignment 2

Read `REPORT.md` for the assignment report.

# Getting started

Install required package `pip install flask`

Run the API server by running `python3 pizza_parlour.py`

# Unit Testing

Install required package `pip install coverage pytest`

Run unit tests with coverage by running `coverage run -m pytest && coverage report -m`

# API Documentation

PizzaParlour API offers services to create and manage pizza orders and get various resources.

## Basic information

We provide data in JSON format.

The root address is `http://127.0.0.1:5000/`

## Routes

### *POST* /v1/orders 

This route is used to create an order at the pizza parlour. It takes a JSON body with the following format.

```
{
	"pizzas": [
		{"type": str, "size": str, "toppings": comma-separated-str},
		{"type": str, "size": str, "toppings": comma-separated-str},
		...
	],
	"drinks": [
		{"type": str, "size": str},
		{"type": str, "size": str},
		...
	]
}
```
The JSON body must contain keys `pizzas` and `drinks`.

`pizzas` must contain a JSON array, possibly empty, with keys `type`, `size`, `toppings`, each with string values. `toppings` must be a string of toppings separated by commas, white space allowed.

`drinks` must contain a JSON array, possibly empty, with keys `type` and `size`, each with string values.

All values must be valid according to the pizza parlour's menu, otherwise a ***204 NO CONTENT FOUND*** will be returned.

If the JSON is missing any key or contains invalid keys, a ***400 BAD REQUEST*** will be returned

On success, a JSON `{"order_number": order_number}` will be returned with the order number of the created order.

### *GET* /v1/orders/<order_number>

This route is used to get an order's information. No parameter is needed, the order number is provided as part of the URL in place of <order_number>.

If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

On success, a JSON will be returned in the form of:
```
{
	"pizzas": [
		{"type": str, "size": str, "toppings": [topping1, topping2, ...]},
		{"type": str, "size": str, "toppings": [topping1, topping2, ...]},
		...
	],
	"drinks": [
		{"type": str, "size": str},
		{"type": str, "size": str},
		...
	],
	"order_number": int,
	"total": int,
	"pickup": boolean,
	"delivery_info": {
		"order_number": int,
		"address": str,
		"details": str,
		"delivery_number": str
	}
}
```

### *DELETE* /v1/orders/<order_number>

This route is used to cancel an order. No parameter is needed, the order number is provided as part of the URL in place of <order_number>.

If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

On success, a JSON `{"cancelled_order": order_number}` will be returned with the number of the order that was successfully cancelled.

### *PUT* /v1/orders/<order_number>

This route is used to update an order at the pizza parlour. The order number is provided as part of the URL in place of <order_number>. It takes a JSON body with the following format:

```
{
	"pizzas": [
		{"type": str, "size": str, "toppings": comma-separated-str},
		{"type": str, "size": str, "toppings": comma-separated-str},
		...
	],
	"drinks": [
		{"type": str, "size": str},
		{"type": str, "size": str},
		...
	]
}
```
The JSON body must contain key `pizzas` **OR** `drinks`.

`pizzas` must contain a JSON array, possibly empty, with keys `type`, `size`, `toppings`, each with string values. `toppings` must be a string of toppings separated by commas, white space allowed.

`drinks` must contain a JSON array, possibly empty, with keys `type` and `size`, each with string values.

All values must be valid according to the pizza parlour's menu, otherwise a ***204 NO CONTENT FOUND*** will be returned.

If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

If the JSON is missing any key or contains invalid keys, a ***400 BAD REQUEST*** will be returned

On success, a `GET /v1/orders/<order_number>` request is called and the response of the GET request will be returned.

### *POST* /v1/orders/pickup

This route is used to change an existing order to be picked up. It takes a JSON body with the format `{"order_number": int}` where the integer is the order number.

If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

If the JSON body is missing the `order_number` key, a ***400 BAD REQUEST*** will be returned.

On success, a `GET /v1/orders/<order_number>` request is called and the response of the GET request will be returned.

### *POST* /v1/orders/ubereats or /v1/orders/inhouse

This route is used to change an existing order to be delivered via UberEats or in-house, respectively. It takes a JSON body with the following format:
```
"delivery_info": {
	"order_number": int,
	"address": str,
	"details": str,
	"delivery_number": str
}
```

All keys must be present, otherwise a ***400 BAD REQUEST*** will be returned.

`order_number` is the number of the existing order to be delivered. If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

`address`, `details`, and `delivery_number` must be string values.

The value of `delivery_info` will replace the `delivery_info` of the corresponding order.

On success, a `GET /v1/orders/<order_number>` request is called and the response of the GET request will be returned.

### *POST* /v1/orders/foodora

This route is used to change an existing order to be delivered via Foodora. It takes a text body that is in a CSV format with the headers `order_number,address,details,delivery_number`.

Only the first line of values after the headers is parsed, since each header is only supposed to correspond to one value. For example, `order_number,address,details,delivery_number\n1,321 Bloor St. W.,no green onions,foodora13` will be parsed into a JSON:
```
"delivery_info": {
	"order_number": 1,
	"address": "321 Bloor St. W.",
	"details": "no green onions",
	"delivery_number": "foodora13"
}
```
`order_number` is the number of the existing order to be delivered. If no order is found with the order number provided, a ***204 NO CONTENT FOUND*** will be returned.

`address`, `details`, and `delivery_number` must be string values.

The value of `delivery_info` will replace the `delivery_info` of the corresponding order.

On success, a `GET /v1/orders/<order_number>` request is called and the response of the GET request will be returned.

### *GET* /v1/resources/menu/all

This route is used to get the full menu with prices of the pizza parlour. No parameter is needed.

It returns the JSON of the menu, where the first layer is the item type, second layer is the item name, third layer, when applicable, is the size, and the final values are the prices. For example:
``` JSON
{
	"pizza": {
		"pepperoni": {"small": 10, "medium": 15},
		"margherita": {"small": 9, "medium": 14},
		"vegetarian": {"small": 8, "medium": 13},
		"neapolitan": {"small": 10, "medium": 15}
	},
	"drink": {
		"coke": {"small": 2, "medium": 2.50},
		"diet coke": {"small": 2, "medium": 2.50},
		"coke zero": {"small": 2, "medium": 2.50},
		"pepsi": {"small": 2, "medium": 2.50},
		"diet pepsi": {"small": 2, "medium": 2.50},
		"dr pepper": {"small": 2, "medium": 2.50},
		"water": {"small": 1, "medium": 1.50},
		"juice": {"small": 2, "medium": 2.50}
	},
	"topping": {
		"olives": 1,
		"tomatoes": 1,
		"mushrooms": 1,
		"jalapenos": 1,
		"chicken": 3,
		"beef": 3,
		"pepperoni": 3
	}
}
```

### *GET* /v1/resources/menu

This route is used to get the price of a specific menu item. It takes three possible parameters, `itype`, `item` and `size`.

If `itype=topping`, `size` is not necessary. If `itype=pizza` or `itype=drink`, `item` and `size` are needed. Otherwise, a ***404 PAGE NOT FOUND*** will be returned.

If the values of the parameters are not found on the menu, a ***204 NO CONTENT FOUND*** will be returned.

On success, a JSON body `{"price": int}` is returned where int is the price of the item. 