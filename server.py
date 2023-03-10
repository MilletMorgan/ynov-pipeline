from bottle import route, run, template
from misc import add


@route('/')
def homepage():
    return 'Hello you !'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/add/<a>/<b>')
def route_add(a, b):
    return {'result': add(a, b)}


run(host='localhost', port=8080, reloader=True)
