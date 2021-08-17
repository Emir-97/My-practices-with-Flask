from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretPassword'

class Form(FlaskForm):
    name = StringField('name')
    submit = SubmitField('submit')

@app.route("/", methods=['GET', 'POST'])
def principal():
    name1 = ''
    sent = False
    form = Form()

    if form.validate_on_submit():
        name1 = form.name.data
        sent = True
        form.name.data = ''

    return render_template('index.html', name=name1, sent1=sent, form=form)

if __name__  == '__main__':
    app.run(debug=True)
