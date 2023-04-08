from application import app
from flask import render_template
from markupsafe import escape
#MVC - model view controller

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route("/<name>/<int:?id>")
def hello(name, id):
    return f"Hello, {escape(name)}! {id}"


@app.route('/')
@app.route('/index')
def index():

    posts = [
        { 
            'author' :{
                'name' : 'Max',
                'age'   : 16
            }, 
            'text' : "Eu non veniam cillum qui consectetur esse veniam.",
            'date' : '24.02.2009'

        },
        { 
            'author' :{
                'name' : 'Mike',
                'age'   : 21
            }, 
            'text' : "Officia voluptate non voluptate fugiat.",
            'date' : '01.01.1994'
        },
    ]

    return render_template('index.html', title = 'Home', posts=posts)