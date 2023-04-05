# Instead of creating the database manually in mysql, we have to create it automatically.
#pip3 install mysql-connector -- produces error
#pip3 install mysql-connector-python -- could be successful

# for now I am creating a database crm by hand manually in mysql.

import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'subham123',
)

#prepare a cursor object

cursorObject  = dataBase.cursor()

#Create a database by the name crm
cursorObject.execute("CREATE DATABASE crm")




