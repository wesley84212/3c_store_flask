from flask import Blueprint
from flask_restful import Api

from .product import *
from .transaction import *

transaction_bp = Blueprint('transaction', __name__)
transaction_api = Api(transaction_bp)

product_bp = Blueprint('product', __name__)
product_api = Api(product_bp)

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

product_api.add_resource(
    ProductCTRL,
    ProductCTRL.LIST_URL
)

product_api.add_resource(
    AddProductCTRL,
    AddProductCTRL.LIST_URL
)

product_api.add_resource(
    ProductsListCTRL,
    ProductsListCTRL.LIST_URL
)

