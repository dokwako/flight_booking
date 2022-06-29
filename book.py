#flask, python micro frame work, (django)
#import flask, Flask, request, render_templete
#from flask import

#Ruoting- binding a url to a function
#render_templete


#import
from flask import *


#bind the name to the applicatiom
app = Flask(__name__)
@app.route('/welcome')
def welcome():
    return 'Welcome to my application'

@app.route('/home')
def home():
    return 'welcome to my homepage'

@app.route('/book')
def book():
    return render_template('book.html')

#run the flask application
app.run(debug=True)