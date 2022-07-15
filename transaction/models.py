from db import db


class Transaction(db.Model):
    __tablename__ = 'trans_record'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    trans_id = db.Column(db.String(36), primary_key=True)
    employee_id = db.Column(db.String(7), nullable=False)
    customer_id = db.Column(db.String(7), nullable=False)
    trans_date = db.Column(db.DateTime(), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    @classmethod 
    def create(trans_id, employee_id, customer_id, trans_date, total_price):
        transaction = Transaction()
        transaction.trans_id = trans_id
        transaction.employee_id = employee_id
        transaction.customer_id = customer_id
        transaction.trans_date = trans_date
        transaction.total_price = total_price
        return transaction




    def to_json(self):
        json = {
            'trans_id': self.trans_id,
            'employee_id': self.employee_id,
            'customer_id': self.customer_id,
            'trans_date': self.trans_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'total_price': self.total_price
        }
        return json
