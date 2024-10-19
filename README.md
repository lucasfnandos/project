# CASHFLOW WEB SITE

### Video Demo: https://www.youtube.com/watch?v=htKamE3Mlak
### Description

**CashFlow** is a website designed to manage financial data for small businesses. It allows owners and administrators to track both incoming and outgoing expenses efficiently. Additionally, CashFlow offers features that enable businesses to store essential information about suppliers and employees. Many small businesses are familiar with the challenges of juggling multiple roles, as owners often handle both operational tasks and administrative duties. CashFlow is an easy-to-use tool that simplifies financial management and data visualization, making it a better option than complex personal spreadsheets.

### HOW TO USE IT?:
  - **Welcome page**: The first page displays a welcome message and a link to the log in page. For the very first time the application will run, when clicking the link will lead not to the login page but to the password change page instead. This is beacuse the first user is created automatically with a standard password, and change password is considered for security reasons.
    ![alt text](/project/static/images/image-8.png)
  - **User Password Change**: A form with three fields is displayed.
    - **Current Password**: The current password for the first access is equat to the standard setted password: foofoo.
    - **New Password**: The password must have the minimum of 6 and maximum of 12 characters.
    - **Confirm Password**: To complete and set a new password a confirmation is required.
    ![alt text](/project/static/images/image-9.png)
  - **User page**: After the password change the user page is displayed, two cards are shown the first one shows the user informations such as name, email, the level, also the link to change the password. At the second card the historic of users are shown where is possible to see any data added, edited or deleted from the application.
    ![alt text](/project/static/images/image-10.png)
    - **Email**: The user's email is shonw as a link when clicked the update email page is displayed. The email follows the same rule of the password for the first time of running the application, wich means that the first email registered for admin user is a standard not valid email 'admin@email.com' and can be edited. At the update email page two fields are displayed where the new email is setted, a confirmation is required.
      ![alt text](/project/static/images/image-11.png)
  - **WHERE TO BEGIN?**: The first inputs recommended to set will allow the perfect running of the application and the data visualization.
    - **Taxes**: When comes to taxes, there are many types and ways the business has to pay it, but most of all are incomings taxes that are discounted directly from the income by goverments or the company that manages the payments transactions. To properly calculates the incomings it is necessary to input the taxes in percentage, for instance to input a 5% of a cash tax the number 5 is filled on the form at the updae taxes page. A table with the historic of all taxes is displayed. The last record is used to calculate the incomings after taxes, when to update the taxes is needed it is done by clicking the button "Update Taxes".
      ![alt text](/project/static/images/image-12.png)
      ![alt text](/project/static/images/image-13.png)
      ![alt text](/project/static/images/image-14.png)
      ![alt text](/project/static/images/image-15.png)
    - **Suppliers**: The suppliers are very important to any type of business, and even small ones has a lot of suppliers. To manage the data about the suppliers can be crucial for a business success. In this application when input a new outgoing at the form the supplier fiele is displayed as a select list, and this is done with a search at the database on the table containing the suppliers registered. This is why it is strongly recommended to register the suppliers, the tip is it can starts with the main suppliers.
      ![alt text](/project/static/images/image-16.png)
      ![alt text](/project/static/images/image-17.png)
    - **Types**: The types defines the categories they are divide in hierarchy where Type1 is the main category and Type2 is the subcategory. This is setted to help the administrator to visualize wich are the most important categories are the outgoings. It can help, for instance to aim where the improvments can be make to reduce the expense and increase the liquid profit.
      ![alt text](/project/static/images/image-18.png)
      - **Type 1**: Always starts registering the Type 1, clicking at "Register Type 1" button then a single form field will display allowing the registration process.
      ![alt text](/project/static/images/image-19.png)
      - **Type 2**: After register a Type 1 the Type 2 can be added. At the register Type 2 page two form fields are displayed where the Type 1 can be choosen from a select list.
      ![alt text](/project/static/images/image-20.png)
      ![alt text](/project/static/images/image-21.png)
  - **Employee Registration**: To store the employees data is not just necessary but in some cases is required by governments. At the register employee page the basics information can be filled through the form the only one field that is not required is the picture field, it can be done after at the employees page.
    ![alt text](/project/static/images/image-22.png)
    ![alt text](/project/static/images/image-23.png)
  - **Employees Page**: The employee data can be accessed at the employee card clicking at its name. Then a page with all informations is displayed, also the buttons "Edit" and "Fire" are shown. As suggested any updates at employee data can be done at "edit" where the form with the informations fields is displayed. With the "fire" button t is possible to set a end of employment date after that the information "current employee" is shonw as "no". If the fire date has to be edited, some steps has to be followed: first clicking on the "Edit" button to display the editing form and there set the field "Current employee" as "Yes" then register the updates, second clicking again in the its name to show the informations page and click the "Fire" button to set the updated date of fire.
    ![alt text](/project/static/images/image-24.png)
    ![alt text](/project/static/images/image-25.png)
  - **Incomings**: The incomings can be added by clicking at the "+Add" button at incomings page. At the incoming registration page all the informations are required and the fields must be filled to properly register the incoming.
    ![alt text](/project/static/images/image-26.png)
    ![alt text](/project/static/images/image-27.png)
    ![alt text](/project/static/images/image-28.png)
    ![alt text](/project/static/images/image-29.png)
  - **Outgoings**: The outgoings follows the same logic of incomings, first at the navegation bar clicking in Finance -> Outgoings to display the outgoings page. To add a new one it is clicking at the "+Add" button to display the form where the field "Status" can be filled as "OPEN" or "OK", this is because sometimes the outgoing will be paid in the future, and this is used to help for planning the amount of outgoings that is coming. When an ougtoing is registered as "OPEN" it will be list at outgoings page otherwise if is registered as "OK" it will be list at the payments page.
    ![alt text](/project/static/images/image-30.png)
    ![alt text](/project/static/images/image-31.png)
    ![alt text](/project/static/images/image-32.png)
    ![alt text](/project/static/images/image-33.png)
  - **Register a User**: To register a new user it is easy, at the navegation bar clicking Register -> User. The user registration page is displayed all the fields from the form are required data type. The user level can be setted as "Admin" or "Viewer", the viewer users are not allowed to input data on the application this is a feature to allow stakeholders to view but not to manipulate the data. After create a new user profile the login form is displayed where the new user can input its data to log in the application but only in this case the navegation bar still shows the links to the pages to allow the current user keeping navegates through the application.
    ![alt text](/project/static/images/image-34.png)
    ![alt text](/project/static/images/image-35.png)
  - **Log Out**: The log out link will logout the current user and forget its authentication, the log in page will be displayed also the links to the pages will not be accessable at the navegation bar.
    ![alt text](/project/static/images/image-36.png)

### HOW IS IT WORK?:
The application is built in Python using Flask to module and integrate the extensions in the backend, while in the frontend the data visualization is carried for open-source CSS framework Bootstrap which provides pre-designed components and layout styles, and help streamline the process of creating aesthetically pleasing and functional user interfaces.
To combinate static HTML file to dynamic data Jinja template engine is used. Jinja allows to create templates that define the structure and layout of HTML pages, and then dynamically populate those templates with data from the application. This separation makes the code more organized, maintainable, and reusable.
For the database SQLAlchemy is applied providing a high-level API for interacting with relational databases by mapping Python objects to database tables. SQLAlchemy abstracts the complexities of raw SQL queries, allowing to work with databases using Python objects and methods, it supports various database systems and offers powerful querying capabilities.

### PACKAGE PROJECT:
The project package containing the three main modules: models, forms and routes. In the __init__ file the app Flask object is _instancionated_.

#### **Imports**
- **`from flask import Flask`**: Imports the Flask class to create a Flask application instance.
- **`from flask_sqlalchemy import SQLAlchemy`**: Imports SQLAlchemy to handle database interactions.
- **`from flask_login import LoginManager`**: Imports LoginManager to manage user sessions.
- **`from project.helper import usd, contact, comp_id`**: Imports custom Jinja2 filters or functions (`usd`, `contact`, `comp_id`) from the `helper` module.

#### **Application Setup**
- **`app = Flask(__name__)`**: Creates an instance of the Flask application.

- **`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'`**: Configures the SQLAlchemy database URI to use SQLite with a database file named `project.db`.

- **`app.config['SECRET_KEY'] = 'fbdb5eb6dafa8db120aee73d'`**: Sets a secret key for the Flask application. This key is used for session management and other cryptographic operations. **(Note: In a production environment, it's recommended to use a more secure, environment-specific key.)**

- **`UPLOAD_FOLDER = 'project/static/images/'`**: Defines the directory path where uploaded files will be stored.
- **`app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER`**: Configures the Flask application to use the specified upload folder.

#### **Extensions Initialization**
- **`db = SQLAlchemy(app)`**: Initializes SQLAlchemy with the Flask application instance, enabling ORM capabilities.

- **`login_manager = LoginManager(app)`**: Initializes Flask-Login with the Flask application instance to manage user sessions and authentication.

#### **Custom Jinja2 Filters**
- **`app.jinja_env.filters["usd"] = usd`**: Adds a custom Jinja2 filter named `usd` to format values as US dollars. `usd` is expected to be a function imported from the `helper` module.

- **`app.add_template_filter(contact)`**: Registers a custom Jinja2 filter named `contact`, which is used to process or format contact information. `contact` is a function imported from the `helper` module.

- **`app.add_template_filter(comp_id)`**: Registers a custom Jinja2 filter named `comp_id`, which is used to process or format company or person identification number. `comp_id` is a function imported from the `helper` module.

#### **Routing Imports**
- **`from project import routes`**: Imports the routing definitions from the `routes` module. This is typically where the application's routes and view functions are defined.


### MODELS:
The following code defines a Flask application with SQLAlchemy models for managing users, financial transactions, suppliers, employees, taxes, and historical records. It includes functionalities for password hashing and user session management using Flask-Login. The database schema is created based on the model definitions when the application context is active.
This code snippet represents a Flask application using SQLAlchemy for ORM (Object-Relational Mapping) and Flask-Login for user session management. Here’s a detailed breakdown of the key components:

#### **Imports**
- **`from project import db, app, login_manager`**: Imports the database instance (`db`), Flask application instance (`app`), and login manager (`login_manager`) from the `project` module.
- **`from werkzeug.security import generate_password_hash, check_password_hash`**: Imports functions for hashing and checking passwords.
- **`from flask_login import UserMixin`**: Imports `UserMixin` which provides default implementations for user session management.

#### **User Management**
- **`@login_manager.user_loader`**: This decorator registers a function that takes a user ID (from session) and returns the corresponding `Users` object. It allows Flask-Login to retrieve the user from the database based on the session ID.

- **`class Users(db.Model, UserMixin)`**: Defines a `Users` model class for user management.
  - **Attributes**:
    - `id`: Primary key for the user.
    - `username`: Unique username for login.
    - `name`: Full name of the user.
    - `email`: Email address.
    - `hash`: Password hash.
    - `level`: User's access level.
  - **Password Management**:
    - `@property def password`: Getter method that returns the password (in practice, this should be avoided to prevent accessing the raw password).
    - `@password.setter def password`: Sets the password by hashing the plain text password.
    - `def check_password(self, password_login)`: Checks if the provided password matches the stored hash.

#### **Database Models**

- **`class Incomings(db.Model)`**: Represents incoming financial transactions.
  - **Attributes**:
    - `id`, `date`, `cash_value`, `tax_cash`, `debit_value`, `tax_debit`, `credit_value`, `tax_credit`, `total_tax`, `net_receipt`: Various financial fields.
    - `user_id`: Foreign key linking to the `Users` table.

- **`class Outgoings(db.Model)`**: Represents outgoing expenses.
  - **Attributes**:
    - `id`, `date`, `cost`, `method`, `receiver`, `type1`, `type2`, `description`, `status`: Various expense-related fields.
    - `user_id`: Foreign key linking to the `Users` table.

- **`class Suppliers(db.Model)`**: Represents suppliers.
  - **Attributes**:
    - `id`, `company_name`, `company_id`, `sales_person`, `contact`: Supplier details.
    - `user_id`: Foreign key linking to the `Users` table.
  - **`__repr__` Method**: Provides a string representation of the supplier using `company_name`.

- **`class Employees(db.Model)`**: Represents employees.
  - **Attributes**:
    - `id`, `name`, `born_date`, `position`, `hire_date`, `email`, `contact`, `is_actual`, `end_date`, `pic`: Various employee details.
    - `user_id`: Foreign key linking to the `Users` table.

- **`class Taxes(db.Model)`**: Represents tax rates.
  - **Attributes**:
    - `id`, `update`, `cash_tax`, `debit_tax`, `credit_tax`: Tax-related fields.
    - `user_id`: Foreign key linking to the `Users` table.

- **`class Type1(db.Model)`**: Represents a category type.
  - **Attributes**:
    - `id`, `type1`: Category type.

- **`class Type2(db.Model)`**: Represents a subcategory type that is linked to `Type1`.
  - **Attributes**:
    - `id`, `type2`, `type1_id`: Subcategory type and foreign key linking to `Type1`.

- **`class Historic(db.Model)`**: Represents historical records or logs.
  - **Attributes**:
    - `id`, `date`, `description`: Historical record details.
    - `user_id`: Foreign key linking to the `Users` table.

#### **Database Initialization**
- **`with app.app_context(): db.create_all()`**: Initializes the database schema by creating all the tables defined by the models within the application context.

### FORMS:

This code defines multiple forms for various functionalities in a Flask application using Flask-WTF and WTForms. These forms handle user registration, supplier and employee management, financial transactions, and other administrative tasks. The forms include field validation to ensure data integrity and uniqueness, and utilize custom queries for dynamic field options.
This code snippet defines a series of forms using Flask-WTF and WTForms for handling various user interactions and data submissions in a Flask application. These forms cover user registration, supplier and employee management, financial transactions, and more.
**WTForms**  
**`WTForms`** is a flexible and extensible library for handling web form creation and validation in Python applications. It simplifies the process of generating forms, managing form data, and validating user input. With WTForms, you can define form fields, apply validation rules, and handle form submissions efficiently, enhancing the user experience and ensuring data integrity.
**email_validator**  
The **`email_validator`** library is a Python package used for validating email addresses. It ensures that email addresses conform to standard formats and can even perform domain validation to check if the email address's domain is valid. By using email_validator, you can improve the reliability of user input and reduce errors related to invalid email addresses in your application.
**Werkzeug**  
**`Werkzeug`** is a comprehensive WSGI (Web Server Gateway Interface) library for Python that provides utility functions and tools for building web applications. It serves as the foundation for Flask and offers features such as request and response handling, URL routing, and debugging tools. Werkzeug helps manage the underlying web server interactions, making it easier to develop and test web applications.

#### **Imports**
- **`from flask_wtf import FlaskForm`**: Imports the base class for creating forms in Flask using Flask-WTF.
- **`from flask_wtf.file import FileField`**: Imports `FileField` for handling file uploads.
- **`from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField, SelectField, RadioField`**: Imports various field types for creating forms.
- **`from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError`**: Imports validators for form fields.
- **`from wtforms_sqlalchemy.fields import QuerySelectField`**: Imports `QuerySelectField` for selecting options from SQLAlchemy queries.
- **`from project.models import Users, Suppliers, Employees, Type1, Type2`**: Imports SQLAlchemy models used in forms for validation and data selection.
- **`from datetime import datetime`**: Imports `datetime` for date handling (though not used directly in this snippet).

#### **Form Definitions**

- **`RegisterFormUser(FlaskForm)`**: Form for user registration.
  - **Fields**:
    - `name`: Full name of the user.
    - `username`: Username, with validation to ensure uniqueness.
    - `email`: Email address with validation.
    - `password`: Password with length validation.
    - `confirm_pass`: Confirmation password field.
    - `level`: User access level (admin or viewer).
    - `submit`: Submit button.
  - **Validation**:
    - `validate_username`: Ensures the username is unique by querying the `Users` model.

- **`RegisterFormSupplier(FlaskForm)`**: Form for supplier registration.
  - **Fields**:
    - `company_name`: Name of the company.
    - `company_id`: Company registration ID with length validation.
    - `sales_person`: Sales person’s name.
    - `contact`: Contact number with exact length validation.
    - `submit`: Submit button.
  - **Validation**:
    - `validate_company_id`: Ensures the company ID is unique by querying the `Suppliers` model.

- **`RegisterFormEmployee(FlaskForm)`**: Form for employee registration.
  - **Fields**:
    - `name`, `born_date`, `position`, `hire_date`, `email`, `contact`, `pic`: Employee details and profile picture upload.
    - `submit`: Submit button.
  - **Validation**:
    - `validate_name`: Ensures the employee name is unique by querying the `Employees` model.

- **`RegisterFormIncome(FlaskForm)`**: Form for recording incoming financial transactions.
  - **Fields**:
    - `date`, `cash_value`, `debit_value`, `credit_value`: Various financial fields.
    - `submit`: Submit button.

- **`RegisterFormOutgoing(FlaskForm)`**: Form for recording outgoing expenses.
  - **Fields**:
    - `date`, `cost`, `method`, `receiver`, `type1`, `type2`, `description`, `status`: Various fields related to expenses.
    - **Queries**:
      - `choice_query`: Returns a query for selecting suppliers.
      - `type_query`: Returns a query for selecting Type1 categories.
    - `submit`: Submit button.

- **`LoginForm(FlaskForm)`**: Form for user login.
  - **Fields**:
    - `username`: Username field.
    - `password`: Password field.
    - `submit`: Submit button.

- **`ChangePassForm(FlaskForm)`**: Form for changing a user's password.
  - **Fields**:
    - `current_pass`, `new_pass`, `confirm_pwd`: Fields for current and new passwords.
    - `submit`: Submit button.

- **`SetTaxesForm(FlaskForm)`**: Form for setting tax rates.
  - **Fields**:
    - `update`, `cash_tax`, `debit_tax`, `credit_tax`: Tax-related fields.
    - `submit`: Submit button.

- **`EditFormEmployee(FlaskForm)`**: Form for editing employee details.
  - **Fields**:
    - `name`, `born_date`, `position`, `hire_date`, `email`, `contact`, `is_actual`, `pic`: Various fields including a picture upload.
    - `submit`: Submit button.

- **`EditFormSupplier(FlaskForm)`**: Form for editing supplier details.
  - **Fields**:
    - `company_name`, `company_id`, `sales_person`, `contact`: Supplier details.
    - `submit`: Submit button.

- **`ChangeEmailForm(FlaskForm)`**: Form for changing a user's email address.
  - **Fields**:
    - `new_email`, `confirm_email`: Email fields with validation.
    - `submit`: Submit button.

- **`FireDateForm(FlaskForm)`**: Form for setting a termination date for an employee.
  - **Fields**:
    - `fire_date`: Termination date.
    - `submit`: Submit button.

- **`SetType1Form(FlaskForm)`**: Form for setting a Type1 category.
  - **Fields**:
    - `type1`: Type1 category name.
    - `submit`: Submit button.
  - **Validation**:
    - `validate_type1`: Ensures the Type1 name is unique.

- **`SetType2Form(FlaskForm)`**: Form for setting a Type2 category, which is linked to Type1.
  - **Fields**:
    - `type2`, `type1`: Type2 category name and associated Type1 category.
    - `submit`: Submit button.
  - **Validation**:
    - `validate_type2`: Ensures the Type2 name is unique.
    - **Query**:
      - `type_query`: Returns a query for selecting Type1 categories.


### ROUTES
This code snippet includes imports necessary for managing user sessions, handling file uploads, performing database queries, and working with unique identifiers and JSON data. The imported functions and modules provide essential capabilities for routing, user authentication, file handling, and data operations within a Flask web application.
This code snippet focuses on importing the essential modules and functions required for various functionalities in a Flask web application. It involves user authentication, file handling, and data operations.

#### **Imports**

- **`from project import app`**:
  - **Purpose**: Imports the Flask application instance from the `project` module. This instance is used to define routes and configure the application.

- **`from flask import render_template, redirect, url_for, flash, request`**:
  - **`render_template`**: Renders HTML templates with optional dynamic content.
  - **`redirect`**: Redirects the client to a different URL.
  - **`url_for`**: Generates a URL for a given function or endpoint.
  - **`flash`**: Sends a one-time message to the user, typically used for notifications.
  - **`request`**: Provides access to the request data, such as form inputs, query parameters, and file uploads.

- **`from flask_login import login_user, logout_user, login_required, fresh_login_required, current_user`**:
  - **`login_user`**: Logs in a user and manages session details.
  - **`logout_user`**: Logs out the current user and clears the session.
  - **`login_required`**: Decorator that ensures a user is authenticated before accessing a route.
  - **`fresh_login_required`**: Decorator that ensures a user has a fresh login session (for routes requiring re-authentication).
  - **`current_user`**: Provides access to the current logged-in user’s details.

- **`from werkzeug.utils import secure_filename`**:
  - **Purpose**: Ensures that filenames are safe to use when saving files on the server. It sanitizes the filename to prevent directory traversal attacks.

- **`from sqlalchemy import select, func`**:
  - **`select`**: Constructs SQL SELECT statements for querying the database.
  - **`func`**: Provides access to SQL functions (e.g., aggregate functions) for use in queries.

- **`import uuid as uuid`**:
  - **Purpose**: Imports the UUID module for generating unique identifiers. UUIDs are often used for unique keys or identifiers within the application.

- **`import os`**:
  - **Purpose**: Provides functions for interacting with the operating system, such as file and directory manipulation. Commonly used for path operations and environment variables.

- **`import json`**:
  - **Purpose**: Handles JSON data, including parsing JSON strings and converting Python objects to JSON format. Useful for data exchange and configuration.

#### **Function**
- **`user_level()`**:
  - **Purpose**: Returns the user's level, two strings value can be returned "viewer" or "admin" witch stands for administrator. The viewer level allows the access to the page by some user that can visualize but not manipulate the datas.
  - **Logic**: Using the current_user method to take its id and use it on a query that looks for the user level on Users table. Than returns the user's level.
  This function will be called in every route thats allow the user to input or change data in database, ensuring that only adiministrator users level will manipulate and create it.

#### **Route**
- **`@app.route('/', methods=['GET', 'POST'])`**:
  - **Route Definition**: The decorator defines a route for both GET and POST requests at the root URL (/).
  - **Redirect**: The index function simply redirects any request that comes to the root URL to the home_page route. This is useful for guiding users to the main page of your application without directly exposing the root URL's logic.
  - **Template**: In the home.htlm page an if statement is setted. If the currente_user.is_authenticated method returns TRUE all the data containing the dashboards is displayed otherwise if the user is not authenticated an welcoming message is shown as well as the link to redirect for login page.

  ![welcome-message](/project/static/images/image-1.png)

- **`@app.route('/login', methods=['GET', 'POST'])`**:
  - **Route Definition**: The decorator defines a route for both GET and POST requests at the /login URL.
  - **Database Check and Admin Creation**: If no users exist in the database an admin user is created and added to it. This sets the first user in the database for the first time the program will be run, and a standard password is created and it must be change for security. Only in this case the link for access in the welcome page will lead to the user's password change page and a card will flash to advise the user t change the standard password for a new one.
    - **Considerations**: There is no link to create a user profile before the login page, and the reason is we want to ensure only allowed users will access it.
  - **Form Handling**: The LoginForm is instantiated. If the form is submitted via POST and validated, it checks if the user exists and if the password is correct. Upon successful login, the user is redirected; otherwise, an error message is shown.
  - **Rendering the Template**: Finally, the login page is rendered with the login form.

- **`@app.route('/home')`**:
  - **Route Definition**: The decorator defines a route for the /home URL.
  - **Date and Initialization**: Fetch current date and initialize variables for holding monthly and yearly financial data.
    - **Search Date**: The current date is stored on a variable in format yyyy-mm-dd. This variable is going to be used to set the period of time to query the database at collecting the data. Then two variables receive the current year and month, so this allows to search through every month from the actual month behind up to the first month of the current year.
      ```
      get_current_date = current_date()
      set_year_search = get_current_date.year
      set_month_search = get_current_date.month
      ```
    - **Loop through the current year**: An while loop is setted where the iterator "i" is equal or greater than the corespondent numeric current month number, which means the while loop is TRUE from the first month of the current year until the actual month. In side of each loop all the data of the months are calculated and pushed to a list using the index starting from zero, this way it follows the rule of a line where the first data pushed remains in the first index of the list and so on up to the end of the indexes.
      ```
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
      ```  
    - **Months names**: Inside the while loop the months names that means the months according to the numeric months from one (January) up to the actual month is get through thehelper method called getmonth_name(). Then each month is pushed to a list using the same line rule from the paragraph before, this is goint to be used as the legend of the charts of incomings and outgoings.
      ```
      months = getmonth_name(i)
      months_list.insert((i-1), months)
      i += 1
      ```

    - **Search Date Year Before**: The same idea of the while loop used to the current year is applied to the year before search data. To look for months in the year before a new variable called months_qty is setted this variable takes 12 minus the numeric of current month, the result is how many months there is in the year before to complete 12 months considering the current month. All this to have the year-to-date data.
      ```
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
      ```
  - **Render Template**: Pass all the computed data to the home.html template for rendering.
  - **Dashboard**: In the home.html page after user authentication the dashboard is renderized with 11 elements where all financial data is displayed by graphs and tables.
    - **Finance Data**: The first table shows the tracking of incomings and outgoings in different period of time. Also the difference between incomings and outgoings is shown as liquid profit.
  ![finance-data-table](/project/static/images/image-2.png)
    - **Incomings and Outgoings**: Twos charts are shown side by side in a row displaying the year-to-date incomings and outgoings values both in the bar chart. Through these chats it is possible to see the evolution in a period of a year.
  ![incomings-outgoings-charts](/project/static/images/image-3.png)
    - **Cash and Bank Account**: The table the total amount of incomings receive in cash and in the bank account via debit and credit card transactions. The outgoings paid in cash and via bank account also is calculated and the total accumulated values are displayed.
  ![cash&bankaccount-table](/project/static/images/image-4.png)
    - **Liquid Profit and Total Cash Flow**: The liquid profit chart displays a line chart with the difference between incomings and outgoings accumuluted by months in a period of a year, in this chart it is possible to visualize how much is the profit. To calculate the profit all the incomings and outgoings are considered, even the outgoings with "open" (not paid yet) status. The total cash flow pie chart is displayed, and it shows the total values of incomings and outgoings.
  ![liquid-profit-total-cashflow](/project/static/images/image-5.png)
    - **Incomings taxes**: The sum of all taxes applied to the incomings values are displayed by each type of income as well as the sum of total taxes.
    - **Outgoings vs. Incomings**: In this table the percentages of top five outgoings type against the total incomings are displayed, wich means that from the total incomings how much the top five types represents.
  ![Incomings-taxes-incomings-vs-outgoings](/project/static/images/image-6.png)
    - **Incomings types**: The doughnut chart shows the distribution of incomings according to the receivers values from cash, debit and credit card.
    - **Top 5 suppliers**: The pie chart displays the amount expend with the top 5 suppliers.
    - **Top 5 outgoings types**: The pie chart displays the amount expend with the top 5 types of outgoings.
  ![pie-chart-incomings-suppliers-types](/project/static/images/image-7.png)

- **`Standard Methods for Routes`**: Some routes have similar objectives, such as adding, editing, or deleting data, which results in shared logic across these routes. The standard behavior for these operations is defined as follows:
  - **Routes to add data**: To add data in the database first a form page is renderized, all the forms are managed using the WTForms extension where it is possible to set the data type field also includes the validators that helps to validate on the server side the inputs. The WTForms forms field allows to query returns wich means the field can be filled by data stored on the database, this is used for instance to return a select field to register an outgoing at the "type" (category) field, in this case the "types" are added to the database by the user then can be choosen to categorize an outgoing. After the forms validations a variable stores the query where the form field data is related to a column in the database's table, another variable sotres wich is called the "historic" data to register the operation in a historic table. Then both of variables are added to the databeses and then a commit is done. At the end most of routes redirects to the view page where all data added can be seen.
  - **Routes to edit data**: Usually the id of the data to be edited is send to the route, as a parameter of the route function a query looks for the data using its id. Then a variable containing the modification is related to the data to be edited. For the porpouse of historic registration the variable containing the query to register all modification data is add to the database, and finnaly is commited. Using the same logic of add data mostly of routes at this point redirects to the view page.
  - **Routes to delete data**: To delete data is pretty same of edit one, the id is send as a parameter of the route function then a query looks for the data is stored in a variable that is finnaly send to delete to the database. The historic management is made the same way as it made in the add and edit routes. Some of data cannot be deleted because it is important the avoid manipulation of the results.

- **`Routes for employees data management`**: The routes to manage the employees data are quite different from others routes. Throught the employees route a table cointaining basics informations of all employees is rederized a template. Then at the template, for more datails it is possible to see the datailed employee data clicking on its own name link, a new route is taken where if the user's level allows the rederized tamplate shows all informations incluiding their photo if exists, also at this template there is the "Fire" button where the end date of te contract can be setted and the "is actual" employee status is changed to "NO" wich means the employee is not a crew member anymore.
  - **Editing fire date**: To edit a fire date fisrt the employee status has to setted as a actual employee, then at the detailed informations page the "fire" button will reapair allowing to be clicked and the new fire date can be setted. 

### HELPER:
This code provides utility functions for handling and formatting dates, phone numbers, company IDs, and financial values. It includes functions for calculating ages, formatting currency and contact information, and dealing with date-related computations. These utilities are helpful for standardizing and presenting data in a user-friendly format.
This code snippet defines a set of utility functions for date manipulation, formatting, and custom string operations. It includes functions to format dates, calculate age, and format strings and numbers in a user-friendly way.

#### **Imports**
- **`import datetime`**: Imports the `datetime` module for working with dates and times.
- **`from datetime import datetime, timedelta`**: Imports specific classes and functions from `datetime`.
- **`from dateutil.relativedelta import relativedelta`**: Imports `relativedelta` for computing date differences in terms of years, months, etc.
- **`import calendar`**: Imports the `calendar` module to work with calendar-related functions.

#### **Function Definitions**

- **`custom_calendar()`**:
  - **Purpose**: Returns the current date in a custom formatted string, including the day of the week, month name, and the day with an ordinal suffix.
  - **Logic**:
    - Uses `datetime.now()` to get the current date and time.
    - Determines the day of the week and month name using the `calendar` module.
    - Applies a custom ordinal suffix to the day of the month (`st`, `nd`, `rd`, `th`).

- **`current_date()`**:
  - **Purpose**: Returns the current date.
  - **Logic**: Uses `datetime.now()` and extracts the date part.

- **`get_date(year, month, day)`**:
  - **Purpose**: Attempts to create a `datetime` object for a specified year, month, and day. If the provided day is invalid, it tries the previous days up to three days before.
  - **Logic**:
    - Tries to create a date with the given year, month, and day.
    - If it fails (likely due to invalid day), it adjusts the day backward by one, two, or three days.

- **`getmonth_name(number)`**:
  - **Purpose**: Returns the name of the month corresponding to a given number.
  - **Logic**: Uses `calendar.month_name` to fetch the month name based on the number.

- **`get_week_before()`**:
  - **Purpose**: Returns the date one week before the current date.
  - **Logic**: Subtracts a `timedelta` of one week from the current date.

- **`usd(value)`**:
  - **Purpose**: Formats a numerical value as a US dollar currency string.
  - **Logic**: Converts the value to a string formatted as currency. If the value is `None`, it returns `$0.00`.

- **`contact(phone)`**:
  - **Purpose**: Formats a phone number into a readable format (e.g., `(123) 456-7890`).
  - **Logic**: Takes a phone number string and formats it using parentheses and a hyphen.

- **`comp_id(ident)`**:
  - **Purpose**: Formats a company ID into a standardized format.
  - **Logic**:
    - If the ID length is greater than 11, it uses one format.
    - Otherwise, it uses another format.

- **`get_age(now, birthdate)`**:
  - **Purpose**: Calculates the age in years given the current date and a birthdate.
  - **Logic**: Uses `relativedelta` to compute the difference in years between the two dates.

- **`string_format(string)`**:
  - **Purpose**: Capitalizes the first letter of a string and trims any leading or trailing whitespace.
  - **Logic**: Strips whitespace and applies the `capitalize()` method to the string.