from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretPassword'

class Form(FlaskForm):
    button = SubmitField('Send message: ')

@app.route("/message", methods=['GET', 'POST'])
def message():
    form = Form()
    if form.validate_on_submit():
        flash('Thanks for clicking the button!!')
        return redirect(url_for('message'))
    return render_template('message.html',form1=form)

if __name__ == '__main__':
    app.run(debug=True)
