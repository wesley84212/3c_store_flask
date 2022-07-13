from atexit import register
from flask import Flask

from api.product import *
from api.sku import *
from api.transaction import *

#建立Flask APP
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    register_blueprints(app)
    return app

#註冊API
def register_blueprints(app):
    app.register_blueprint(product_api, url_prefix="/3c_store/api/v1"+"/product")
    app.register_blueprint(sku_api, url_prefix="/3c_store/api/v1"+"/sku")
    app.register_blueprint(transaction_api, url_prefix="/3c_store/api/v1"+"/transaction")