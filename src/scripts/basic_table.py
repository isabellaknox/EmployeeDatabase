import sqlite3
import csv
from tabulate import tabulate

class BasicTable():

	def __init__(self, name, path, fields):
		self.name = name
		self.fields = fields
		self.path = path
		self.primary_key = None
		self.auto_increment = False
		for field in fields:
			if field[1] == 'INTEGER PRIMARY KEY':
				self.auto_increment = True
			if field[1].find("PRIMARY KEY")!=-1:
				self.primary_key = field[0]

	def connect_to_db(self):
		try:
			# Connect to database.
			self.connect = sqlite3.connect(self.path)
			self.create_table()
		except sqlite3.DatabaseError as e:
			# Confirm unsuccessful connection and quit.
			print("Database connection unsuccessful.")
			quit()

	def create_table(self):
		cursor = self.connect.cursor()
		create_table_query = 'CREATE TABLE IF NOT EXISTS {}('.format(self.name)
		for field in self.fields:	
			create_table_query += '{} {},'.format(field[0], field[1])
		create_table_query = create_table_query.strip(',') + ');'
		try:		
			cursor.execute(create_table_query)
		except sqlite3.OperationalError:
			print("Table Already Exists")
		
	
	def get_input(self):
		vals = {}
		for field in self.fields:
			data = input("Enter {}: ".format(field[0]))
			vals[field[0]] = data
		return vals
	
	def add_from_csv(self, csv_file_path):
		reader = csv.DictReader(open(csv_file_path))
		for row in reader:
			query, vals = self.build_add_query(row)
			if query is not None:
				self.execute_query(query, vals)
				
	def add_from_user(self):
		data = self.get_input()
		query, vals = self.build_add_query(data)
		if query is not None:
			self.execute_query(query, vals)
			
	def update_row(self):
		id = input("Please enter the {} of the row you would like to update: ".format(self.primary_key))
		data = self.get_input()
		query ="UPDATE {} SET ".format(self.name)
		vals = []
		for field in self.fields:
			query +="{}=?,".format(field[0])
			try:
				vals.append(data[field[0]])
			except KeyError:
				if field[0] == self.primary_key:
					print("Input had no Primary Key")
					return None, None
				vals.append('null')
		vals.append(id)
		query = query.strip(',') + " WHERE {}=?".format(self.primary_key)
		self.execute_query(query, vals)
	
	def delete_row(self):
		id = input("Please enter the {} of the row you would like to delete: ".format(self.primary_key))
		cursor = self.connect.cursor()
		query = "DELETE FROM {} WHERE {}=?".format(self.name, self.primary_key)
		self.execute_query(query, [id])
		
	def update_cell(self):
		id = input("Please enter the {} of the cell you would like to update: ".format(self.primary_key))
		field = input("Please enter the field of the cell: ")
		val = input("Please enter the updated value: ")
		query = "UPDATE {} SET {} = ? WHERE {}=?".format(self.name, field, self.primary_key)
		self.execute_query(query, [val, id])
		
	def delete_cell(self):
		id = input("Please enter the {} of the cell you would like to delete: ".format(self.primary_key))
		field = input("Please enter the field of the cell: ")
		if field == self.primary_key:
			print("Cannot delete {} (Primary Key)".format(self.primary_key))
			return
		query = "UPDATE {} SET {} = null WHERE {}=?".format(self.name, field, self.primary_key)
		self.execute_query(query, [id]) 
	
	def execute_query(self, query, vals):
		cursor = self.connect.cursor()
		try:
			cursor.execute(query, (*vals,))
		except sqlite3.IntegrityError as e:
			print(e)
			print("WARNING: non-unique primary key found")
		except sqlite3.DatabaseError as e:
			print("Error adding information.")
	
	def build_add_query(self, data):
		query = "INSERT INTO {} (".format(self.name)
		query_latter = ') Values ('
		vals = []
		for field in self.fields:
			if field[0] == self.primary_key and self.auto_increment:
				pass
			else:
				query += '{},'.format(field[0])
				query_latter += '?,'
				try:
					vals.append(data[field[0]])
				except KeyError as e:
					if field[0] == self.primary_key:
						print("Input had no Primary Key")
						return None, None
					vals.append('null')
		return(query.strip(',') + query_latter.strip(',') + ')', vals)
		
	def close(self):
		self.connect.commit()
		self.connect.close()
		
	def __str__(self):
		cursor = self.connect.cursor()
		column = [field[0] for field in self.fields]
		return(tabulate(cursor.execute('Select * FROM {}'.format(self.name)), headers = column))
