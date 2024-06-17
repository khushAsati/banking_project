from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.customer import Customer
from models.transaction import Transaction

banker_controller = Blueprint('banker_controller', __name__)

@banker_controller.route('/api/banker/customers', methods=['GET'])
@jwt_required()
def customers():
    print("in this")
    customers = Customer.find_all()
    customers_list = list(customers) 
    for customer in customers_list:
        print("-->",customer)
        customer['_id']=str(customer['_id'])
        customer['username']=str(customer['username'])
        customer['password']=str(customer['password'])


    return jsonify(customers_list), 200

@banker_controller.route('/api/banker/transactions', methods=['GET'])
@jwt_required()
def transactions():
    transactions = Transaction.find_all()
    transactions_list = list(transactions) 
    for transaction in transactions_list:
        print("-->",transaction)
        transaction['_id'] = str(transaction['_id'])
        transaction['customer_id'] = str(transaction['customer_id'])
        transaction['amount']=str(transaction['amount'])
        transaction['type']=str(transaction['type'])
    return jsonify(transactions_list), 200
