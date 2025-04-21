'''
Online Ordering System Implementation using OOP

Each restaurant should have:

restaurant_id (string) - Unique identifier.
name (string) - The restaurant's name.
menu (dict) - Stores food items and their prices {item_name: price}.
orders (list) - A list of pending orders (order objects).
'''

class Restaurant:

    def __init__(self, res_id: str, res_name):

        self.name = res_name
        self.menu = {}
        self.orders = []
        self.restaurant_id = res_id


    def add_to_menu(self, item_name, price) -> None:

        self.menu[item_name] = float(price)


    def place_order(self, order):

        if order not in self.orders:
            self.orders.append(order)

    def complete_order(self):

        completed_order = self.orders.pop(0)
        return completed_order

class Customer:

    def __init__(self, customer_name, customer_id):

        self.name = customer_name
        self.order_history = []
        self.id = customer_id

class Order:

    def __init__(self, customer_id: str, res_id: str, items: dict):

        self.order_id = ''
        self.customer_id = customer_id
        self.res_id = res_id
        self.items = items
        self.total_price = 0

    def calculate_total(self, menu: dict):
        total = 0

        for item in self.items:
            if item in menu:
                total += round(menu[item] * self.items[item], 2)

        # update the order total
        self.total_price = total


class OrderingSystem:

    def __init__(self):
        # store ids pointing to customer objects
        self.customers = {}

        # res ids pointing to a res object
        self.restaurants = {}
        self.order_id = 1


    def register_customer(self, name, customer_id):

        if customer_id not in self.customers:

            customer = Customer(name, customer_id)
            self.customers[customer_id] = customer

    def add_restaurant(self, restaurant: object):

        self.restaurants[restaurant.restaurant_id] = restaurant

    def place_order(self, customer_id: str, restaurant_id: str, items: dict):

        # create order, update order it, and update it for next order
        if restaurant_id not in self.restaurants:
            return False

        if customer_id not in self.customers:
            return False

        # get restaurant
        restaurant = self.restaurants.get(restaurant_id)

        order = Order(customer_id, restaurant_id, items)
        order.order_id = self.order_id
        # update order total based on items
        order.calculate_total(restaurant.menu)

        # place order at restaurant
        restaurant.place_order(order)

        # update order id for next order
        self.order_id += 1
        return True

    def complete_order(self, restaurant_id):

        # not sure if need to check this again
        restaurant = self.restaurants.get(restaurant_id, None)

        # complete the first order in queue
        if restaurant is None:
            return False

        completed_order = restaurant.complete_order()

        # update the customer
        self.customers[completed_order.customer_id].order_history.append(completed_order)



