'''
# First setup Environment - 
    py -m venv envName     
    envName\Scripts\activate
    pip install flask
'''
from flask import Flask

# To run app - flask run
app = Flask(__name__)

@app.route('/')
def myFunc1():
    return '<h1>Hello World<h1>'
'''
Hello World
'''

# @app.route('/') - redirects to the webpage as mentioned
@app.route('/<name>')
def myFunc2(name):
    return '<h1>Hello World!!. Hi {}<h1>'.format(name)

'''
Hello World!!. Hi Ayush
'''