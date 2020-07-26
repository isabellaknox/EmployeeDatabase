import sqlite3
import modules.validate as validate

def connect_to_db(name):
	try:
		# Connect to database.
		connect = sqlite3.connect(name)
		return connect
	except sqlite3.DatabaseError as e:
		# Confirm unsuccessful connection and quit.
		print("Database connection unsuccessful.")
		quit()
		

def	add_from_user(db, fields):
	cursor = db.cursor()
	vals = input("Please enter your data formatted as: 'first_name, last_name, badge_id, title, office_address, fun_fact'\n").strip().split(',')
	vals = [val.strip() for val in vals]
	query = "INSERT INTO members (first_name, last_name, badge_id, title, office_address, fun_fact) Values (?, ?, ?, ?, ?, ?)"
	try:
		print(vals)
		if validate.is_valid_all(vals):
			cursor.execute(query, (*vals,))
		else:
			print("Invalid Input")
	except IndexError:
		print("Invalid Input")
	except sqlite3.DatabaseError as e :
		print("Error adding information.")
		quit()
		
def update_cell(db, delete = False):
	cursor = db.cursor()
	id = input("Please enter the badge_id of the cell: ")
	if validate.is_valid_badge_id(id):
		field = input("Please enter the field of the cell: ")
		if delete:
			if field == 'badge_id':
				print("Cannot delete badge_id (Primary Key)")
				return
			query = "UPDATE members SET {} = null WHERE badge_id=?".format(field)
			try:
				cursor.execute(query, (id,)) 
			except sqlite3.DatabaseError as e :
				print("Error adding information.")
				quit()	
		else:
			val = input("Please enter the updated value: ") 
			if field == 'first_name' or field == 'last_name':
				if not validate.is_valid_name(val):
					print("Invalid Input")
					return
			if field == 'badge_id':
				if not validate.is_valid_badge_id(val):
					print("Invalid Input")
					return
			query = "UPDATE members SET {} = ? WHERE badge_id=?".format(field)
			try:
				cursor.execute(query, (val, id)) 
			except sqlite3.DatabaseError as e :
				print("Error adding information.")
				quit()
	else:
		print("Invalid badge_id")
	
def update_row(db):
	id = input("Please enter the badge_id of the row you would like to update: ")
	if validate.is_valid_badge_id(id):
		update = input("Please enter the new data for that row formatted as: 'first_name, last_name, badge_id, title, office_address, fun_fact'\n").strip().split(',')
		update = [x.strip() for x in update]
		cursor = db.cursor()
		query = "UPDATE members SET first_name=?, last_name=?, badge_id=?, title=?, office_address=?, fun_fact=? WHERE badge_id=?"
		try:
			if validate.is_valid_all(update):
				cursor.execute(query, (*update, id))
			else:
				print("Invalid Input")
		except IndexError:
			print("Invalid Input")
		except sqlite3.DatabaseError as e :
			print("Error adding information.")
			quit()
	else:
		print("Invalid badge_id")

def delete_row(db):
	id = input("Please enter the badge_id of the row you would like to delete: ")
	if validate.is_valid_badge_id(id):
		cursor = db.cursor()
		query = "DELETE FROM members WHERE badge_id=?"
		cursor.execute(query, (id, ))
	else:
		print("Invalid badge_id")
	
	
