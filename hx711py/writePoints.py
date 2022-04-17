import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

def updatePoints(UID,points):
    try:
        cnx = mysql.connector.connect(user='fernandez', password='2303', host='frodo.bentley.edu', database='fernandez')
        cursor = cnx.cursor(buffered = True)

        query = ("INSERT INTO point (UID, earnDate, point) VALUES (%s,%s,%s)")
        earnDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        values = (UID, earnDate, points)
        
        cursor.execute(query,values)
        cnx.commit()
        
        print("Inserted successfully")
        
    except mysql.connector.Error as err:
        print(err)
    finally:
        cursor.close()
        cnx.close()