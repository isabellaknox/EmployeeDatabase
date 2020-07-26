import sqlite3

def restore(db, bck, table_name):
	dump = 'dump.sql'

	with open(dump, 'w') as f:
		for line in bck.iterdump():
			f.write('%s\n' % line)
			
	with open(dump, 'r') as f:
		sql_script = f.read()
		
	cu = db.cursor()
	try:
		cu.execute('DROP TABLE {}'.format(table_name))
	except sqlite3.OperationalError:
		'''Table doesnt exist'''
	cu.executescript(sql_script)
	
