from flask import Flask
''' It create an instance of the flask class which will 
be your WSGI( web Server Gateway Interrface)
'''
# this s my WSGi application
app=Flask(__name__)

@app.route('/')

def welcome():
    return 'WElcome to this flask application . This application show thwe many information'
@app.route('/index')

def index():
    return 'Welcome to my index page name'
if __name__=='__main__':
    app.run(debug=True)
