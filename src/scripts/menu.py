DB_MENU_TEXT =  '''What would you like to do:
    connect: connect to a table
    print: print all tables
    query: query the database
    backup: backup the database
    restore: restore the database
    exit: exit'''

TABLE_MENU_TEXT = '''Please enter your choice:
    csvadd: Add data from the CSV file
    useradd: Manually add data
    display: Display the table	
    updaterow: Update row
    deleterow: Delete row
    updatecell: Update cell
    deletecell: Delete cell
    exit: Exit and commit changes'''

class Menu():
    def __init__(self, db, csv_paths):
        self.db = db
        self.csv_paths = csv_paths

    def table_menu(self, i):
        try:
            if i == 'csvadd':
                self.table.add_from_csv(self.csv_paths[self.table.name])
            elif i == 'useradd':
                self.table.add_from_user()
            elif i == 'display':
                print(self.table)
            elif i == 'updaterow':
                self.table.update_row()
            elif i == 'deleterow':
                self.table.delete_row()
            elif i == 'updatecell':
                self.table.update_cell()
            elif i == 'deletecell':
                self.table.delete_cell()
            elif i == 'search':
                "self.table.search()"
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")

    def db_menu(self, i):
        try:
            if i == 'connect':
                print("Which table would you like to connect to: ")
                for table in self.db.tables:
                    print('    ' + table.name)
                i = input().lower()
                try:
                    self.table = self.db.table_dict[i]
                    self.table.connect_to_db()
                    self.run_table()
                except KeyError:
                    print('Invalid input')
            elif i == 'backup':
                self.db.backup()
            elif i == 'print':
                self.db.print_all_tables()
            elif i == 'restore':
                self.db.restore()
            elif i == 'query':
                self.db.execute_user_query()
            elif i == 'exit':
                quit()
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
    
    def run(self):
        self.run_db()
    
    def run_db(self):
        while(True):
            print(DB_MENU_TEXT)
            choice = input().lower()
            self.db_menu(choice)

    def run_table(self):
        while(True):
            print(TABLE_MENU_TEXT)
            i = input()
            if i=='exit':
                self.table.close()
                break
            self.table_menu(i)
