from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///sample.db"
db=SQLAlchemy(app)

class user_db(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

# @app.route("/")
# def index():

#     context = {
#         'nums': list(range(9+1)),
#         'likeDict': {
#             '好きな色' : '青',
#             '好きなOS' : 'Linux',
#             '好きな言語' : 'Python',
#         },
#         'flag' : True
#     }
#     return render_template('index.html', context=context)

# @app.route('/routing')
# def routing():
#     return render_template('routing.html')

# @app.route('/get', methods=['GET'])
# def send_get():
#     text = request.args.get('text')
#     print(text)
#     return render_template('get.html', receive_data=text)


if __name__ == "__main__":
    db.create_all()
    # app.run(port=8080, debug=True)