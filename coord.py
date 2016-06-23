import MySQLdb



def get_poligon_oblast():
	try:
		db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
		dbCursor=db.cursor()
		dbCursor.execute('''SELECT geojson FROM poligons WHERE idpoligons=39''')
		poligons=dbCursor.fetchone()
		print type(poligons)
		return poligons
	
	except Exception:
		print "MySQLdb error"



def get_poligon_reg():
	try:
		db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
		dbCursor=db.cursor()
		dbCursor.execute('''SELECT geojson FROM poligons WHERE idpoligons=41''')
		poligons=dbCursor.fetchone()
		print type(poligons)
		return poligons
	except Exception:
		print "MySQLdb error"

def get_object():
	try:
		db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
		dbCursor=db.cursor()
		dbCursor.execute('''SELECT descr,coord FROM orendaPodobovo WHERE idorendaPodobovo <21 ''')
		data=dbCursor.fetchall()
		return data
	except Exception:
		print "MySQLdb error"