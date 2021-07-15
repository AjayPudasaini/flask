from flask import Flask, render_template, url_for, request
from flask.helpers import flash

app = Flask(__name__)


posts = [
    {
        'author':'ajay',
        'title':'blog post 1',
        'content':'first post',
    },

    {
        'author':'sanj',
        'title':'blog post 2',
        'content':'second post',
    }
]

input_data = []

@app.route('/', methods=["GET", "POST"])
def hello():
    input = request.form.get('shorturl')
    input_data.append(f"{input}")
    return render_template('index.html', data = posts, input=input_data)





if __name__ == '__main__':
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(debug=True)
