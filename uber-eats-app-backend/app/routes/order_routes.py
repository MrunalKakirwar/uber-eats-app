from flask import Blueprint, request, jsonify

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/order/checkout', methods=['POST'])
def checkout_order():
    try:
        data = request.json
        food_id = data.get("food_id")
        food_name = data.get("food_name")
        price = data.get("price")
        
        if not food_id or not food_name or not price:
            return jsonify({"error": "Missing required fields: food_id, food_name, or price"}), 400

        # Calculate total (price + dummy tax)
        tax = 1.0
        total_amount = round(price + tax, 2)

        response = {
            "food_item": food_name,
            "price": price,
            "tax": tax,
            "total_amount": total_amount
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": "Failed to process order", "details": str(e)}), 500
