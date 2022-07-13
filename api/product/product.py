from flask_restful import Resource, reqparse
from db import cnxn

class ProductAPI(Resource):
    LIST_URL = '/product/<date>'

    def get(self, date):
        return date
    
    def post(self):
        return 

    def put(self):
        return 

    def delete(self):
        return 
