from flask import Blueprint, request, jsonify
from app.utils import search_restaurants, filter_restaurants

restaurant_routes = Blueprint('restaurant_routes', __name__)

# Dummy restaurant data
restaurants = [
    {"id": 1, "name": "Italian Delight", "location": "New York", "cuisine": "Italian"},
    {"id": 2, "name": "Sushi Paradise", "location": "San Francisco", "cuisine": "Japanese"},
    {"id": 3, "name": "Taco Haven", "location": "Los Angeles", "cuisine": "Mexican"},
    {"id": 4, "name": "Burger World", "location": "New York", "cuisine": "American"}
]

# Search restaurants by name or cuisine
@restaurant_routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    result = search_restaurants(restaurants, query)
    return jsonify(result), 200

# Filter restaurants by location or cuisine
@restaurant_routes.route('/filter', methods=['GET'])
def filter_restaurants_endpoint():
    location = request.args.get('location', '').lower()
    cuisine = request.args.get('cuisine', '').lower()

    result = filter_restaurants(restaurants, location, cuisine)
    return jsonify(result), 200
