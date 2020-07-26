from basic_table import BasicTable
from database import Database
import sqlite3

csv_file_path = 'C:\\Users\\a665707\\Documents\\Python\\Projects\\db_challenge\\data\\cds_info_simple.csv'
db_file_path = 'C:\\Users\\a665707\\Documents\\Python\\Projects\\db_challenge\\Databases\\team_info_test.db'
backup_file_path = 'C:\\Users\\a665707\\Documents\\Python\\Projects\\db_challenge\\Backups\\team_info_backup.db'

menu_text = '''Please enter your choice (0-9):
	1. Add data from the CSV file
	2. Manually add data
	3. Display the table
	4. Backup database
	5. Restore database from backup
	6. Update row
	7. Delete row
	8. Update cell
	9. Delete cell
	0. Exit and commit changes'''
fields = [['first_name', 'TEXT'],
			['last_name', 'TEXT'],
			['badge_id', 'TEXT NOT NULL PRIMARY KEY'],
			['title', 'TEXT'],
			['office_address', 'TEXT'],
			['fun_fact', 'TEXT']]

def menu(i, table, db):
	try:
		if int(i) == 1:
			table.add_from_csv(csv_file_path)
		elif int(i) == 2:
			table.add_from_user()
		elif int(i) == 3:
			print(table)
		elif int(i) == 4:
			db.backup()
		elif int(i) == 5:
			db.restore()
		elif int(i) == 6:
			table.update_row()
		elif int(i) == 7:
			table.delete_row()
		elif int(i) == 8:
			table.update_cell()
		elif int(i) == 9:
			table.delete_cell()
		elif int(i) == 0:
			table.close()
			quit()
	except ValueError:
		print("Invalid Input")

def main():
	table1 = BasicTable('members', db_file_path, fields)
	table2 = BasicTable('other_members', db_file_path, fields)
	database = Database([table1, table2], db_file_path, backup_file_path)

	print('SQLite Version {}'.format(sqlite3.version))
	while(True):
		print(menu_text)
		i = input()
		menu(i, table1, database)
					
if __name__ == '__main__':
	main()
