from utils.db import db
'''
    Allows the creation of the table model corresponding to the contacts
'''
class Contact(db.Model):
    #* Table columns
    id = db.Column(db.Integer, primary_key=True) #* Primary key, auto incremental in db.
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    #TODO: Object 'contact' initializer (is not necessary the 'id' attribute)
    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone