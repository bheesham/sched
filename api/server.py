import json, random
import pymysql
from bottle import route, request, static_file, run

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='thisisatest', db='sched')

@route('/api/<path:path>', method='POST')
def api(path='invalid'):
  cur = conn.cursor()
  if path == 'get-date-hours':
    hours = []
    date = request.forms.get('date')
    
    # hours available
    cur.execute('SELECT hour FROM available WHERE date = %s', (date))
    for row in cur:
      hours.append(row[0])

    # hours not booked
    cur.execute('SELECT hour FROM appointments WHERE date = %s;', (date))
    for row in cur:
      if row[0] in hours:
        hours.remove(row[0])
    
    cur.close()
    conn.close()
    return json.dumps({'hours': hours})
  if path == 'save-appointment':
    date = request.forms.get('date')
    hour = request.forms.get('hour')
    ihour = int(hour)

    name = request.forms.get('name')
    email = request.forms.get('email')

    if len(name) < 1 or len(email) < 1:
      return json.dumps({'message': 'Error: need to specify a name AND an email address'})

    ret = ''
    cur.execute('SELECT hour FROM appointments WHERE date = %s AND hour = %s;', (date, ihour))
    if cur.rowcount == 0:
      cur.execute('INSERT INTO appointments (date, hour, name, email) VALUES (%s, %s, %s, %s);', (date, ihour, name, email))
      if cur.rowcount:
        conn.commit()
        ret = json.dumps({'message': 'Successfully booked the appointment.'})
      else:
        ret = json.dumps({'message': 'There has been an error. Please email bheesham@ccsl.carleton.ca'})
    else:
      ret = json.dumps({'message': 'There has been an error while trying to book that time, please select another.'})
    cur.close()
    conn.close()
    return ret
  else:
    cur.close()
    conn.close()
    return json.dumps({'error': 'invalid request'})

@route('/<path:path>')
def dist(path):
  return static_file(path, root='dist')

@route('/')
@route('/<filename>')
def index(filename='index.html'):
  return static_file(filename, root='dist')

run(host='0.0.0.0', port=80)
