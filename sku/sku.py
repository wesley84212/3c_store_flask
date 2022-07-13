from flask_restful import Resource, reqparse
from db_pyodbc import cnxn

class SKUAPI(Resource):
    LIST_URL = '/sku/<date>'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
