import json, random
import pg8000
from bottle import route, static_file, run

@route('/api/<path:path>', method='POST')
def api(path='invalid'):
  if path == 'get-avail-hours':
    hours = []
    for i in range(4):
      hours.append(random.randint(8,16))
    return json.dumps({'hours': hours})
  elif path == 'save-appointment':
    return json.dumps({'message': 'not implemented'})
  else:
    return json.dumps({'error': 'invalid request'})

@route('/<path:path>')
def dist(path):
  return static_file(path, root='dist')

@route('/')
@route('/<filename>')
def index(filename='index.html'):
  return static_file(filename, root='dist')

run(host='localhost', port=80)
