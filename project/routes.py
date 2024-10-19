from project import app
from flask import render_template, redirect, url_for, flash, request
from project.models import Incomings, Outgoings, Users, Suppliers, Employees, Taxes, Type1, Type2, Historic
from project.forms import RegisterFormUser, RegisterFormEmployee, RegisterFormSupplier, RegisterFormIncome, RegisterFormOutgoing, LoginForm, ChangePassForm, SetTaxesForm, EditFormEmployee, EditFormSupplier, ChangeEmailForm, FireDateForm, SetType1Form, SetType2Form
from project import db
from flask_login import login_user, logout_user, login_required, fresh_login_required, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from project.helper import custom_calendar, current_date, get_date, getmonth_name, get_age, get_week_before, string_format
from sqlalchemy import select, func
import uuid as uuid
import os
import json

def user_level(current_user):
    query_user = db.session.execute(db.select(Users.level).where(Users.id == current_user.id)).scalars().first()
    return query_user

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('home_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    user_data = db.session.execute(db.select(Users)).all()
    if not user_data:
        pswd = generate_password_hash('foofoo')
        admin = Users(username='admin', name='Administrator', email='admin@email.com', hash=pswd, level='admin')
        db.session.add(admin)
        db.session.commit()
        user_login = db.session.execute(db.select(Users)).scalars().first()
        login_user(user_login)
        flash('Standard Password: foofoo. You must change the password for security!', category='danger')
        return redirect(url_for('edit_pass', id=1))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_login = db.session.execute(db.select(Users).where(Users.username == form.username.data)).scalars().first()
            if user_login and user_login.check_password(password_login=form.password.data):
                login_user(user_login)
                flash(f"Success! You're logged in.", category="success")
                return redirect(url_for('home_page'))
            else:
                flash('Incorrect username and/or password!', category='danger')
    return render_template('login.html', form=form)

@app.route('/home')
def home_page():
    today = custom_calendar()
    get_current_date = current_date()
    
    #Current year monthly incomings search
    set_year_search = get_current_date.year
    set_month_search = get_current_date.month
    i = 1
    monthly_inc_list = []
    monthly_out_list = []
    months_list = []
    while(i <= set_month_search):
        date_from = get_date(set_year_search, i, 1)
        date_to = get_date(set_year_search, i, 31)
        
        monthly_inc = db.session.execute(db.select(func.sum(Incomings.net_receipt)).where(Incomings.date >= date_from).where(Incomings.date <= date_to)).scalars().first()
        if not monthly_inc:
            monthly_inc = 0
        monthly_inc_list.insert((i-1),monthly_inc)
        
        monthly_out = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.date >= date_from).where(Outgoings.date <= date_to)).scalars().first()
        if not monthly_out:
            monthly_out = 0
        monthly_out_list.insert((i-1),monthly_out)

        months = getmonth_name(i)
        months_list.insert((i-1), months)
        i += 1
    
    date_from = get_date(set_year_search, set_month_search, 1)
    date_to = get_date(set_year_search, set_month_search, 31)
    
    current_month_income = db.session.execute(db.select(func.sum(Incomings.net_receipt)).where(Incomings.date >= date_from).where(Incomings.date <= date_to)).scalars().first()
    if not current_month_income:
        current_month_income = 0

    current_month_outgoing = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.date >= date_from).where(Outgoings.date <= date_to)).scalars().first()
    if not current_month_outgoing:
        current_month_outgoing = 0
    
    date = get_date(set_year_search, set_month_search, get_current_date.day)
        
    current_day_income = db.session.execute(db.select(func.sum(Incomings.net_receipt)).where(Incomings.date == date)).scalars().first()
    if not current_day_income:
        current_day_income = 0
    
    current_day_outgoing = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.date == date)).scalars().first()
    if not current_day_outgoing:
        current_day_outgoing = 0

    current_year_income = sum(monthly_inc_list)
    current_year_outgoing = sum(monthly_out_list)

    week_before = get_week_before()
    date_to = get_date(set_year_search, set_month_search, get_current_date.day)

    current_week_income = db.session.execute(db.select(func.sum(Incomings.net_receipt)).where(Incomings.date >= week_before).where(Incomings.date <= date_to)).scalars().first()
    if not current_week_income:
        current_week_income = 0

    current_week_outgoing = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.date >= week_before).where(Outgoings.date <= date_to)).scalars().first()
    if not current_week_outgoing:
        current_week_outgoing = 0

    data = {}
    data['current_month_income'] = current_month_income
    data['current_month_outgoing'] = current_month_outgoing
    data['current_day_income'] = current_day_income
    data['current_day_outgoing'] = current_day_outgoing
    data['current_year_income'] = current_year_income
    data['current_year_outgoing'] = current_year_outgoing
    data['current_week_income'] = current_week_income
    data['current_week_outgoing'] = current_week_outgoing
    data['total_day'] = current_day_income - current_day_outgoing
    data['total_week'] = current_week_income - current_week_outgoing
    data['total_month'] = current_month_income - current_month_outgoing
    data['total_year'] = current_year_income - current_year_outgoing

    #Last year monthly incomings search (to complete YTD search)
    year_before = set_year_search - 1
    months_qty = 12 - set_month_search
    monthly_yb_inc_list = []
    monthly_yb_out_list = []
    i = 0
    months_yb_list = []
    while(i <= months_qty):
        date_from = get_date(year_before, (set_month_search + i), 1)
        date_to = get_date(year_before, (set_month_search + i), 31)
        
        monthly_inc_yb = db.session.execute(db.select(func.sum(Incomings.net_receipt)).where(Incomings.date >= date_from).where(Incomings.date <= date_to)).scalars().first()
        if not monthly_inc_yb:
            monthly_inc_yb = 0
        monthly_yb_inc_list.insert((i), monthly_inc_yb)

        monthly_out_yb = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.date >= date_from).where(Outgoings.date <= date_to)).scalars().first()
        if not monthly_out_yb:
            monthly_out_yb = 0
        monthly_yb_out_list.insert((i), monthly_out_yb)
        
        months = getmonth_name(set_month_search + i)
        months_yb_list.insert(i, months)
        i += 1

    for x in monthly_inc_list:
        monthly_yb_inc_list.append(x)
    total_monthly_inc = monthly_yb_inc_list

    for y in months_list:
        months_yb_list.append(y)
    months_ytd = months_yb_list

    for z in monthly_out_list:
        monthly_yb_out_list.append(z)
    total_monthly_out = monthly_yb_out_list

    liquid = []
    for A, B in zip(total_monthly_inc, total_monthly_out):
        liquid.append(A - B)

    total_cash = db.session.execute(db.select(func.sum(Incomings.cash_value))).scalars().first()
    if not total_cash:
        total_cash = 0
    get_tax_cash = db.session.execute(db.select(func.sum(Incomings.tax_cash))).scalars().first()
    if not get_tax_cash:
        get_tax_cash = 0
    total_cash = total_cash - get_tax_cash

    total_debit = db.session.execute(db.select(func.sum(Incomings.debit_value))).scalars().first()
    if not total_debit:
        total_debit = 0
    get_tax_debit = db.session.execute(db.select(func.sum(Incomings.tax_debit))).scalars().first()
    if not get_tax_debit:
        get_tax_debit = 0
    total_debit = total_debit - get_tax_debit

    total_credit = db.session.execute(db.select(func.sum(Incomings.credit_value))).scalars().first()
    if not total_credit:
        total_credit = 0
    get_tax_credit = db.session.execute(db.select(func.sum(Incomings.tax_credit))).scalars().first()
    if not get_tax_credit:
        get_tax_credit = 0
    total_credit = total_credit - get_tax_credit

    incomings_type = [total_cash, total_debit, total_credit]
    incomings_type_taxes = [get_tax_cash, get_tax_debit, get_tax_credit]
    total_tax_sum = sum(incomings_type_taxes)
    bank_acc_inc = total_debit + total_credit

    out_dep_query = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.method == 'deposit')).scalars().first()

    out_cash_query = db.session.execute(db.select(func.sum(Outgoings.cost)).where(Outgoings.method == 'cash')).scalars().first()
    
    if not out_dep_query:
        out_dep_query = 0
        
    if not out_cash_query:
        out_cash_query = 0
        
    finance_data = {}
    finance_data['cash_incomings'] = total_cash
    finance_data['bank_incomings'] = bank_acc_inc
    finance_data['cash_outgoings'] = out_cash_query
    finance_data['bank_outgoings'] = out_dep_query
    finance_data['total_cash'] = (total_cash - out_cash_query)
    finance_data['total_bank'] = (bank_acc_inc - out_dep_query)
    
    receivers_list = db.session.execute(db.select((Outgoings.receiver), func.sum(Outgoings.cost)).group_by(Outgoings.receiver).order_by(func.sum(Outgoings.cost).desc()).limit(5)).all()
    
    cost_list = []
    for _ , cost in receivers_list:
        cost_list.append(cost)
    
    receiver_list = []
    for receiver, _ in receivers_list:
        receiver_list.append(receiver)

    expen_type_list = db.session.execute(db.select((Outgoings.type1), func.sum(Outgoings.cost)).group_by(Outgoings.type1).order_by(func.sum(Outgoings.cost).desc()).limit(5)).all()
    
    expen_type_cost = []
    for _ , cost in expen_type_list:
        expen_type_cost.append(cost)
    
    type_list = []
    for type1, _ in expen_type_list:
        type_list.append(type1)

    total_income = db.session.execute(db.select(func.sum(Incomings.net_receipt))).scalars().first()
    if not total_income:
        total_income = 0
    total_outgoing = db.session.execute(db.select(func.sum(Outgoings.cost))).scalars().first()
    if not total_outgoing:
        total_outgoing = 0

    incomings_outgoings = [0,0]
    incomings_outgoings[0] = total_income
    incomings_outgoings[1] = total_outgoing
    
    net_income = (total_income) - (total_outgoing)
    try:
        net_income_perc = round(((net_income / total_income)*100), 2)
    except:
        net_income_perc = 0.00

    expen_type_percent = []
    calc = 0
    for i in expen_type_cost:
        calc = (i / total_income)*100
        expen_type_percent.append(round(calc,2))

    return render_template('home.html', today=today, get_current_date=get_current_date, total_monthly_inc=json.dumps(total_monthly_inc), total_monthly_out=json.dumps(total_monthly_out), months_ytd=json.dumps(months_ytd), incomings_type=json.dumps(incomings_type), receivers=json.dumps(receiver_list), payments_by_receiver=json.dumps(cost_list), expen_type_cost=json.dumps(expen_type_cost), type_list=json.dumps(type_list), liquid=json.dumps(liquid), net_income=(net_income), net_income_perc=(net_income_perc), incomings_outgoings=json.dumps(incomings_outgoings), type_items=type_list, expen_type_percent=expen_type_percent, incomings_type_taxes=incomings_type_taxes, total_tax_sum=total_tax_sum, data=data, finance_data=finance_data)
    

@app.route('/inputincome', methods=['GET', 'POST'])
@fresh_login_required
def input_income():
    if user_level(current_user) == 'admin':
        form = RegisterFormIncome()
        if form.validate_on_submit():
            results = Taxes.query.order_by(Taxes.update.desc(), Taxes.id.desc()).first_or_404()
            cash_tax = round(((results.cash_tax  / 100.00) * (form.cash_value.data)), 2)
            debit_tax = round(((results.debit_tax  / 100.00) * (form.debit_value.data)), 2)
            credit_tax = round(((results.credit_tax  / 100.00) * (form.credit_value.data)), 2)
            total_tax = round((float(cash_tax + debit_tax + credit_tax)), 2)
            net_receipt = round((((form.cash_value.data)+(form.debit_value.data)+(form.credit_value.data)) - total_tax), 2)
            income_to_input = Incomings(date=form.date.data,
                                    cash_value=form.cash_value.data,
                                    tax_cash=cash_tax,
                                    debit_value=form.debit_value.data,
                                    tax_debit=debit_tax,
                                    credit_value=form.credit_value.data,
                                    tax_credit=credit_tax,
                                    total_tax=total_tax,
                                    net_receipt=net_receipt,
                                    user_id=current_user.id)
            historic = Historic(date=current_date(),
                                description='Input income - net_receipt $' + str(net_receipt),
                                user_id=current_user.id)
            db.session.add(income_to_input)
            db.session.add(historic)
            db.session.commit()
            return redirect(url_for('incomings_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}')
        return render_template('inputincome.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/incomings', methods=['GET', 'POST'])
@login_required
def incomings_page():
    incomings = Incomings.query.order_by(Incomings.date.desc(), Incomings.id.desc()).all()
    total_income = 0.00
    for income in incomings:
        total_income += income.net_receipt
    total_income_value = round(total_income,2)
    return render_template('incomings.html', incomings=incomings, total_income_value=total_income_value)


@app.route('/editincome/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def edit_income(id):
    if user_level(current_user) == 'admin':
        row = Incomings.query.filter_by(id=id).first()
        form = RegisterFormIncome(obj=row)
        if form.validate_on_submit():
            results = Taxes.query.order_by(Taxes.update.desc(), Taxes.id.desc()).first_or_404()
            cash_tax = round(((results.cash_tax  / 100.00) * (form.cash_value.data)), 2)
            debit_tax = round(((results.debit_tax  / 100.00) * (form.debit_value.data)), 2)
            credit_tax = round(((results.credit_tax  / 100.00) * (form.credit_value.data)), 2)
            total_tax = round((float(cash_tax + debit_tax + credit_tax)), 2)
            net_receipt = round((((form.cash_value.data)+(form.debit_value.data)+(form.credit_value.data)) - total_tax), 2)
            row.date = form.date.data
            row.cash_value = form.cash_value.data
            row.tax_cash = cash_tax
            row.debit_value = form.debit_value.data
            row.tax_debit = debit_tax
            row.credit_value = form.credit_value.data
            row.tax_credit = credit_tax
            row.total_tax = total_tax
            row.net_receipt = net_receipt
            row.user_id = current_user.id
            historic = Historic(date=current_date(),
                                description='Edit income id:' + str(row.id),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Income edited!', category="success")
            return redirect(url_for('incomings_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('inputincome.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/deleteincome/<int:id>', methods=['GET', 'POST'])
def delete_income(id):
    if user_level(current_user) == 'admin':
        income_to_delete = Incomings.query.filter_by(id=id).first()
        historic = Historic(date=current_date(),
                                description='Delete income id:' + str(id) + ' net_receipt deleted $ ' + str(income_to_delete.net_receipt),
                                user_id=current_user.id)
        db.session.add(historic)
        db.session.delete(income_to_delete)
        db.session.commit()
        flash(f'Success! Income deleted!', category="success")
        return redirect(url_for('incomings_page'))
    else:
        return redirect(url_for('home_page'))

@app.route('/inputoutgoing', methods=['GET', 'POST'])
@fresh_login_required
def input_outgoing():
    if user_level(current_user) == 'admin':
        form = RegisterFormOutgoing()
        if form.type1.data:
            form.type2.query = Type2.query.filter_by(type1_id=form.type1.data.id).all()
        else:
            form.type2.query = Type2.query.filter(None).all()
        
        if form.validate_on_submit():
            cost_round = round(float(form.cost.data), 2)
            receiver_data = str(form.receiver.data)
            type1 = str(form.type1.data.type1)
            type2 = str(form.type2.data.type2)
            outgoing_to_input = Outgoings(date=form.date.data,
                                    cost=cost_round,
                                    method=form.method.data,
                                    receiver=receiver_data,
                                    type1=type1,
                                    type2=type2,
                                    description=form.description.data,
                                    status=form.status.data,
                                    user_id=current_user.id)
            historic = Historic(date=current_date(),
                                description='Input outgoing total cost $' + str(cost_round),
                                user_id=current_user.id)
            db.session.add(outgoing_to_input)
            db.session.add(historic)
            db.session.commit()
            return redirect(url_for('outgoings_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('inputoutgoing.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route("/get_type1")
def get_types():
    type1_id = request.args.get("type1", type=int)
    type2 = Type2.query.filter_by(type1_id=type1_id).all()
    return render_template("type2_options.html", type2=type2)

@app.route('/outgoings', methods=['GET', 'POST'])
@login_required
def outgoings_page():
    outgoings = Outgoings.query.filter_by(status='open').all()
    total_outgoings = 0.00
    for outgoing in outgoings:
        total_outgoings += outgoing.cost
    total_outgoings_value = round(total_outgoings, 2)
    return render_template('outgoings.html', outgoings=outgoings, total_outgoings_value=total_outgoings_value)


@app.route('/editoutgoing/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def edit_outgoing(id):
    if user_level(current_user) == 'admin':
        row = Outgoings.query.filter_by(id=id).first()
        form = RegisterFormOutgoing(date=row.date,
                                    cost=row.cost,
                                    method=row.method,
                                    description=row.description)
        if form.type1.data:
            form.type2.query = Type2.query.filter_by(type1_id=form.type1.data.id).all()
        else:
            form.type2.query = Type2.query.filter(None).all()
        if form.validate_on_submit():
            receiver_data = str(form.receiver.data)
            cost_round = round(float(form.cost.data), 2)
            type1 = str(form.type1.data.type1)
            type2 = str(form.type2.data.type2)
            row.date = form.date.data
            row.cost = cost_round
            row.method = form.method.data
            row.receiver = receiver_data
            row.type1 = type1
            row.type2 = type2
            row.description = form.description.data
            row.status = form.status.data
            row.user_id = current_user.id
            historic = Historic(date=current_date(),
                                description='Edit outgoing id:' + str(id),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Outgoing has been edited!', category="success")
            return redirect(url_for('outgoings_page'))
        return render_template("editoutgoing.html", form=form, row=row)
    else:
        return redirect(url_for('home_page'))

@app.route('/deleteoutgoing/<int:id>', methods=['GET', 'POST'])
def delete_outgoing(id):
    if user_level(current_user) == 'admin':
        outgoing_to_delete = Outgoings.query.filter_by(id=id).first()
        historic = Historic(date=current_date(),
                                description='Delete outgoing id:' + str(id) + ' total cost $' + str(outgoing_to_delete.cost),
                                user_id=current_user.id)
        db.session.add(historic)
        db.session.delete(outgoing_to_delete)
        db.session.commit()
        flash(f'Success! Outgoing deleted!', category="success")
        return redirect(url_for('outgoings_page'))
    else:
        return redirect(url_for('home_page'))

@app.route('/supplierregister', methods=['GET', 'POST'])
@fresh_login_required
def supplier_register():
    if user_level(current_user) == 'admin':
        form = RegisterFormSupplier()
        if form.validate_on_submit():
            supplier_to_register = Suppliers(company_name=form.company_name.data,
                                             company_id=form.company_id.data, sales_person=form.sales_person.data,contact=form.contact.data, user_id=current_user.id)
            historic = Historic(date=current_date(),
                                description='Register a new supplier: ' + str(form.company_name.data),
                                user_id=current_user.id)
            db.session.add(supplier_to_register)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Supplier has been registered!', category='success')
            return redirect(url_for('suppliers_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('supplierreg.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/suppliers', methods=['GET', 'POST'])
@login_required
def suppliers_page():
    suppliers = Suppliers.query.all()
    return render_template('suppliers.html', suppliers=suppliers)


@app.route('/editsupplier/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def edit_supplier(id):
    if user_level(current_user) == 'admin':
        supplier = Suppliers.query.filter_by(id=id).first()
        form = EditFormSupplier(obj=supplier)
        if form.validate_on_submit():
            supplier.company_name = form.company_name.data
            supplier.company_id = form.company_id.data
            supplier.sales_person = form.sales_person.data
            supplier.contact = form.contact.data
            supplier.user_id = current_user.id
            historic = Historic(date=current_date(),
                                description='Edit supplier\'s data supplier id: ' + str(id),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Supplier edited!', category="success")
            return redirect(url_for('suppliers_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('editsupplier.html', form=form, supplier=supplier)
    else:
        return redirect(url_for('home_page'))

@app.route('/employeeregister', methods=['GET', 'POST'])
@fresh_login_required
def employee_register():
    if user_level(current_user) == 'admin':
        form = RegisterFormEmployee()
        if form.validate_on_submit():
            if form.pic.data:
                pic_filename = secure_filename(form.pic.data.filename)
                pic_name = str(uuid.uuid1()) + '_' + pic_filename
                picture = form.pic.data
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            else:
                pic_name = None

            employee_to_register = Employees(name=form.name.data,
                                    born_date=form.born_date.data,
                                    position=form.position.data,
                                    hire_date=form.hire_date.data,email=form.email.data,contact=form.contact.data, is_actual='yes',pic=pic_name, user_id=current_user.id)
            historic = Historic(date=current_date(),
                                description='Register a new employee: ' + str(form.name.data) + ' to position: ' + str(form.position.data),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.add(employee_to_register)
            db.session.commit()
            return redirect(url_for('employees_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('employeereg.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/employees')
@login_required
def employees_page():
    employees = db.session.execute(db.select(Employees).order_by(Employees.is_actual.desc(), Employees.hire_date)).scalars().all()
    return render_template('employees.html', employees=employees)

@app.route('/employee_detail/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def employee_detail(id):
    if user_level(current_user) == 'admin':
        employee = db.session.execute(db.select(Employees).where(Employees.id == id)).first()
        for i in employee:
            born_date = i.born_date
        age = get_age(current_date(),born_date)
        return render_template('employee_detail.html', employee=employee, age=age)
    else:
        return redirect(url_for('employees_page'))

@app.route('/employee_detail/edit/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def edit_employee(id):
    if user_level(current_user) == 'admin':
        employee = Employees.query.filter_by(id=id).first()
        form = EditFormEmployee(name=employee.name, born_date=employee.born_date, position=employee.position, hire_date=employee.hire_date, email=employee.email, contact=employee.contact, is_actual=employee.is_actual)
        if form.validate_on_submit():
            pic = form.pic.data
            if employee.pic == None:
                if form.pic.data == None:
                    employee.pic = None
                elif form.pic.data:
                    pic_filename = secure_filename(form.pic.data.filename)
                    pic_name = str(uuid.uuid1()) + '_' + pic_filename
                    picture = form.pic.data
                    picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                    employee.pic = pic_name
            elif employee.pic:
                if form.pic.data == None:
                    employee.pic = employee.pic
                elif form.pic.data:
                    old_pic = os.path.join(app.config['UPLOAD_FOLDER'], employee.pic)
                    if os.path.exists(old_pic):
                        os.remove(old_pic)
                        pic_filename = secure_filename(form.pic.data.filename)
                        pic_name = str(uuid.uuid1()) + '_' + pic_filename
                        picture = form.pic.data
                        picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                        employee.pic = pic_name
            employee.name = form.name.data
            employee.position = form.position.data
            employee.born_date = form.born_date.data
            employee.hire_date = form.hire_date.data
            employee.email = form.email.data
            employee.contact = form.contact.data
            employee.is_actual = str(form.is_actual.data)
            employee.user_id = current_user.id
            historic = Historic(date=current_date(),
                                description='Edit employee\'s data employee id: ' + str(id),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Employee data has been edited!', category="success")
            return redirect(url_for('employees_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('editemployee.html', form=form, employee=employee)
    else:
        return redirect(url_for('home_page'))

@app.route('/employee_detail/fire/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def fire_employee(id):
    if user_level(current_user) == 'admin':
        form = FireDateForm()
        if form.validate_on_submit():
            employee = Employees.query.filter_by(id=id).first()
            employee.is_actual = 'no'
            employee.end_date = form.fire_date.data
            historic = Historic(date=current_date(),
                                description='Edit employee\'s status to fired employee id:' + str(id),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Employee data has been edited!', category="success")
            return redirect(url_for('employee_detail', id=id))
        return render_template('firedate.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/payments', methods=['GET', 'POST'])
@login_required
def payments():
    payments = Outgoings.query.filter_by(status='ok').order_by(Outgoings.date.desc(), Outgoings.id.desc()).all()
    total_payments = 0.00
    for payment in payments:
        total_payments += payment.cost
    total_payments_value = round(total_payments, 2)
    return render_template('payments.html', payments=payments, total_payments_value=total_payments_value)


@app.route('/setpayment/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def set_payment(id):
    if user_level(current_user) == 'admin':
        payment = Outgoings.query.filter_by(id=id).first()
        payment.status = 'ok'
        payment.user_id = current_user.id
        historic = Historic(date=current_date(),
                                description='Setting payment outgoing payed id:' + str(id),
                                user_id=current_user.id)
        db.session.add(historic)
        db.session.commit()
        flash(f'Success! Payment has been registered!', category="success")
        return redirect(url_for('payments'))
    else:
        return redirect(url_for('home_page'))

@app.route('/editpayment/<int:id>')
@fresh_login_required
def edit_payment(id):
    if user_level(current_user) == 'admin':
        payment = Outgoings.query.filter_by(id=id).first()
        payment.status = 'open'
        payment.user_id = current_user.id
        historic = Historic(date=current_date(),
                                description='Edit payment change status to open outgoing id: ' + str(id),
                                user_id=current_user.id)
        db.session.add(historic)
        db.session.commit()
        flash(f'Success! Ougoing status has been updated!', category="success")
        return redirect(url_for('outgoings_page'))
    else:
        return redirect(url_for('home_page'))

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('login_page'))


@app.route('/userregister', methods=['GET', 'POST'])
@fresh_login_required
def user_register():
    if user_level(current_user) == 'admin':
        form = RegisterFormUser()
        if form.validate_on_submit():
            user_to_register = Users(name=form.name.data,
                                    username=form.username.data,
                                    email=form.email.data,
                                    password=form.password.data,
                                    level=form.level.data)
            historic = Historic(date=current_date(),
                                description='Register a new user: ' + str(form.username.data) + ' level: ' + str(form.level.data),
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.add(user_to_register)
            db.session.commit()
            flash(f'Success! User has been registered!', category="success")
            return redirect(url_for('login_page'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('userreg.html', form=form)
    else: 
        return redirect(url_for('home_page'))

@app.route('/user')
@login_required
def user_page():
    if user_level(current_user) == 'admin':
        historic = db.session.execute(db.select(Historic.id, Historic.date, Historic.description, Users.username).join_from(Historic, Users).order_by(Historic.id.desc())).all()
        return render_template('user.html', historic=historic)
    else:
        return render_template('user.html')


@app.route('/edit_user_email/<int:id>', methods=['GET', 'POST'])
@fresh_login_required
def edit_email(id):
    form = ChangeEmailForm()
    if form.validate_on_submit():
        get_user_info = Users.query.filter_by(id=id).first()
        get_user_info.email = form.new_email.data
        historic = Historic(date=current_date(),
                                description='Edit user email',
                                user_id=current_user.id)
        db.session.add(historic)
        db.session.commit()
        flash(f'Success! Email has been updated!', category="success")
        return redirect(url_for('user_page'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
    return render_template('edit_email.html', form=form)


@app.route('/edit_user_pass/<int:id>', methods=['GET', 'POST'])
def edit_pass(id):
    form = ChangePassForm()
    if form.validate_on_submit():
        get_user_info = Users.query.filter_by(id=id).first()
        if get_user_info.check_password(password_login=form.current_pass.data):
            new_pass = form.new_pass.data
            get_user_info.hash = generate_password_hash(new_pass)
            historic = Historic(date=current_date(),
                                description='Edit user password',
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.commit()
            flash('Password has been changed!', category='success')
            return redirect(url_for('user_page'))
        else:
            flash('Current password is incorrect!', category='danger')
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
    return render_template('edit_pass.html', form=form)
    

@app.route('/taxes')
@login_required
def taxes():
    taxes = db.session.execute(db.select(Taxes.id, Taxes.update, Taxes.cash_tax, Taxes.debit_tax, Taxes.credit_tax, Users.username).join_from(Taxes, Users).order_by(Taxes.update.desc(), Taxes.id.desc())).all()
    return render_template('taxes.html', taxes=taxes)

@app.route('/set_taxes', methods=['GET', 'POST'])
@fresh_login_required
def set_taxes():
    if user_level(current_user) == 'admin':
        form = SetTaxesForm()
        if form.validate_on_submit():
            taxes_to_set = Taxes(update=form.update.data,
                                    cash_tax=form.cash_tax.data,
                                    debit_tax=form.debit_tax.data,
                                    credit_tax=form.credit_tax.data,user_id=current_user.id)
            historic = Historic(date=current_date(),
                                description='Setting taxes updated taxes',
                                user_id=current_user.id)
            db.session.add(historic)
            db.session.add(taxes_to_set)
            db.session.commit()
            flash(f'Success! Taxes has been updated!', category="success")
            return redirect(url_for('taxes'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template('set_taxes.html', form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/settypes', methods=['GET', 'POST'])
@fresh_login_required
def settypes():
    if user_level(current_user) == 'admin':
        typ1 = db.session.execute(db.select(Type1.type1)).all()
        typ2 = db.session.execute(db.select(Type1.type1, Type2.type2).join_from(Type2, Type1).order_by(Type1.type1)).all()
        return render_template('settypes.html', typ1=typ1, typ2=typ2)
    else:
        return redirect(url_for('home_page')) 

@app.route('/set_type1', methods=['GET', 'POST'])
@fresh_login_required
def set_type1():
    if user_level(current_user) == 'admin':
        form = SetType1Form()
        if form.validate_on_submit():
            type1 = string_format(form.type1.data)
            type1_to_register = Type1(type1=type1)
            historic = Historic(date=current_date(),
                                description='Setting type1',
                                user_id=current_user.id)
            db.session.add(type1_to_register)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Type 1 has been registered!', category='success')
            return redirect(url_for('settypes'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')  
        return render_template("set_type1.html", form=form)
    else:
        return redirect(url_for('home_page'))

@app.route('/set_type2', methods=['GET', 'POST'])
@fresh_login_required
def set_type2():
    if user_level(current_user) == 'admin':
        form = SetType2Form()
        if form.validate_on_submit():
            t1_id = int(form.type1.data.id)
            type2 = string_format(form.type2.data)
            type2_to_register = Type2(type2=type2, type1_id=t1_id)
            historic = Historic(date=current_date(),
                                description='Setting type2',
                                user_id=current_user.id)
            db.session.add(type2_to_register)
            db.session.add(historic)
            db.session.commit()
            flash(f'Success! Type 2 has been registered!', category='success')
            return redirect(url_for('settypes'))
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f'Form data does not meet the requirements: {error_message}', category='warning')
        return render_template("set_type2.html", form=form)
    else:
        return redirect(url_for('home_page'))