from flask_restful import Resource, reqparse
from db_pyodbc import cnxn

class CustomerCTRL(Resource):
    LIST_URL = '/customer/<date>'
    CREATE_URL = '/customer'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 


class EmployeeCTRL(Resource):
    LIST_URL = '/employee/<date>'
    CREATE_URL = '/employee'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 