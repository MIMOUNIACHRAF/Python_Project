import mysql.connector

dataBase = mysql.connector.connect(host='localhost',
                                   user='achraf',
                                   passwd='Colle ciment1.')
# preparer a cusor object
cursorObject = dataBase.cursor()

# cearate database
cursorObject.execute("CREATE DATABASE P_CRM")

print("all Done")