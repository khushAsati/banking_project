from . import mongo

class Customer:
    @staticmethod
    def find_by_username(username):
        return mongo.db.customers.find_one({"username": username})
    
    @staticmethod
    def insert(customer_data):
        return mongo.db.customers.insert_one(customer_data)
    
    @staticmethod
    def find_by_id(customer_id):
        return mongo.db.customers.find_one({"_id": customer_id})
    
    @staticmethod
    def find_all():
        return mongo.db.customers.find()
