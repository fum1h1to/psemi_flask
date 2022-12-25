from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///sample.db"
db=SQLAlchemy(app)

class user_db(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

@app.route("/")
def index():
    users = user_db.query.all()
    
    return render_template('index3.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    password = request.form['password']

    new_item = user_db(name=name, password=str(hashlib.sha256(password.encode()).hexdigest()))
    db.session.add(new_item)
    db.session.commit()

    return redirect('/')

@app.route('/remove/<id>', methods=['GET'])
def remove(id):
    exists = user_db.query.filter_by(id=id).first()
    db.session.delete(exists)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    # with app.app_context():
        # db.create_all()
    app.run(port=8080, debug=True)