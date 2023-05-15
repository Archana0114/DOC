from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'   # specify the URI for the database
db = SQLAlchemy(app)    # instantiate the SQLAlchemy object with the app object

# Define the Customer and Order models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)   # define the id field as an Integer primary key
    name = db.Column(db.String(50))  

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))  # define the customer_id field as a foreign key that references the id field in the Customer model
    product = db.Column(db.String(50))  

# Create the database tables
db.create_all()
