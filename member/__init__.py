from flask import Blueprint
from flask_restful import Api

from ..application.controllers.member import *

member_api = Blueprint('customer', __name__)
api = Api(member_api)

api.add_resource(
    CustomerAPI,
    CustomerAPI.LIST_URL
)

