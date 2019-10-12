from flask import Flask, render_template
app = Flask(__name__)

persons = [
    {
        "name": "Kirsty",
        "age": "15"
    }, {
        "name": "Josephina",
        "age": "21"
    }, {
        "name": "Ellie",
        "age": "18"
    }, {
        "name": "Timothy",
        "age": "3"
    }, {
        "name": "Sabrina",
        "age": "21"
    }
]

@app.route('/')
def hello_world():
    return render_template("home.html", title='Home')

@app.route('/people')
def about():
    return render_template("people.html", persons=persons, title='People')