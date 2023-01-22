from app import app
from utils.db import db
import config 

"""
    Runner script: Allows the starting of the web app
"""
# * Initializes the app database
db.init_app(app)
# * Creates or establishes the elements of the database
with app.app_context():
    db.create_all()
#* Runs the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
