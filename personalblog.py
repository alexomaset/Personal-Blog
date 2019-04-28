from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
 
app.config['SECRET_KEY'] = 'ekiomz1234'

@app.route("/")
@approute("/index")
def index():
    return render_template


@approute("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)    

@approute("/register")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)    

if __name__ = '__main__':
    app.run(debug=True)
