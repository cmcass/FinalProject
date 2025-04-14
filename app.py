from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'

@app.route('/two')
def hello():
    return 'Hello, page 2!'

if __name__ == '__main__':
    app.run(debug=True)

