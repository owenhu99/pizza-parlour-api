# Pair Programming and program design

## First feature - "Submit a new order"

**Driver**: Charlie

**Navigator**: Xiao (Owen)

During the planning, we looked at how to set up the class components required for the pizza parlour and how they depend on each other. 

We decided to use set up an `Order` class to store information about an order, a `Drink` class and a `Pizza` class to store the specific items in the order, and an `OrderManager` class to store the active orders and manage them. 

`OrderManager` acts as a factory method that creates instances of `Order` and stores them in a list. It also has methods to update and retrieve order information.

During the coding session, we decided that it might be useful to setup a `FoodItem` superclass that `Drink` and `Pizza` inherits from to reuse code, implement polymorphism and adds scalability. We didn't implement it during this session, but it was later added.

We also decided to store the menu/item information locally in a JSON file. The file is read to check for validity of user input. We can add pizza types, toppings, drink types and all of the prices simply by editing the JSON file. There is no need for changing the codebase.

## Second feature - "Ask for pickup or delivery"

**Driver**: Xiao (Owen)

**Navigator**: Charlie

During the planning, we looked at how to implement pickup and delivery functionalities. We first thought about having a `DeliveryManager` class similar to `OrderManager` which can manage the orders stored inside a `OrderManager` object, however, that would create too much coupling between `OrderManager` and `DeliveryManager`.

Then, we decided to add a list of pickup orders and a list of delivery orders to the `OrderManager` class, and move orders to these lists accordingly. However, this means that every time we look up an order, we would have to look through all three lists and check which list it belongs to. This was shown to be unnecessary as well, since we have to expand the `Order` classes to include the delivery information anyway.

Therefore, we decided to add an extra dictionary attribute `delivery_info` to the `Order` class that contains all the delivery information and it would be empty when the order is not to be delivered. We also added a boolean attribute `pickup` to indicate whether the order is to be picked up.

During coding, we interpreted the "Address", "Order Details", "Order Number" in the delivery specifications as customer address, delivery instructions, and delivery number, respectively. We pictured the workflow of the delivery service as: the delivery platform makes an API call to get our menu, an API call to create an order, and another API call to change that default order to a delivered order.So, we kept the route to create an order, and added new routes to change existing orders to include the delivery information or set a "to be picked up" flag. 

We implemented the Foodora port to take JSON input for the coding session since we were not sure what the specification meant. We later modified the route to parse the payload as CSV.

## Reflection

**Positives:**

- We were catching a lot of each other's errors before the code was run

- We were able to give each other styling and general coding suggestions

- Allowed us to make real time design decisions together instead of just doing something beceause it seems like a good idea at the time

- Debugging was faster when there were more than one person looking at the code

**Negatives**

- We were more used to coding by ourselves, so pair programming made us a bit self-conscious and thus slowed down the efficiency a bit

- The navigator was not very useful during long coding sessions, and it's difficult to stay focused watching your partner code

- In a small project, having two people code at the same time may still be faster overall than one person coding while having the benefits of the navigator watching

# Program Design

## Design Patterns

## Relationships Between Objects

- Our code has relatively high cohesion and groups data into objects that would understandably represent them. The food_item classes all are simple and use all of their data well and often. Order and order_manager store the relevant data and have the needed methods to get, set, and check everything.

- The way we set up our code with the order manager keeping track of orders, which hold objects for pizzas and drinks, which then hold their own information all means that the coupling stays low. Data stays where it is held and is only used to be given to the user or stored into an object.

## Function Design

# Code Craftsmanship

## Pylint

We used Pylint's default settings with a few ignored minor errors that were not easily fixable.

- Missing module docstring: this error was ignored because it is occuring when we import libraries that are missing docstrings.

- Import error: this error was ignored because some local modules were not recognized or found in the Python path, even though the imports are legal and successful.

- Consider using enumerate: this error was ignored because it occured when an index is required for two lists of the same length, so iterating one list does not work.

- Unused argument: this error was ignored because functions replacing default errorhandlers required an argument, but it is not used in our implementation of it.
