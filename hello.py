from flask import 

Flaskapp = Flask(__name__)
@app.route('/')

def index():    
    return '<h1>Hello World!</h1>'