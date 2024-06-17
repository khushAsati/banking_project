from . import mongo
from bson.objectid import ObjectId

class Transaction:
    @staticmethod
    def insert(transaction_data):
        return mongo.db.transactions.insert_one(transaction_data)
    
    @staticmethod
    def find_by_customer_id(customer_id):
        return mongo.db.transactions.find({"customer_id": customer_id})
    
    @staticmethod
    def find_all():
        return mongo.db.transactions.find()
