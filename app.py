from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["fintech_wallet"]
users_collection = db["users"]
transactions_collection = db["transactions"]

def generate_wallet_id():
    return str(uuid.uuid4())

@app.route('/api/register', methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    phone_number = ['phone_number']

    if not name or not email or not phone_number:
        return jsonify({"error": "All fields are required"}), 400

    wallet_id = generate_wallet_id()
    user = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "wallet_id": wallet_id,
        "balance": 0
    }
    users_collection.insert_one(user)

    return jsonify({"wallet_id": wallet_id, "balance": 0}), 201

# Endpoint: Add Money to Wallet
@app.route('/api/wallet/add-money', methods=['POST'])
def add_money():
    data = request.json
    wallet_id = data.get('wallet_id')
    amount = data.get('amount')

    if not wallet_id or not amount or amount <= 0:
        return jsonify({"error": "Invalid wallet ID or amount"}), 400

    user = users_collection.find_one({"wallet_id": wallet_id})
    if not user:
        return jsonify({"error": "Wallet not found"}), 404

    new_balance = user["balance"] + amount
    users_collection.update_one({"wallet_id": wallet_id}, {"$set": {"balance": new_balance}})

    transaction = {
        "wallet_id": wallet_id,
        "transaction_type": "Add Money",
        "amount": amount,
        "timestamp": datetime.now()
    }
    transactions_collection.insert_one(transaction)

    return jsonify({"wallet_id": wallet_id, "balance": new_balance}), 200

@app.route('/api/wallet/<wallet_id>/balance', methods=['GET'])
def check_balance(wallet_id):
    user = users_collection.find_one({"wallet_id": wallet_id})
    if not user:
        return jsonify({"error": "Wallet not found"}), 404

    return jsonify({"wallet_id": wallet_id, "balance": user["balance"]}), 200

@app.route('/api/wallet/<wallet_id>/transactions', methods=['GET'])
def transaction_history(wallet_id):
    transactions = list(transactions_collection.find({"wallet_id": wallet_id}, {"_id": 0}))
    return jsonify(transactions), 200

@app.route('/api/admin/wallets', methods=['GET'])
def view_all_wallets():
    wallets = list(users_collection.find({}, {"_id": 0, "wallet_id": 1, "balance": 1, "name": 1}))
    return jsonify(wallets), 200

# Endpoint: Admin - View All Transactions
@app.route('/api/admin/transactions', methods=['GET'])
def view_all_transactions():
    transactions = list(transactions_collection.find({}, {"_id": 0}))
    return jsonify(transactions), 200

if __name__ == '__main__':
    app.run(debug=True)
