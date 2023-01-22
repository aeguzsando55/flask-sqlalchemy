from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact  #! Imports model Contact
from utils.db import db  #! Imports db util

contacts = Blueprint("contacts", __name__)  # * Establishes the Router


@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


#** In the first use, this creates the table named 'contact'
@contacts.route("/new", methods=["POST"])  # * Uses POST method instead GET
def add_contact():
    # * Input parameters (Uses the parameter 'name' from the form of html template 'index.html')
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    # * New object contact instance
    new_contact = Contact(fullname=fullname, email=email, phone=phone)
    # * Saves the new object as a row in the table 'contacts'
    db.session.add(new_contact)  # * Opens a connection given the insert method and the object (INSERT INTO)
    db.session.commit()  # * Commits changes and closes connection
    
    flash("contact added successfully")
    
    return redirect(url_for("contacts.index"))  # * Redirects to home

#* The route takes an additional parameter referencing the id from an object contact.
@contacts.route("/update/<id>", methods=["POST", "GET"])  # * Uses POST and GET methods
def update(id):
    # * Consults the table given the id
    contact = Contact.query.get(id)
    # * Performs the update given the query method  
    if request.method == "POST":
        # * Request the form and gives new values
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        # * Here ns only necessary to commit changes
        db.session.commit()
        flash("Contact updated successfully")
        # * Redirects to index
        return redirect(url_for("contacts.index"))
    # * If method != "POST" 
    return render_template("update.html", contact=contact)

# * The route takes an additional parameter referencing the id from an object contact.
@contacts.route("/delete/<id>")  
# * In the function this input will be the given value referencing the id column.
# * To instance the object, uses a inherited method of the db class:
def delete(id):  
    # * Consults the table given the id
    contact = Contact.query.get(id)  
    # * Performs delete action given the object(DELETE FROM 'table' WHERE 'id' == '')
    db.session.delete(contact)  
    # * Commits changes and closes connection
    db.session.commit()  
    flash("Contact deleted successfully")
     # * Redirects to home
    return redirect(url_for("contacts.index")) 

@contacts.route("/about")
def about():
    return render_template("about.html")
