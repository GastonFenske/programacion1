from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField, validators, BooleanField 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

class BolsonForm(FlaskForm):

    bolson_name = StringField('Nombre del bolson', validators=[validators.InputRequired()])
    bolson_des = StringField('Descripcion del bolson', validators=[validators.InputRequired()])
    bolson_venta = BooleanField('Listo para la venta')

@app.route('/', methods=['GET', 'POST'])
def form():
    form = BolsonForm()
    if form.validate_on_submit():
        print('Hola')
    return render_template('agregarbolson.html', form = form)

if __name__ == '__main__':
    app.run(debug=True, port=6500)
