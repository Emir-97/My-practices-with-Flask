from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello Word, Good Morning</h1>"

@app.route("/bye")
def bye():
    return "<h2>Goodbye see you later</h2>"

@app.route("/greet/<name>")
def greet(name):
    return "<h2>Hello {}, how are you?".format(name)

@app.route("/length/<name>")
def length(name):
    value = len(name)
    return "<h2>The {} has {} letters</h2>".format(name, value)

@app.route("/length/<name>/<age>")
def data(name, age):
    value = len(name)
    return "<h2>The name {} has {} letters and your age is {}</h2>".format(name, value, age)

@app.route("/sum/<num1>/<num2>")
def sum(num1, num2):
    sum1 = int(num1) + int(num2)
    result = str(sum1)
    return "<h2>The sum between {} and {} are {}</h2>".format(num1, num2, result)

if __name__ == '__main__':
    app.run()
