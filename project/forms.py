from flask_wtf import FlaskForm
from flask_wtf.file import  FileField
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField, SelectField, RadioField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from project.models import Users, Suppliers, Employees, Type1, Type2
from datetime import datetime

class RegisterFormUser(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    name = StringField(label='Full Name:', validators=[Length(min=3, max=50), DataRequired()])
    username = StringField(label='Username:', validators=[Length(min=3, max=20), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6, max=12), DataRequired()])
    confirm_pass = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    level = RadioField(u'Level:', choices=[('admin', 'ADMIN'), ('viewer', 'VIEWER')], validators=[DataRequired()])
    submit = SubmitField(label='Register')

class RegisterFormSupplier(FlaskForm):
    def validate_company_id(self, company_id_to_check):
        company = Suppliers.query.filter_by(company_id=company_id_to_check.data).first()
        if company:
            raise ValidationError('Company is already registered!')
        
    company_name = StringField(label='Company Name:', validators=[Length(max=30), DataRequired()])
    company_id = StringField(label='Company Registration:', validators=[Length(min=11, max=14), DataRequired()])
    sales_person = StringField(label='Sales Person:', validators=[Length(max=20), DataRequired()])
    contact = StringField(label='Contact:', validators=[Length(min=11, max=11), DataRequired()])
    submit = SubmitField(label='Register')


class RegisterFormEmployee(FlaskForm):
    def validate_name(self, name_to_check):
        employee = Employees.query.filter_by(name=name_to_check.data).first()
        if employee:
            raise ValidationError('Employee is already registered!')
        
    name = StringField(label='Full Name:', validators=[Length(max=59), DataRequired()])
    born_date = DateField(label='Born Date:', validators=[DataRequired()])
    position = StringField(label='Position:', validators=[Length(max=30), DataRequired()])
    hire_date = DateField(label='Hire Date:', validators=[DataRequired()])
    email = StringField(label='Email:', validators=[Length(max=50), Email(), DataRequired()])
    contact = StringField(label='Contact:', validators=[Length(min=11, max=11), DataRequired()])
    pic = FileField("Employee Picture:")
    submit = SubmitField(label='Register')

class RegisterFormIncome(FlaskForm):
    date = DateField(label='Date:', validators=[DataRequired()])
    cash_value = FloatField(label='Cash:', validators=[])
    debit_value = FloatField(label='Debit Card:', validators=[])
    credit_value = FloatField(label='Credit Card:', validators=[])
    submit = SubmitField(label='Register')

class RegisterFormOutgoing(FlaskForm):
    def choice_query():
        return Suppliers.query
    
    def type_query():
        return Type1.query
         
    date = DateField(label='Date:', validators=[DataRequired()])
    cost = FloatField(label='Cost:', validators=[])
    method = SelectField(u'Method:', choices=[('deposit', 'DEPOSIT'), ('cash', 'CASH')], validators=[DataRequired()])
    receiver = QuerySelectField('Select Receiver:',query_factory=choice_query, allow_blank=True, get_label='company_name', validators=[DataRequired()])
    type1 = QuerySelectField('Type 1:', query_factory=type_query, allow_blank=True, get_label='type1', validators=[DataRequired()])
    type2 = QuerySelectField('Type 2:', get_label='type2', allow_blank=True, validators=[DataRequired()])
    description = StringField(label='Description:', validators=[Length(max=200), DataRequired()])
    status = SelectField(u'Status:', choices=[('open', 'OPEN'), ('ok', 'OK')], validators=[DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    username = StringField(label='', validators=[DataRequired()])
    password = PasswordField(label='', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class ChangePassForm(FlaskForm):
    current_pass = PasswordField(label='', validators=[Length(min=6, max=12), DataRequired()])
    new_pass = PasswordField(label='', validators=[Length(min=6, max=12), DataRequired()])
    confirm_pwd = PasswordField(label='', validators=[EqualTo('new_pass'), DataRequired()])
    submit = SubmitField(label='Change')

class SetTaxesForm(FlaskForm):
    update = DateField(label='Date', validators=[DataRequired()])
    cash_tax = FloatField(validators=[DataRequired()])
    debit_tax = FloatField(validators=[DataRequired()])
    credit_tax = FloatField(validators=[DataRequired()])
    submit = SubmitField(label='Set')

class EditFormEmployee(FlaskForm):
    name = StringField(label='Full Name:', validators=[Length(max=60), DataRequired()])
    born_date = DateField(label='Born Date:', validators=[DataRequired()])
    position = StringField(label='Position:', validators=[Length(max=30), DataRequired()])
    hire_date = DateField(label='Hire Date:', validators=[DataRequired()])
    email = StringField(label='Email:', validators=[Length(max=50), Email(), DataRequired()])
    contact = StringField(label='Contact:', validators=[Length(min=11, max=11), DataRequired()])
    is_actual = SelectField(u'Current Employee?:', choices=[('yes', 'YES'), ('no', 'NO')], validators=[DataRequired()])
    pic = FileField("Employee Picture:")
    submit = SubmitField(label='Register')

class EditFormSupplier(FlaskForm):
    company_name = StringField(label='Company Name:', validators=[Length(max=30), DataRequired()])
    company_id = StringField(label='Company Registration:', validators=[Length(min=14, max=19), DataRequired()])
    sales_person = StringField(label='Sales Person:', validators=[Length(max=20), DataRequired()])
    contact = StringField(label='Contact:', validators=[Length(min=11, max=11), DataRequired()])
    submit = SubmitField(label='Register')

class ChangeEmailForm(FlaskForm):
    new_email = StringField(label='', validators=[Email(), DataRequired()])
    confirm_email =  StringField(label='', validators=[EqualTo('new_email'), Email(), DataRequired()])
    submit = SubmitField(label='Confirm')

class FireDateForm(FlaskForm):
    fire_date = DateField('Fire Date:')
    submit = SubmitField(label='Confirm')
    
class SetType1Form(FlaskForm):
    def validate_type1(self, type1_to_check):
        type1 = Type1.query.filter_by(type1=type1_to_check.data).first()
        if type1:
            raise ValidationError(f'{type1_to_check.data} is already registered as Type 1!')
    
    type1 = StringField(label='Type 1:', validators=[Length(max=30), DataRequired()])
    submit = SubmitField(label='Set')

class SetType2Form(FlaskForm):
    def validate_type2(self, type2_to_check):
        type2 = Type2.query.filter_by(type2=type2_to_check.data).first()
        if type2:
            raise ValidationError(f'{type2_to_check.data} is already registered as Type 2!')
    
    def type_query():
        return Type1.query
    
    type2 = StringField(label='Type 2:', validators=[Length(max=30),DataRequired()])
    type1 = QuerySelectField('Type 1:', query_factory=type_query, allow_blank=True, get_label='type1', validators=[DataRequired()])
    submit = SubmitField(label='Set')


