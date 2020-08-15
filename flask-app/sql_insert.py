#INSERT Command


#import the sqlite3 library 
import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#INSERT data 

cursor.execute("INSERT INTO population VALUES('New York City','NY', 560076)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 65949)")

#commit the change
conn.commit()

#close the database connection
conn.close()
