from email import message
import re
from flask_restful import Resource
from flask_restful import reqparse
parser = reqparse

employees = [{'name':'DC',},{'name':'dc',}]
class Employee (Resource):
    def get(self, name):
        find = [item for item in employees if item['name']==name]
        if(len(find) == 0):
            return{
                'message':'employee not exist!'
            },403
        employee = find[0]
        if not employee:
            return{
                'message':'employee not exist!'
            },403
        return {'message':'',
                'employee':name},200
    
    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        global employees
        employees = [item for item in employees if item['name'] != name]
        return {
            'message': f'{employees}Delete done!'
        }
class Employees(Resource):
    def get(self):
        return{'message':'','employees':employees}