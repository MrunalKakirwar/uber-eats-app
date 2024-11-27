from flask import Blueprint, jsonify

menu_routes = Blueprint('menu_routes', __name__)

# Dummy menu data
menus = {
    1: [  # Italian Delight
        {"id": 1, "name": "Margherita Pizza", "price": 12.99},
        {"id": 2, "name": "Spaghetti Carbonara", "price": 14.99}
    ],
    2: [  # Sushi Paradise
        {"id": 3, "name": "California Roll", "price": 9.99},
        {"id": 4, "name": "Dragon Roll", "price": 11.99}
    ],
    3: [  # Taco Haven
        {"id": 5, "name": "Beef Tacos", "price": 8.99},
        {"id": 6, "name": "Chicken Quesadilla", "price": 10.99}
    ],
    4: [  # Burger World
        {"id": 7, "name": "Cheeseburger", "price": 6.99},
        {"id": 8, "name": "Veggie Burger", "price": 7.99}
    ]
}

# Get menu for a restaurant
@menu_routes.route('/<int:restaurant_id>', methods=['GET'])
def get_menu(restaurant_id):
    if restaurant_id not in menus:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify(menus[restaurant_id]), 200
