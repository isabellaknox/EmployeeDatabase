import sqlite3

def backup(db, bck, table_name):
	dump = 'dump.sql'

	with open(dump, 'w') as f:
		for line in db.iterdump():
			f.write('%s\n' % line)
			
	with open(dump, 'r') as f:
		sql_script = f.read()
		
	cu = bck.cursor()
	try:
		cu.execute('DROP TABLE {}'.format(table_name))
	except sqlite3.OperationalError:
		'''Table doesnt exist'''
	cu.executescript(sql_script)
	
