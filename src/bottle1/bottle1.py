from bottle import route, run

@route('/')
def welcome():
    return "Welcome."

@route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def helloNameInURI(name):
    return "Hello " + name

@route('/add/<a:int>/<b:int>')  # with conversion 
def add(a,b):
    r = a + b
    return "Add " + str(a) + " + " + str(b) + " = " + str(r) 

run(host='localhost', port=8080, debug=True)