from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def front():
    dictionary = {'name': 'Emir', 'age': 24, 'country': 'Argentina'}
    return render_template("front.html", name=dictionary)

@app.route("/color")
def list1():
    colors_list = ["Green", "Yellow", "Blue", "Brown"]
    return render_template("colors.html", colors=colors_list)

@app.route("/route/<text>")
def sentence(text):
    return render_template("sentence.html", text1=text)

if __name__ == '__main__':
    app.run(debug=True)
