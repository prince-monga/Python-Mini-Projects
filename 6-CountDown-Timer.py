#Step 1: import time modul
import time

#Step 2: Create Function for display Countdown 

def Countdown_timer(seconds):
    while seconds:
        #Calculate Minutes and seconds
        mins, secs=divmod(seconds, 60)
        
        #format as mm:secs
        #print the countdown timer
        #end="\r" is used to print on the same line
        #f-string is used to format the string
        #f"{mins:02d}:{secs:02d}" is used to format the string with 2 digits
        timer=f"{mins:02d}:{secs:02d}"
        print(timer,end="\r")

        
        #wait for 1 seconds
        time.sleep(1)
        
        seconds-=1
    print("Times Up!")
    
try:
    total_time=int(input("Enter countdown time in seconds:"))
    Countdown_timer(total_time)
except ValueError:
    #Handle invalid input
    print("Invaild input")
