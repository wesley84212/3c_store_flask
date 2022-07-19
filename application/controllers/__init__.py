from flask import Blueprint
from flask_restful import Api

from .transaction import *
from .member import *
from .product import *

transaction_bp = Blueprint('transaction', __name__)
member_bp = Blueprint('member', __name__)
product_bp = Blueprint('product', __name__)
sku_bp = Blueprint('sku', __name__)

product_api = Api(product_bp)
transaction_api = Api(transaction_bp)
member_api = Api(member_bp)

transaction_api.add_resource(
    RestockAPI,
    RestockAPI.LIST_URL,
    RestockAPI.CREATE_URL
)
transaction_api.add_resource(
    TransactionAPI,
    TransactionAPI.LIST_URL,
    TransactionAPI.CREATE_URL
)

member_api.add_resource(
    CustomerAPI,
    CustomerAPI.LIST_URL,
    CustomerAPI.CREATE_URL
)
member_api.add_resource(
    EmployeeAPI,
    EmployeeAPI.LIST_URL,
    EmployeeAPI.CREATE_URL
)

product_api.add_resource(
    ProductAPI,
    ProductAPI.LIST_URL
)

product_api.add_resource(
    AddProduct,
    AddProduct.LIST_URL
)

product_api.add_resource(
    ProductsList,
    ProductsList.LIST_URL
)

