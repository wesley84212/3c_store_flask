from flask import Blueprint
from flask_restful import Api

from .customer import *

product_api = Blueprint('product', __name__)
api = Api(product_api)

api.add_resource(
    CustomerAPI,
    CustomerAPI.LIST_URL
)

