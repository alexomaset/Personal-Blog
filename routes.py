from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
 
app.config['SECRET_KEY'] = 'ekiomz1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
@approute("/index")
def index():
    return render_template


@approute("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if from.validate_on_submit():
        flash(f'Account created for (form.username.data)!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='register', form=form)    

@approute("/register")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)    

if __name__ == '__main__':
    app.run(debug=True)
