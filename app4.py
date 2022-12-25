from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index4.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']

    isLogin = False
    if name == "admin" and password == "password":
        isLogin = True

    context = {
        "isLogin": isLogin,
    }

    return render_template('login.html', context=context)



if __name__ == "__main__":
    app.run(port=8080, debug=True)