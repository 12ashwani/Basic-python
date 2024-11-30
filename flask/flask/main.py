from flask import Flask,render_template
''' It create an instance of the flask class which will 
be your WSGI( web Server Gateway Interrface)
'''
# this s my WSGi application
app=Flask(__name__)

@app.route('/')
def welcome():
    return '<html><h1>Welcome to this flask application . This application show the many information<h1><html>'
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
