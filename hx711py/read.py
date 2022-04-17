import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='fernandez', password='2303', host='frodo.bentley.edu', database='fernandez')
    cursor = cnx.cursor(buffered = True)

    query = ("SELECT * FROM user WHERE UID = %s")
    UID = ("188435878401",)
    
    cursor.execute(query, UID)
    
    for row in cursor:
        print(row)
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    cnx.close()