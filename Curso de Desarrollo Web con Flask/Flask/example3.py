from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/page1")
def part1():
    return render_template("page1.html")

@app.route("/page2")
def part2():
    return render_template("page2.html")

@app.route("/form")
def form1():
    return render_template("form.html")

@app.route("/greeting")
def greeting():
    value1 = request.args.get('name')
    value2 = request.args.get('lastname')
    return render_template("greeting.html", name=value1, lastname=value2)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('page404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
