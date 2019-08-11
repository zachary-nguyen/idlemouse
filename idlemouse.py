import pyautogui, time

delay = int(input("Enter interval of refresh (seconds)" 
                  "\n 1 minute = 60s \n 5 minutes = 300s \n 10 minutes = 600s \n Interval (1 min minimum):"))

while True:
    if(delay >= 60):
        break
    delay = int(input("Enter a value greater than 60" 
                      "\n 1 minute = 60s \n 5 minutes = 300s \n 10 minutes = 600s \n Interval (1 min minimum):"))

print("Refreshing screen every " + str(delay) + " seconds")

while True :
       
    time.sleep(delay)
    pyautogui.dragTo(100, 150)

print("Program terminated!")    
   
