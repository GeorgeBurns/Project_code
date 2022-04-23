from machine import Pin
import utime
# This is the tuple that contains the collections of pins that corruspond to the number I.E Tens[1] = 1

Tens = ((11,12,6,7,8,9),(12,6),(11,12,10,8,7),(11,12,10,6,7),(9,10,12,6),
        (11,9,10,6,7),(11,9,10,6,8,7),(12,6,11),(11,12,6,7,8,9,10),(11,9,10,12,6))
Ones = ((14,15,16,18,5,13),(15,16),(14,15,5,18,17),(14,15,16,18,17),(15,16,17,13),(14,13,17,16,18),
          (13,16,17,18,5),(15,16,14),(14,15,16,18,5,13,17),(14,15,17,13,16))
#Define the interupt pin
interupt_pin = Pin(0, Pin.IN, Pin.PULL_DOWN)
#define count
count = 0 
def Check_pin(x):
    """Checks the state of a pin if the pin is on it will return 1 else will return 0"""
    return Pin(x).value()


def Turn_pin(x,State):
    """Turns the pin on or off using state = either true or false and x is the pin number example input Turn_pin(11,True)"""
    pin = Pin(x,Pin.OUT) #Declare the pin class for num x and a output pin
    if State == True:
        pin.value(1) #If state is True Turn the pin on 
    elif State == False: 
        pin.value(0) #If state is False turn pin off
    else:
        pass    #Else do nothing

def Clear_pins():
    """Clears all pins that are on very useful as pins do not turn off automatically"""
    for i in Ones: # For all values in Ones
        for x in i: # For all values inside Ones[i] if pin state is 1 then it will turn off the pin
            if Check_pin(x) == 1:
                Turn_pin(x,False)
    for i in Tens: #For all values in tens
        for x in i: # For all values inside Tens[i] if pin state is 1 then it will turn off the pin
            if Check_pin(x) == 1: 
                Turn_pin(x,False)
                

def Set_digit_state(digit,value):
    Clear_pins() #Clears pins before pin change
    """Will set the digit sate, I.E Set_digit_state(3,tens) will display 30 on the hexidecimal display"""
    if digit.lower() == "tens": #If the digit is tens
        for i in Tens[int(value)]:
            Turn_pin(i,True)  #for all values in that tuple value turn the pin on
    if digit.lower() == "ones":
        for i in Ones[int(value)]:
            Turn_pin(i,True) #for all values in that tuple value turn the pin on

#
def Tens_finder(x):
    """Will find the the value of the tenth number in a string I.E Tens_finder(99) will display 90 on the hexidecimal"""
    x = [int(i) for i in str(x)] #For all "Str" values in the integer convert them into integers and crate a list
    Set_digit_state("tens",x[-2]) #Set the tens value to the Tens 1st value of the list
    Set_digit_state("ones",0) #Set the digit value to 0

def Int_to_7_seg(Int):
    """Will take any integer and return it as a valid format for the hexidecimal display that can be used in conjuntion with Set_digit_state"""
    Int = "%02d" % round(float(Int)) #Turn the input of the function into a integer with two values a tens and digit
    if int(Int) > 99:
        raise Exception("Please enter a number less then 100") #If the number is > 99 raise the error Please enter a number less then 100
    return [int(x) for x in str(Int)] #returns the integer as a list in format [digit,tens]


def counter():
    """Counts from 0,100 on the hexidecimal display"""
    for i in range(0,100): #For i in range 0 to 100 display the number
        ls = Int_to_7_seg(i)
        Set_digit_state("ones",ls[1]);Set_digit_state("tens",ls[0])
        utime.sleep(1)
        Clear_pins() #clear after every iteration

   

def Task_2_9():
    """Asks the user what value they would like to display on the value"""           
    In = "%02d" % round(float(input("What is your number ")))#Turn the input of the function into a integer with two values a tens and digit
    if int(In) > 99:
        raise Exception("Please enter a number less then 100") #If the number is > 99 raise the error Please enter a number less then 100
    In = [int(x) for x in str(In)] #turns the integer into a list that splits the integer into tens and digits
    Set_digit_state("tens", In[0]);Set_digit_state("ones", In[1]) #Set the digit on the hexidecimal display to the value given 


#Always run Clear_pins so all pins are cleared on the display 

def myISR(pin):
    """The pin for defining the interupt program"""
    global count #make varible count global
    count = count + 1 #Add one to count
Clear_pins() 

Set_digit_state("digit", 0);Set_digit_state("tens", 0) #set to 00
interupt_pin.irq(handler = myISR, trigger = Pin.IRQ_FALLING)
while __name__ == "__main__": #Always run
    if count >= 10:#If count becomes greater then 10, reset count to 0
        count = 0
    display = Int_to_7_seg(count) #set the value display to the 7-segment format of count
    Set_digit_state("ones",display[1]);Set_digit_state("tens",display[0]) #Show the value of display on the hexidecimal display 
     
    
    


