from db import db
from sqlalchemy import select

class Product(db.Model):
    __tablename__ = 'product'
    # __table_args__ = {'mysql_charset': 'utf8mb4_unicode_ci'}

    product_id = db.Column(db.String(8), primary_key=True)
    product_name = db.Column(db.String(100), nullable=True)
    product_model = db.Column(db.String(30), nullable=True)
    brand_id = db.Column(db.String(5), db.ForeignKey('brand.brand_id'), nullable=True)
    category_id = db.Column(db.Integer, nullable=True)
    supplier_id = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime(), nullable=True)
    details = db.Column(db.String(500), nullable=True)


    def __init__(self, product_id ,product_name,product_model,brand_id,category_id,supplier_id,create_time,details):
        self.product_id=product_id
        self.product_name=product_name
        self.product_model =product_model
        self.brand_id =brand_id
        self.category_id=category_id
        self.supplier_id=supplier_id
        self.create_time = create_time
        self.details=details

    def to_json(self):
        json = {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_model': self.product_model,
            'brand_id': self.brand_id,
            'category_id': self.category_id,
            'supplier_id': self.supplier_id,
            'create_time': self.create_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'details': self.details
        }
        return json