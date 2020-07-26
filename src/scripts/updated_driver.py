from basic_table import BasicTable
from database import Database
from menu import Menu
import sqlite3
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("../data")

addresses_file_path = os.getcwd() + '//addresses.csv'
associates_file_path =  os.getcwd() + '//associates.csv'
fun_facts_file_path =  os.getcwd() + '//fun_facts.csv'
events_file_path =  os.getcwd() + '//events.csv'
associates_events_file_path = os.getcwd() + '//associates_events.csv'

csv_paths = {'addresses': addresses_file_path,
			'associates': associates_file_path,
			'fun_facts': fun_facts_file_path,
			'events': events_file_path,
			'associates_events': associates_events_file_path}

os.chdir("../databases")
db_file_path = os.getcwd() + '//team_info_test.db'
os.chdir("../backups")
backup_file_path = os.getcwd() + '//team_info_backup.db'
	
associate_fields = [['badge_id', 'TEXT NOT NULL PRIMARY KEY'],
			['first_name', 'TEXT'],
			['last_name', 'TEXT'],
			['hire_date', 'TEXT']]
fun_fact_fields = [['fact_id', 'INTEGER PRIMARY KEY'],
			['title', 'TEXT'],
			['description', 'TEXT'],
			['badge_id', 'TEXT NOT NULL']]
address_fields = [['address_id', 'INTEGER PRIMARY KEY'],
			['street_address', 'TEXT'],
			['city', 'TEXT'],
			['state', 'TEXT'],
			['zip_code', 'TEXT'],
			['badge_id', 'TEXT NOT NULL']]
event_fields = [['event_id', 'INTEGER PRIMARY KEY'],
			['title', 'TEXT'],
			['description', 'TEXT'],
			['date', 'DATE'],	
			['time', 'TEXT']]
associates_events_fields = [['event_id','INTEGER NOT NULL'],
			['badge_id', 'TEXT NOT NULL']]

def main():
	associates = BasicTable('associates', db_file_path, associate_fields)
	fun_facts = BasicTable('fun_facts', db_file_path, fun_fact_fields)
	addresses = BasicTable('addresses', db_file_path, address_fields)
	events = BasicTable('events', db_file_path, event_fields)
	associates_events = BasicTable('associates_events', db_file_path, associates_events_fields)
	tables = [associates, fun_facts, addresses, events, associates_events]

	database = Database(tables, db_file_path, backup_file_path)

	print('SQLite Version {}'.format(sqlite3.version))
	
	m = Menu(database, csv_paths)
	m.run()
					
if __name__ == '__main__':
	main()
