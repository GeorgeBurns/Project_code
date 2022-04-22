from machine import Pin
import utime
import time

# This is the 
Tens = [[11,12,6,7,8,9],[12,6],[11,12,10,8,7],[11,12,10,6,7],[9,10,12,6],
        [11,9,10,6,7],[11,9,10,6,8,7],[12,6,11],[11,12,6,7,8,9,10],[11,9,10,12,6]]
Ones = [[14,15,16,18,5,13],[15,16],[14,15,5,18,17],[14,15,16,18,17],[15,16,17,13],[14,13,17,16,18],
          [13,16,17,18,5],[15,16,14],[14,15,16,18,5,13,17],[14,15,17,13,16]]
count = 0
led = Pin(1, Pin.OUT)
pushbutton = Pin(0,Pin.IN, Pin.PULL_UP)
def Check_pin(x):
    return Pin(x).value()
def Turn_pin(x,State):
    pin = Pin(x,Pin.OUT)
    if State == True:
        pin.value(1)
    if State == False:
        pin.value(0)
    else:
        pass   
def Clear_pins():
    for i in Ones:
        for x in i:

            if Check_pin(x) == 1:
                Turn_pin(x,False)
    for i in Tens:
        for x in i:
            if Check_pin(x) == 1:
                Turn_pin(x,False)
Clear_pins()
def Set_digit_state(digit,value):
    if digit.lower() == "tens":
        for i in Tens[int(value)]:
            Turn_pin(i,True)
    if digit.lower() == "ones":
        for i in Ones[int(value)]:
            Turn_pin(i,True)

def Int_to_7_seg(Int):
    Clear_pins()
    Int = "%02d" % round(float(Int))
    if int(Int) > 99:
        print("Please enter a number under 100")
    Int = [int(x) for x in str(Int)]
    return Int

    
def myISR(pin):
    global count
    led.toggle()
    count = count + 1

pushbutton.irq(handler = myISR, trigger = Pin.IRQ_FALLING)
while True:
    if count >= 10:
        count = 0
    display = Int_to_7_seg(count)
    print(display)
    Set_digit_state("ones",display[1]);Set_digit_state("tens",display[0])
    
    
    


