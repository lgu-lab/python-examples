from bottle import Bottle
from hello import hello

app = Bottle()

@app.route('/')
def rootIndex():
    return 'Application Suite Home Page'

if __name__ == '__main__':
    app.merge(hello)
    app.run(port=1234, debug=True)