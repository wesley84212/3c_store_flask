from flask import Blueprint
from flask_restful import Api

from .transaction import *
from .member import *

transaction_bp = Blueprint('transaction', __name__)
member_bp = Blueprint('member', __name__)
product_bp = Blueprint('product', __name__)
sku_bp = Blueprint('sku', __name__)

transaction_api = Api(transaction_bp)
member_api = Api(member_bp)

transaction_api.add_resource(
    RestockCTRL,
    RestockCTRL.LIST_URL,
    RestockCTRL.CREATE_URL
)
transaction_api.add_resource(
    RestockDataCTRL,
    RestockDataCTRL.LIST_URL,
    RestockDataCTRL.CREATE_URL
)
transaction_api.add_resource(
    TransactionCTRL,
    TransactionCTRL.LIST_URL,
    TransactionCTRL.CREATE_URL
)


member_api.add_resource(
    CustomerCTRL,
    CustomerCTRL.LIST_URL,
    CustomerCTRL.CREATE_URL
)
member_api.add_resource(
    EmployeeCTRL,
    EmployeeCTRL.LIST_URL,
    EmployeeCTRL.CREATE_URL
)




