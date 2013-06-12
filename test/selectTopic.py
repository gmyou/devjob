# selectTopic.py
# Use external module 'MySQLCon' located at '/usr/lib64/python2.6'

import MySQLdb
from MySQLCon import _con


m = _con()
c = m.cursor()
c.execute("select * from topic")
print c.fetchall()
