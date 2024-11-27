from flask import Blueprint, request, jsonify

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/payment', methods=['POST'])
def process_payment():
    try:
        data = request.json
        card_number = data.get("card_number")
        expiry_date = data.get("expiry_date")
        cvv = data.get("cvv")
        amount = data.get("amount")

        if not card_number or not expiry_date or not cvv or not amount:
            return jsonify({"error": "Missing required payment fields"}), 400

        # Simulate payment success
        if len(str(card_number)) != 16 or len(str(cvv)) != 3:
            return jsonify({"error": "Invalid card details"}), 400

        response = {"message": "Payment successful", "amount_paid": amount}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": "Payment failed", "details": str(e)}), 500
