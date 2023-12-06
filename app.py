#this is for database connection 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
# from app import app, db, faculty

app = Flask(__name__)


# Configure the SQLAlchemy database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p2:Rhrew281@34.136.218.122:3306/p2_committee"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance
# db = SQLAlchemy(app)

# db=mysql.connector.connect(
#     host='localhost',
#     user='p2',
#     password='Rhrew281',
#     database='p2_committee'
# )

# Define a simple database model (optional)
# class faculty(db.Model):
#     facultyID = db.Column(db.Integer, primary_key=True)
#     FirstName = db.Column(db.String(50))
#     LastName = db.Column(db.String(50))
#     Department = db.Column(db.String(50))
#     DepartmentPosition = db.Column(db.String(50))

@app.route('/', methods= ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/seeHistoryButtonP', methods= ['GET', 'POST'])
def seeHistoryButtonP():
    return render_template('seeHistoryP.html')

@app.route('/seeHistoryButtonA', methods= ['GET', 'POST'])
def seeHistoryButtonA():
    return render_template('seeHistoryA.html')

@app.route('/loginButtonP', methods= ['GET', 'POST'])
def loginButtonP():
    return render_template('homeP.html')

# @app.route('/loginP')
# def loginP():
#     return render_template('loginP.html')

@app.route('/loginButtonA', methods= ['GET', 'POST'])
def loginButtonA():
    return render_template('homeA.html')

# @app.route('/loginA')
# def loginA():
#     return render_template('loginA.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/homeButtonA', methods= ['GET', 'POST'])
def homeButtonA():
    return render_template('homeA.html')

@app.route('/homeButtonP', methods= ['GET', 'POST'])
def homeButtonP():
    return render_template('homeP.html')

@app.route('/', methods= ['GET', 'POST'])
def logoutButton():
    return render_template('home.html')

@app.route('/applyButtonA', methods= ['GET', 'POST'])
def applyButtonA():
    return render_template('applyA.html')

@app.route('/applyButtonP', methods= ['GET', 'POST'])
def applyButtonP():
    return render_template('applyP.html')   

@app.route('/settingsButtonA', methods= ['GET', 'POST'])
def settingsButtonA():
    return render_template('settingsA.html')

@app.route('/settingsButtonP', methods= ['GET', 'POST'])
def settingsButtonP():
    return render_template('settingsP.html')

#DB CONNECT
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)