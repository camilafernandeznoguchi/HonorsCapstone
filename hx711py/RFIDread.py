#!/usr/bin/env python
import time
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
from mysql.connector import errorcode

sys.path.insert(0, '/home/camilaferno/Desktop/HonorsCapstone/hd44780')
import lcddriver

lcd = lcddriver.lcd()

def read():
    reader = SimpleMFRC522() #RFID
    
    print("Welcome. Please scan your ID")
    lcd.lcd_display_string("Please scan ", 1)
    lcd.lcd_display_string("       your ID", 2)
    
    id, text = reader.read()
    
    return id

def authenticate():
    authenticated = False
    
    try:
        cnx = mysql.connector.connect(user='fernandez', password='2303', host='frodo.bentley.edu', database='fernandez')
        cursor = cnx.cursor(buffered = True)

        query = ("SELECT * FROM user WHERE UID = %s")
        
        UID = (str(read()),) #FORMAT AS TUPLE
        cursor.execute(query, UID)
        
        user = cursor.fetchone()
        if user != None:
            firstName = user[1]
            lastName = user[2]
            email = user[3]
            
            lcd.lcd_clear()
            print("Welcome", firstName)
            lcd.lcd_display_string("Welcome: ", 1)
            lcd.lcd_display_string(firstName, 2)
            time.sleep(3)
            
            authenticated = True
    except mysql.connector.Error as err:
        print(err)
    finally:
        lcd.lcd_clear()
        cursor.close()
        cnx.close()
        GPIO.cleanup()
    
    return authenticated

#print(authenticate())