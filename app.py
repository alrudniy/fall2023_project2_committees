from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p3:Mtmqn584@34.136.218.122:3306/p3_courses"


# Create a SQLAlchemy instance
db = SQLAlchemy(app)


# Define a simple database model (optional)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))



@app.route('/', methods= ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/loginButtonP', methods= ['GET', 'POST'])
def loginButtonP():
    return render_template('mainP.html')


@app.route('/seeHistoryButtonP', methods= ['GET', 'POST'])
def seeHistoryButtonP():
    return render_template('seeHistoryP.html')

@app.route('/applyButtonP', methods= ['GET', 'POST'])
def applyButtonP():
    return render_template('applyP.html')


@app.route('/loginP')
def loginP():
    return render_template('loginP.html')


@app.route('/loginButtonA')
def loginButtonA():
    return render_template('loginA.html')


@app.route('/loginA')
def loginA():
    return render_template('mainA.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


if __name__ == '__main__':
    app.run(debug=True)