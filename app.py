from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

'''
    Main script for the web app.
'''
#* Instance from class Flask for the app:  Allow us to use methods from the library
app = Flask(__name__)
#* Configuration for the database access: Using MySQL Root user (mysql://user:password@server_name/database)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#* Calls the SQL method with the app as parameter to run the connection to database
SQLAlchemy(app)
#* Calls the blueprint to run the HTML site
app.register_blueprint(contacts)


