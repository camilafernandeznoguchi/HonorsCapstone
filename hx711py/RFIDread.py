#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def authenticateUser():
    authenticated = False
    
    user1 = {'UID': 188435878401, "firstName": "John", 'lastName': "Doe"}
    reader = SimpleMFRC522() #RFID
    
    print("Welcome. Please scan your ID")
    id, text = reader.read()
    if id == user1["UID"]:
        print("Welcome", user1["firstName"])
        authenticated = True
        GPIO.cleanup()
    return authenticated