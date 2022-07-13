from flask import Blueprint
from flask_restful import Api

from .sku import *

sku_api = Blueprint('sku', __name__)
api = Api(sku_api)

api.add_resource(
    SKUAPI,
    SKUAPI.LIST_URL
)