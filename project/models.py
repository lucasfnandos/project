from project import db, app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    name = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=50), nullable=False)
    hash = db.Column(db.String(length=350), nullable=False)
    level = db.Column(db.String(length=6), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.hash = generate_password_hash(plain_text_password)

    def check_password(self, password_login):
        return check_password_hash(self.hash, password_login)

class Incomings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    cash_value = db.Column(db.Float(), nullable=False)
    tax_cash = db.Column(db.Float(), nullable=False)
    debit_value = db.Column(db.Float, nullable=False)
    tax_debit = db.Column(db.Float(), nullable=False)
    credit_value = db.Column(db.Float(), nullable=False)
    tax_credit = db.Column(db.Float(), nullable=False)
    total_tax = db.Column(db.Float(), nullable=False)
    net_receipt = db.Column(db.Float(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Outgoings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
    method = db.Column(db.String(length=10))
    receiver = db.Column(db.String(), nullable=False)
    type1 = db.Column(db.String(length=30), nullable=False)
    type2 = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=200), nullable=False)
    status = db.Column(db.String(length=10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Suppliers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    company_name = db.Column(db.String(length=60), nullable=False)
    company_id = db.Column(db.String(length=15), nullable=False)
    sales_person = db.Column(db.String(length=20), nullable=False)
    contact = db.Column(db.String(length=11), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '{}'.format(self.company_name)

class Employees(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=60), nullable=False)
    born_date = db.Column(db.Date(), nullable=False)
    position = db.Column(db.String(length=30), nullable=False)
    hire_date = db.Column(db.Date(), nullable=False)
    email = db.Column(db.String(length=50), nullable=True)
    contact = db.Column(db.String(length=11), nullable=False)
    is_actual = db.Column(db.String(length=3), nullable=False)
    end_date = db.Column(db.Date(), nullable=True)
    pic = db.Column(db.String(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Taxes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    update = db.Column(db.Date(), nullable=False)
    cash_tax = db.Column(db.Float(), nullable=False)
    debit_tax = db.Column(db.Float(), nullable=False)
    credit_tax = db.Column(db.Float(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Type1(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type1 = db.Column(db.String(length=30), nullable=False)
    

class Type2(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type2 = db.Column(db.String(length=30), nullable=False)
    type1_id = db.Column(db.Integer, db.ForeignKey('type1.id'), nullable=False)

class Historic(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

with app.app_context():
    db.create_all()