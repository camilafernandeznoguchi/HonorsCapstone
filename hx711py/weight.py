#! /usr/bin/python2
import time
import sys

sys.path.insert(0, '/home/camilaferno/Desktop/HonorsCapstone/hd44780')
import lcddriver

import RFIDread
import writePoints

EMULATE_HX711=False #weight
lcd = lcddriver.lcd() #lcd

referenceUnit = 1
pointScale = 0.02 #100 points = 5000g = 5kg

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

try:
    #Authenticate user
    isAuthenticated, UID = RFIDread.authenticate()
    if isAuthenticated:
        print("Setting up the scale...")
        lcd.lcd_display_string("Setting up scale", 1)
        
        hx = HX711(5, 6)
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
        
        lcd.lcd_clear()
        print("Add weight now...")
        lcd.lcd_display_string("Add weight now", 1)
        time.sleep(5)
        lcd.lcd_clear()

        counter = 0
        while True:
            val = max(0, int(hx.get_weight(5)))
            print(val)
            if counter >= 5 and val > 0:
                print("The weight is: ", val)
                lcd.lcd_display_string("The weight is: ", 1)
                lcd.lcd_display_string(str(val)+" grams", 2)
                
                time.sleep(3)
                
                #Points
                points = round(val*pointScale)
                
                writePoints.updatePoints(UID, points)
                
                lcd.lcd_clear()
                print("You win:", points, "points")
                lcd.lcd_display_string("You win: ", 1)
                lcd.lcd_display_string(str(points)+" points", 2)
                
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
        GPIO.cleanup()
    else:
        lcd.lcd_display_string("Unable to ", 1)
        lcd.lcd_display_string("   authenticate", 2)
        print("Unable to authenticate user")
        time.sleep(3)
        
except KeyboardInterrupt:
    print("Keyboard Interrupt. Closing program...")
except Exception as e:
    print("Error:", str(e), "Closing program...")
finally:
    lcd.lcd_clear()
    lcd.lcd_display_string("Thank you!", 1)
    time.sleep(3)
    lcd.lcd_clear()
    print("Thank you!")
    sys.exit()