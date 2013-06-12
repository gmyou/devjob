import MySQLdb
from MySQLCon import _con

#def _con():
#	return MySQLdb.connect(host='localhost', db='opentutorials',  user='root', passwd='unicad10')

m = _con()
c = m.cursor()
c.execute("select * from topic")
print c.fetchall()
