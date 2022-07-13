from flask import Blueprint
from flask_restful import Api

from .restock import *
from .transaction import *

transaction_api = Blueprint('transaction', __name__)
api = Api(transaction_api)

api.add_resource(
    RestockAPI,
    RestockAPI.LIST_URL
)

api.add_resource(
    TransactionAPI,
    TransactionAPI.LIST_URL
)

