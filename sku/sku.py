from urllib import response
from flask_restful import Resource, reqparse
from db import db
# from db_pyodbc import cnxn
from .models import Sku
# import json 

class SkuAPI(Resource):
    LIST_URL = '/sku/<date>'

    def get(self, date):
        parser = reqparse.RequestParser()

        sku = db.session.query(Sku).all()
        json = {
            'sku': [record.to_json() for record in sku]
        } 
      
        return json
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
