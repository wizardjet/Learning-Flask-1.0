from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'jEBicN33YU6BYN7hEFdJBiPoQKF3'

persons = [
    {
        "name": "Kirsty",
        "email": "kc123",
        "course": "Computer Science",
        "membership": "Yes"
    }, {
        "name": "Josephina",
        "email": "dd22",
        "course": "Computer Science",
        "membership": "Yes"
    }, {
        "name": "Ellie",
        "email": "dwad22",
        "course": "Computer Science",
        "membership": "Yes"
    }, {
        "name": "Timothy",
        "email": "hh55",
        "course": "Computer Science",
        "membership": "Yes"
    }, {
        "name": "Sabrina",
        "email": "jj8",
        "course": "Computer Science",
        "membership": "Yes"
    }
]

@app.route('/')
def hello_world():
    return render_template("home.html", title='Home')

@app.route('/people')
def about():
    return render_template("people.html", persons=persons, title='People')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Registration', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title='Log In', form=form)