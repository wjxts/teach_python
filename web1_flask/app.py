from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the home page!'

from flask import render_template

@app.route('/dynamic/<name>')
def dynamic_page(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)