from pyfirmata import Arduino, util
import time

board = Arduino('COM3')
pin = board.get_pin('a:0:i')            #analog pin 0 input

led_light = board.get_pin('d:3:p')      #led light digital pin 3 p for Pulse-width modulation
led_light2 = board.get_pin('d:5:p')     #These pins are not radnomly chosen.
led_light3 = board.get_pin('d:9:p')     #On Arduino Uno, the PWM pins are 3, 5, 6, 9, 10 and 11.
led_light4 = board.get_pin('d:10:p')

iterator = util.Iterator(board)
iterator.start()
time.sleep(0.1)

try:
    while True:

        analog_value = pin.read()
        #str_val = '%.3f' % (analog_value)      #converting input to string this was my first solution how to conver 'NoneType'
        round_value = round(analog_value, 3)    #setting input to 3 decimals
        value_as_float = float(round_value)     #converting round_value to float
        print(value_as_float)

        time.sleep(0.1)

        #Splitting potentiometer on 4 each quarter dirves one led
        if value_as_float < 0.250:
            led_light.write(value_as_float * 4)    #Setting value from 0 - 0.250 as 0-1
            led_light2.write(0)
            led_light3.write(0)
            led_light4.write(0)

        elif value_as_float >= 0.250 and value_as_float<= 0.500:
            led_light2.write((value_as_float - 0.250) * 4)  #Setting value to 0 than value from 0.250 - 0.500 as 0-1
            led_light3.write(0)
            led_light4.write(0)

        elif value_as_float >= 0.500 and value_as_float <= 0.750:
            led_light3.write((value_as_float - 0.500) * 4)  #Setting value to 0 than value from 0.500 - 0.750 as 0-1
            led_light4.write(0)

        elif value_as_float >= 0.750:
            led_light4.write((value_as_float - 0.750) * 4)  #Setting value to 0 than value from 0.750 - 1 as 0-1
except KeyboardInterrupt:
    board.exit()
