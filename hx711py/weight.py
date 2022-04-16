#! /usr/bin/python2
import time
import sys
#import RPi.GPIO as GPIO #RFID
from mfrc522 import SimpleMFRC522 #RFID

sys.path.insert(0, '/home/camilaferno/Desktop/HonorsCapstone/hd44780')
import lcddriver

def authenticateUser():
    print("Welcome. Please scan your ID")
    id, text = reader.read()
    if id == user1["UID"]:
        print("Welcome", user1["firstName"])
    return True
    

user1 = {'UID': 188435878401, "firstName": "John", 'lastName': "Doe"}

reader = SimpleMFRC522() #RFID

EMULATE_HX711=False #weight
lcd = lcddriver.lcd() #lcd

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
#else:
#    from emulated_hx711 import HX711

try:
    #Authenticate user
    if authenticateUser():
        print(EMULATE_HX711)
        hx = HX711(5, 6)
        print("here")
        hx.set_reading_format("MSB", "MSB")

        # HOW TO CALCULATE THE REFFERENCE UNIT
        # To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
        # In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
        # and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
        # If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
        hx.set_reference_unit(229)
        #hx.set_reference_unit(referenceUnit)

        hx.reset()

        hx.tare()

        print("Add weight now...")
        time.sleep(5)

        counter = 0
        while True:
            val = max(0, int(hx.get_weight(5)))
            print(val)
            if counter >= 5 and val > 0:
                print("The weight is: ", val)
                lcd.lcd_display_string("The weight is: ", 1)
                lcd.lcd_display_string(str(val)+" grams", 2)
                time.sleep(5)
                break
                
            print("Calculating weight...")
            lcd.lcd_display_string("Calculating", 1)
            lcd.lcd_display_string("weight...", 2)
            
            counter += 1

            hx.power_down()
            hx.power_up()
            time.sleep(3)
            lcd.lcd_clear()
    else:
        print("Unable to authenticate user")
except KeyboardInterrupt:
    print("Keyboard Interrupt. Closing program...")
except Exception as e:
    print("Error:", str(e), "Closing program...")
finally:
    lcd.lcd_clear()
    GPIO.cleanup()
    print("Thank you!")
    sys.exit()