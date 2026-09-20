from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })


@app.route("/orders")
def orders():

    order_id = 101
    amount = 55000

    payment_data = {
        "order_id": order_id,
        "amount": amount
    }

    try:
        payment_response = requests.post(
            "http://payment-service:5002/payment",
            json=payment_data
        )

        payment_result = payment_response.json()

        return jsonify({
            "order_id": order_id,
            "product": "Laptop",
            "quantity": 1,
            "amount": amount,
            "payment": payment_result
        })

    except Exception as e:
        return jsonify({
            "error": "Payment Service unavailable",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)