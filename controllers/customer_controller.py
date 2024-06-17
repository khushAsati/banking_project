from json import dumps
from bson import ObjectId
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models.customer import Customer
from models.transaction import Transaction
import bcrypt

customer_controller = Blueprint('customer_controller', __name__)

@customer_controller.route('/api/customer/register', methods=['POST'])
@jwt_required()
def register():
    data = request.get_json()
    username = data['username']
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    customer_data = {
        'username': username,
        'password': password
    }
    Customer.insert(customer_data)
    return jsonify({'message': 'Customer registered successfully'}), 201

@customer_controller.route('/api/customer/login', methods=['POST'])
@jwt_required()
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    customer = Customer.find_by_username(username)
    if customer and bcrypt.checkpw(password.encode('utf-8'), customer['password']):
        access_token = create_access_token(identity=str(customer['_id']))
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@customer_controller.route('/api/customer/transaction', methods=['POST'])
def transaction():
    data = request.get_json()
    customer_id = data['customer_id']
    amount = data['amount']
    transaction_type = data['type']
    transaction_data = {
        'customer_id': customer_id,
        'amount': amount,
        'type': transaction_type
    }
    Transaction.insert(transaction_data)
    return jsonify({'message': 'Transaction completed successfully'}), 201


@customer_controller.route('/api/customer/transactions', methods=['GET'])
@jwt_required()
def transactions():
    data = request.get_json()
    customer_id = data['customer_id']
    try:
        customer_id_obj = ObjectId(customer_id)  # Convert to ObjectId
    except:
        return jsonify({'message': 'Invalid customer ID format'}), 400
    print(customer_id)
    transactions = Transaction.find_by_customer_id(customer_id)
    transactions_list = list(transactions) 
    for transaction in transactions_list:
        print("-->",transaction)
        transaction['_id'] = str(transaction['_id'])
        transaction['customer_id'] = str(transaction['customer_id'])
    
    print(transactions_list) 
    return jsonify(transactions_list), 200
