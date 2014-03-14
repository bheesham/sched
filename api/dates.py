#!/usr/bin/env python3
import json, random
import pymysql
from bottle import route, request, static_file, run

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='thisisatest', db='sched')
cur = conn.cursor()
cur.execute('SELECT name, email, date, hour FROM appointments ORDER BY date ASC, hour ASC;')

print('Name\t\tEmail\t\tDate\tHour')

for row in cur:
  print(row[0], '\t', row[1], '\t', row[2], row[3], sep='\t')
    
cur.close()
conn.close()
