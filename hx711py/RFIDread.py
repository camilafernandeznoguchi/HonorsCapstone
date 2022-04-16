#!/usr/bin/env python
import time
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

sys.path.insert(0, '/home/camilaferno/Desktop/HonorsCapstone/hd44780')
import lcddriver

def authenticateUser():
    authenticated = False
    
    lcd = lcddriver.lcd() #lcd
    
    user1 = {'UID': 188435878401, "firstName": "John", 'lastName': "Doe"}
    reader = SimpleMFRC522() #RFID
    
    print("Welcome. Please scan your ID")
    lcd.lcd_display_string("Please scan ", 1)
    lcd.lcd_display_string("       your ID", 2)
    
    id, text = reader.read()
    lcd.lcd_clear()
    if id == user1["UID"]:
        print("Welcome", user1["firstName"])
        lcd.lcd_display_string("Welcome: ", 1)
        lcd.lcd_display_string(user1["firstName"], 2)
        time.sleep(3)
        lcd.lcd_clear()
        
        authenticated = True
        GPIO.cleanup()
    return authenticated