from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    return f"{convert_celsius_to_fahrenheit(float(celsius)):.2f}"


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
