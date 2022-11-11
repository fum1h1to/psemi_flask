from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():

    context = {
        'nums': list(range(9+1)),
        'likeDict': {
            '好きな色' : '青',
            '好きなOS' : 'Linux',
            '好きな言語' : 'Python',
        },
        'flag' : True
    }
    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(port=8080, debug=True)