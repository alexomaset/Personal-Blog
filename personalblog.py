from flask import Flask, render_template,url_for
app = Flask(__name__)
 
app.config['SECRET_KEY'] = 'ekiomz1234'

@app.route("/")
@approute("/index")
def index():
    return render_template

if __name__ = '__main__':
    app.run(debug=True)
