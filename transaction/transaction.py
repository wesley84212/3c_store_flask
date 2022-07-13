from urllib import response
from flask_restful import Resource, reqparse
from db import db
# from db_pyodbc import cnxn
from .models import Transaction
# import json 

class TransactionAPI(Resource):
    LIST_URL = '/transaction/<date>'

    def get(self, date):
        parser = reqparse.RequestParser()

        # transaction = Transaction.session.query().filter().all()
        transaction = db.session.query(Transaction).all()
        json = {
            'transaction': [record.to_json() for record in transaction]
        } 
        # cursor = cnxn.cursor()
        # sql = '''SELECT `trans_record`.`trans_id`,
        #             `trans_record`.`employee_id`,
        #             `trans_record`.`customer_id`,
        #             DATE_FORMAT(`trans_record`.`trans_date`, '%Y-%m-%d'),
        #             `trans_record`.`total_price`
        #         FROM `pos`.`trans_record`;'''

        # # print(sql)
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # res = [list(row) for row in data]       
        # # print(res)
        return json
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
