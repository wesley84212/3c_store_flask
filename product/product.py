# -*- coding: utf-8 -*-
from itertools import product
from urllib import response
from flask_restful import Resource, reqparse
from db_pyodbc import cnxn
from db import db
from .models import Product

class ProductAPI(Resource):
    LIST_URL = '/product/<date>'

    def get(self, date):
        parser = reqparse.RequestParser()

        # transaction = Transaction.session.query().filter().all()
        products = db.session.query(Product).all()
        json = {
            'Products': [record.to_json() for record in products]
        } 
        # for record in products :
        #     print(type(record.product_name))
        #     print(record.product_name)
        query = Product.query.filter_by(brand_id='B0002').order_by(Product.product_id.desc()).all()
        for record in query :
            print(record.product_id,record.product_name)
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

    def post(self,date):
         # 新增資料
        product_add = Product('SP000009','iPhone 14','A2633','B0002',1,4,'2022/01/01 20:37:21','蘋果14')
        db.session.add(product_add)
        db.session.commit()
        return {'message':f'insert {product_add}success'},200

    def put(self):
        # Updata data
        query = Product.query.filter_by(product_name='iPhone 14').first()

        # 將 price 修改成 10 塊
        query.name = 10
        db.session.commit()
        return 

    def delete(self,date):
        # 刪除資料
        query = Product.query.filter_by(product_name='iPhone 14').first()
        db.session.delete(query)
        db.session.commit()
        return 
