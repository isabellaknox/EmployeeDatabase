import sqlite3
from tabulate import tabulate

class Database():
	
	def __init__(self, tables, path, backup_path):
		self.tables = tables
		self.table_dict = {}
		for table in tables:
			self.table_dict[table.name]=table
		self.connect = self.connect_to_db(path)
		self.backup_connect = self.connect_to_db(backup_path)
		
	def connect_to_db(self, path):
		try:
			# Connect to database.
			connect = sqlite3.connect(path)
			return connect
		except sqlite3.DatabaseError as e:
			# Confirm unsuccessful connection and quit.
			print("Database connection unsuccessful.")
			quit()

	def print_all_tables(self):
		for table in self.tables:
			table.connect_to_db()
			print(table.name)
			print(table)
			table.close()

	def execute_user_query(self):
		query = input("Please enter your SQL Query: ")
		cursor = self.connect.cursor()
		try:
			print(tabulate(cursor.execute(query)))
		except sqlite3.DatabaseError as e:
			print("Error adding information.")
		
	def backup(self):
		dump = 'dump.sql'
		
		with open(dump, 'w') as f:
			for line in self.connect.iterdump():
				f.write('%s\n' % line)	
				
		with open(dump, 'r') as f:
			sql_script = f.read()
			
		cu = self.backup_connect.cursor()
		for table in self.tables:
			try:
				cu.execute('DROP TABLE {}'.format(table.name))
			except sqlite3.OperationalError:
				'''Table doesnt exist'''
		cu.executescript(sql_script)

	def restore(self):
		dump = 'dump.sql'
		with open(dump, 'w') as f:
			for line in self.backup_connect.iterdump():
				f.write('%s\n' % line)
				
		with open(dump, 'r') as f:
			sql_script = f.read()
			
		cu = self.connect.cursor()
		for table in self.tables:
			try:
				cu.execute('DROP TABLE {}'.format(table.name))
			except sqlite3.OperationalError:
				'''Table doesnt exist'''
		cu.executescript(sql_script)
