from datetime import datetime
from urllib import response
from flask_restful import Resource, reqparse
from db import db
# from db_pyodbc import cnxn
from .models import Transaction
import uuid
import R
# import json 

class TransactionAPI(Resource):
    LIST_URL = '/transaction/<trans_id>'
    CREATE_URL = '/transaction'

    def get(self, trans_id):
        parser = reqparse.RequestParser()

        transaction = db.session.query(Transaction).all()

        if not transaction:
            return {'message':'查無此交易紀錄'}

        json = {
            'transaction': [record.to_json() for record in transaction]
        } 
        return json
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True)
        parser.add_argument('customer_id', type=str, required=True)
        parser.add_argument('trans_date', type=datetime, required=True)
        req_data = parser.parse_args()
        print(req_data)
        transaction = Transaction.create(
            trans_id = uuid.uuid4(),
            employee_id = req_data['employee_id'],
            customer_id = req_data['customer_id'],
            trans_date = req_data['trans_date'],
            total_price = 200000
        )
        return {'trans_id': transaction.trans_id},

    def put(self, trans_id): 
        parser = reqparse.RequestParser()
        parser.add_argument('total_price', type=int, required=True)
        req_data = parser.parse_args()

        transaction = db.session.query(Transaction).filter(
            Transaction.trans_id == trans_id
        ).first()
        if not transaction:
            return {'message': f'不存在的trans_id:{trans_id}'}
        
        transaction.total_price = req_data['total_price']
        db.session.add(transaction)
        db.session.commit()
        return 

    def delete(self, trans_id):
        transaction = db.session.query(Transaction).filter(
            Transaction.trans_id == trans_id
        ).first()
        
        if not transaction:
            return {'message': f'不存在的trans_id:{trans_id}'}

        db.session.delete(transaction)
        db.session.commit()
        return 
