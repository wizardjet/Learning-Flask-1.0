from flask import Flask, render_template, url_for
app = Flask(__name__)

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