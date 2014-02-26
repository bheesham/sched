import json, random
import pymysql
from bottle import route, request, static_file, run

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='thisisatest', db='sched')
cur = conn.cursor()

@route('/api/<path:path>', method='POST')
def api(path='invalid'):
  if path == 'get-avail-hours':
    hours = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    date = request.forms.get('date')
    cur.execute('SELECT hour FROM appointments WHERE date = %s;', date)
    for row in cur:
      hours.remove(row)
    return json.dumps({'hours': hours})
  if path == 'save-appointment':
    date = request.forms.get('date')
    hour = int(request.forms.get('hour'))
    cur.execute('SELECT hour FROM appointments WHERE date = %s AND hour = %d', (date, hour))
    if cur.rowcount == 0:
      cur.execute('INSERT INTO appointments (date, hour) VALUES (%s, %d);', date, hour)
      return json.dumps({'message': 'Appointment has been booked'})
    return json.dumps({'message': 'There has been an error while trying to book that time, please select another.'})
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

run(host='0.0.0.0', port=80)
