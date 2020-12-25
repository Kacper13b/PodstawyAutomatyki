from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Home Page!'


if __name__ == '__main__':
    app.run(debug=True)
