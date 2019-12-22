from flask import Flask
app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'Response from my local computer'


if __name__ == '__main__':
    app.run(port='8080')
