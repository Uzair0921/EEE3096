#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
c = 0
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Logic that you write
def my_callback(channel):
    global c
    chan_list = (13,12,11)
 
    if c == 0 :
        GPIO.output(chan_list, 0)
    elif c == 1 :
        GPIO.output(chan_list, (0,0,1))
    elif c == 2 :
        GPIO.output(chan_list, (0,1,0))
    elif c == 3 :
        GPIO.output(chan_list, (0,1,1))
    elif c == 4 :
        GPIO.output(chan_list, (1,0,0))
    elif c == 5 :
        GPIO.output(chan_list, (1,0,1))
    elif c == 6 :
        GPIO.output(chan_list, (1,1,0))
    elif c == 7 :
        GPIO.output(chan_list, (1,1,1))

    
GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback, bouncetime=200)  # add rising edge detection on a channel
GPIO.add_event_detect(18, GPIO.RISING, callback=my_callback, bouncetime=200)
def main():
    global c
    print(c)
    time.sleep(0.2)
    if GPIO.event_detected(16):
        c += 1
        
        if c > 7:
            c = 0
        elif c < 0:
            c = 7  
    if GPIO.event_detected(18):
        c -= 1
        
        if c > 7:
            c = 0
        elif c < 0:
            c = 7  
    my_callback(16)
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
