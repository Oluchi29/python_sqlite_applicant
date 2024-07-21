#Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called applicants 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python new_table.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected successfully to database")

conn.execute('CREATE TABLE applicants (name TEXT, email TEXT, phoneno TEXT, job_title TEXT)')


print(" I Created a table successfully!")

conn.close()

