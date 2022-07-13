from flask import Blueprint
from flask_restful import Api

from .product import *
from .category import *
from .brand import *

product_api = Blueprint('product', __name__)
api = Api(product_api)

api.add_resource(
    ProductAPI,
    ProductAPI.LIST_URL
)

api.add_resource(
    CategoryAPI,
    CategoryAPI.LIST_URL
)
