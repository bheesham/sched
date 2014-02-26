import KSdb
import json, random
import bottle

@app.route('/api/<path:path>', method='POST')
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

@app.route('/<path:path>')
def dist(path):
  return static_file(path, root='dist')

@app.route('/')
@app.route('/<filename>')
def index(filename='index.html'):
  return static_file(filename, root='dist')

app.run(host='localhost', port=80)