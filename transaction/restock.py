from flask_restful import Resource, reqparse
from db_pyodbc import cnxn

class RestockAPI(Resource):
    LIST_URL = '/restock/<date>'

    def get(self, date):
        parser = reqparse.RequestParser()
        cursor = cnxn.cursor()
        sql = ""
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
