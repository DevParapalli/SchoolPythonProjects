import mysql.connector
import os

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv('MYSQLPASSWORD', 'roguecatalyst') # gets the my sql password either from the system environment variable
    # or from the default value.
)

cursor = database.cursor()

#mycursor.execute('CREATE DATABASE mydatabase') # if the database does not exist
cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)


