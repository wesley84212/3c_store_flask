from datetime import datetime
from urllib import response
from flask_restful import Resource, reqparse
from db import db
# from db_pyodbc import cnxn
from ..models.transaction import Transaction, ReStock, ReStockDetail
import uuid
# import json 

class TransactionAPI(Resource):
    LIST_URL = '/transaction/<trans_id>'
    CREATE_URL = '/transaction'

    def get(self, trans_id):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True, location=['form'])
        parser.add_argument('customer_id', type=str, required=True, location=['form'])
        
        transaction = db.session.query(Transaction).filter(
            Transaction.trans_id == (trans_id if(trans_id!='all') else Transaction.trans_id)
        ).all()

        if not transaction:
            return {'message':'查無此交易紀錄'}

        transaction_json = {
            'transaction': [record.to_json() for record in transaction]
        } 
        return transaction_json
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True, location=['form'])
        parser.add_argument('customer_id', type=str, required=True, location=['form'])
        parser.add_argument('trans_date', type=str, required=False, location=['form'])
        req_data = parser.parse_args()
        print(req_data)
        transaction = Transaction.create(
            trans_id = str(uuid.uuid4()),
            employee_id = req_data['employee_id'],
            customer_id = req_data['customer_id'],
            trans_date = req_data['trans_date'],
            total_price = 200000
        )
        db.session.add(transaction)
        db.session.commit()
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

class RestockAPI(Resource):
    LIST_URL = '/restock/<restock_id>'
    CREATE_URL = '/restock'

    def get(self, restock_id):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True, location=['form'])
        parser.add_argument('customer_id', type=str, required=True, location=['form'])
        
        restock = db.session.query(ReStock).filter(
            ReStock.restock_id == (restock_id if(restock_id!='all') else ReStock.restock_id)
        ).all()

        if not restock:
            return {'message':'查無此交易紀錄'}

        restock_json = {
            'restock': [record.to_json() for record in restock]
        } 
        return restock_json
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True, location=['form'])
        parser.add_argument('supplier_id', type=str, required=True, location=['form'])
        parser.add_argument('restock_date', type=str, required=True, location=['form'])
        req_data = parser.parse_args()
        print(type(req_data['restock_date']))
        restock = ReStock.create(
            restock_id = str(uuid.uuid4()),
            employee_id = req_data['employee_id'],
            supplier_id = req_data['supplier_id'],
            restock_date = req_data['restock_date'],
            total_price = 200000
        )
        db.session.add(restock)
        db.session.commit()
        return {'restock_id': restock.restock_id},

    def put(self, trans_id): 
        parser = reqparse.RequestParser()
        parser.add_argument('total_price', type=int, required=True)
        req_data = parser.parse_args()

        Restock = db.session.query(Restock).filter(
            Restock.trans_id == trans_id
        ).first()
        if not Restock:
            return {'message': f'不存在的trans_id:{trans_id}'}
        
        Restock.total_price = req_data['total_price']
        db.session.add(Restock)
        db.session.commit()
        return 

    def delete(self, trans_id):
        Restock = db.session.query(Restock).filter(
            Restock.trans_id == trans_id
        ).first()
        
        if not Restock:
            return {'message': f'不存在的trans_id:{trans_id}'}

        db.session.delete(Restock)
        db.session.commit()
        return 
