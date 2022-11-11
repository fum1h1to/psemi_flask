from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index2.html')

@app.route('/routing')
def routing():
    return render_template('routing.html')

@app.route('/get', methods=['GET'])
def receive_get():
    text = request.args.get('text')
    print(text)
    return render_template('get.html', receive_data=text)

@app.route('/post', methods=['POST'])
def receive_post():
    text = request.form.get('text')
    return render_template('post.html', receive_data=text)

if __name__ == "__main__":
    app.run(port=8080, debug=True)