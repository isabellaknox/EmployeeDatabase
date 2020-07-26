# EmployeeDatabase
SQLite Database which uses Third Form Data model to import, insert, query, delete, backup, and restore employee data


Basic Building Steps:
Create and excel spreadsheet (or CSV file) of all the associates that work for the CDS team and include the following columns:
First name, Last name, Badge Id, Title, Office Address, and Fun Fact.
	Create a new (or alter your existing) Python SQLite database with the new fields. 
  Create a Python program to insert the database from the Excel (or CSV file) source.
	Query and display this new data (nicely formatted) from the database.
Write a new Python module to nicely insert new data into the table from direct user input.
In the end, in today's challenge your Python program can handle new insert sources from either a data file or from direct user input.
Write a new Python module to update and/or delete a specific column value in your table. 
Write a new Python module to update and/or delete a specific row of values in your table.
Write a Python program to create a backup of your SQLite database. Writer a Python program to restore your SQLite database 




Expand your database to be able to accommodate the following third normal form (3NF) data model with the following associations:
 Event<-->Associates
 Address<--Associate 
 Fun Fact <--> Associate

An Associate is uniquely identified their badge number. Fields in this table should include;
Badge number, First Name, Last Name, and Hire Date. An associate can be associated to 1 to many fun facts, and 1 to many 
addresses (their home address and their work address). And an associate can be associated with 1 to many events and events can be attended by 1 to many associates.

A fun fact needs a unique identifier and should contain the fields Fun Fact Title and Fun Fact Description. You can ask each of use for multiple fun facts.
	
An Address should contain a unique identifier, a street address, city, state, and zip code. Please use fake data for the
home addresses of our team members as actual data is considered personal data and you can not gather this from the  

An event should contain a unique identifier and also an event title, event description, a date, and a time. Same events can include; 
Morning Coffee, Backlog Refinement, Intern Standup, Daily Standup, and more. 


NOTE:
CSV files have had employee data changed for privacy and security reason. CSV should be filled in will correctly formatted data 
and unique badge numbers which are the same across employees in the CSV files. Issues when running may occur from badge numbers being changed in upload process
