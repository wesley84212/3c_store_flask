from flask_restful import Resource, reqparse
from db_pyodbc import cnxn

class CustomerAPI(Resource):
    LIST_URL = '/customer/<date>'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
