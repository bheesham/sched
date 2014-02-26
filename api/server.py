import json, random
import pymysql
from bottle import route, request, static_file, run

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='thisisatest', db='sched')

@route('/api/<path:path>', method='POST')
def api(path='invalid'):
  cur = conn.cursor()
  if path == 'get-date-hours':
    hours = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    date = request.forms.get('date')
    cur.execute('SELECT hour FROM appointments WHERE date = %s;', (date))
    for row in cur:
      hours.remove(row[0])
    cur.close()
    return json.dumps({'hours': hours})
  if path == 'save-appointment':
    date = request.forms.get('date')
    hour = request.forms.get('hour')
    ihour = int(hour)

    name = request.forms.get('name')
    email = request.forms.get('email')

    if len(name) < 1 or len(email) < 1:
      return json.dumps({'message': 'Need to specify a name AND an email address'})

    ret = ''
    cur.execute('SELECT hour FROM appointments WHERE date = %s AND hour = %s;', (date, ihour))
    if cur.rowcount == 0:
      cur.execute('INSERT INTO appointments (date, hour, name, email) VALUES (%s, %s, %s, %s);', (date, ihour, name, email))
      if cur.rowcount:
        conn.commit()
        ret = json.dumps({'message': 'Appointment has been booked'})
      else:
        ret = json.dumps({'message': 'There has been an error. Please email bheesham@ccsl.carleton.ca'})
    else:
      ret = json.dumps({'message': 'There has been an error while trying to book that time, please select another.'})
    cur.close()
    return ret
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
