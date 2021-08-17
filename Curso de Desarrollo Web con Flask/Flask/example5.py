from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretPasword'
class Form(FlaskForm):
    name = StringField('NAME', validators=[DataRequired()])
    age = BooleanField('You are of age?')
    sex = RadioField('What is your sex?:', choices=[('male', 'male'), ('female', 'female')])
    color = SelectField('Favorite Color: ', choices=[('b', 'blue'), ('r', 'red'), ('y', 'yellow')])
    comment = TextAreaField()
    button = SubmitField()

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/data", methods=['GET', 'POST'])
def data():
    myForm = Form()
    if myForm.validate_on_submit():
        session['name'] = myForm.name.data
        session['age'] = myForm.age.data
        session['sex'] = myForm.sex.data
        session['color'] = myForm.color.data
        session['comment'] = myForm.comment.data
        return redirect(url_for('information'))

    return render_template('data.html', form=myForm)

if __name__ == '__main__':
    app.run(debug=True)
