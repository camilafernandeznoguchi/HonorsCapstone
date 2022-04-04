import lcddriver
import time
 
lcd = lcddriver.lcd()
lcd.lcd_clear()

username = "camilaferno"
 
lcd.lcd_display_string("Welcome", 1)
lcd.lcd_display_string(username, 2)
time.sleep(3)
lcd.lcd_clear()


