from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p3:Mtmqn584@34.136.218.122:3306/p3_courses"

# Create a SQLAlchemy instance
db = SQLAlchemy(app)

# Define a simple database model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50)

# Create the database tables
db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Example: Create a new course
        course_name = request.form['course_name']
        new_course = Course(name=course_name)
        db.session.add(new_course)
        db.session.commit()

    courses = Course.query.all()
    return render_template('home.html', courses=courses)

@app.route('/seeHistoryButtonP', methods=['GET', 'POST'])
def seeHistoryButtonP():
    # Read data from the database
    courses = Course.query.all()
    return render_template('seeHistoryP.html', courses=courses)

@app.route('/seeHistoryButtonA', methods=['GET', 'POST'])
def seeHistoryButtonA():
    # Read data from the database
    courses = Course.query.all()
    return render_template('seeHistoryA.html', courses=courses)

@app.route('/delete_course/<int:course_id>', methods=['GET'])
def delete_course(course_id):
    # Example: Delete a course
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('seeHistoryButtonP'))

if __name__ == '__main__':
    app.run(debug=True)