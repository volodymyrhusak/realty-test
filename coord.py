import MySQLdb



def get_poligon_oblast():
	db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
	dbCursor=db.cursor()
	dbCursor.execute('''SELECT geojson FROM poligons WHERE idpoligons=39''')
	poligons=dbCursor.fetchone()
	print type(poligons)
	return poligons



def get_poligon_reg():
	db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
	dbCursor=db.cursor()
	dbCursor.execute('''SELECT geojson FROM poligons WHERE idpoligons=41''')
	poligons=dbCursor.fetchone()
	print type(poligons)
	return poligons

def get_object():
	db=MySQLdb.connect(host='localhost', user='root',passwd='123',db='orendatest')
	dbCursor=db.cursor()
	dbCursor.execute('''SELECT descr,coord FROM orendaPodobovo WHERE idorendaPodobovo <21 ''')
	data=dbCursor.fetchall()
	return data