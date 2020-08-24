import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv('MYSQLPASSWORD', 'roguecatalyst') # gets the my sql password either from the system environment variable
    # or from the default value.
)

mycursor = mydb.cursor()

#mycursor.execute('CREATE DATABASE mydatabase')
mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)


