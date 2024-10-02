from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models.user_model import User



class Order:
    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.order_type = data['order_type']
        self.wallet = data['wallet']
        self.payment_method = data['payment_method']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = User.get_by_id({'id' : self.user_id})




    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders"
        results = connectToMySQL(DB).query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    




    @classmethod
    def get_orders_by_id(cls, data):
        query = "SELECT * FROM orders WHERE id = %s"
        result = connectToMySQL(DB).query_db(query,data)
        if len(result) <1:
            return False
        return cls(result[0])
    



    @classmethod
    def create_order(cls, data):
        query = "INSERT INTO orders (full_name, email, order_type, wallet, payment_method, user_id) VALUES (%(full_name)s, %(email)s, %(order_type)s, %(wallet)s, %(payment_method)s, %(user_id)s)"
        results = connectToMySQL(DB).query_db(query, data)
        return results
    


    @classmethod
    def update_order(cls, data):
        query = "UPDATE orders SET full_name=%(full_name)s, email=%(email)s, order_type=%(order_type)s, wallet=%(wallet)s, payment_method=%(payment_method)s, updated_at=NOW() WHERE id=%(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        return results
    



    @classmethod
    def delete_order(cls, data):
        query = "DELETE FROM orders WHERE id = %s"
        results = connectToMySQL(DB).query_db(query, data)
        return results
    



    @staticmethod
    def validate_order(data):
        errors = {}
        if not data['full_name']:
            errors['full_name'] = "Full name is required"
        if not data['email']:
            errors['email'] = "Email is required"
        if not data['order_type']:
            errors['order_type'] = "Order type is required"
        if not data['wallet']:
            errors['wallet'] = "Wallet is required"
        if not data['payment_method']:
            errors['payment_method'] = "Payment method is required"
        if not data['user_id']:
            errors['user_id'] = "User ID is required"
        return errors
    


