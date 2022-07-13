from flask_restful import Resource, reqparse
from db import cnxn

class RestockAPI(Resource):
    LIST_URL = '/sku/<date>'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
