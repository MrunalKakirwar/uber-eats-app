# uber-eats-app
Features
Restaurant Search and Filter:

Filter restaurants by location and cuisine.
Browse a list of restaurants.
Menu Management:

View the menu of a specific restaurant.
Order Checkout:

Place an order with item price, tax calculation, and final amount.
Payment:

Simulated payment endpoint requiring card details.

API Endpoints
Restaurant Endpoints
Method	Endpoint	Description
GET	/api/restaurants/filter?location=<location>&cuisine=<cuisine>	Search and filter restaurants.
GET	/api/restaurants	Fetch a list of all restaurants.
Menu Endpoints
Method	Endpoint	Description
GET	/api/menu/<id>	Fetch the menu of a restaurant.
Order Endpoints
Method	Endpoint	Description
POST	/api/order/checkout	Checkout for an order.
Payment Endpoints
Method	Endpoint	Description
POST	/api/payment	Process payment for an order.

Testing with Postman
Import the API endpoints into Postman.
Use the following example requests:
Filter Restaurants:
sql
Copy code
GET http://127.0.0.1:5000/api/restaurants/filter?location=new%20york&cuisine=italian
Fetch Menu:
ruby
Copy code
GET http://127.0.0.1:5000/api/menu/1
Checkout Order:
json
Copy code
POST http://127.0.0.1:5000/api/order/checkout
{
    "restaurant_id": 1,
    "food_items": [{"id": 1, "quantity": 2}, {"id": 3, "quantity": 1}]
}
Payment:
json
Copy code
POST http://127.0.0.1:5000/api/payment
{
    "order_id": 1,
    "card_number": "4242424242424242",
    "expiration_date": "12/25",
    "cvv": "123"
}
