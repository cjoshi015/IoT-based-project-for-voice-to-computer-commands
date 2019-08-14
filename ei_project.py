import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('/dev/ttyACM1',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print incoming
    
    if 'play' in incoming:
        pyautogui.typewrite(['space'], 0.2)
    
    elif 'pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)
    
    elif 'rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  
    
    elif 'close' in incoming:
        pyautogui.hotkey('alt', 'f4')  
   	
   	
    elif 'forward' in incoming:
		a=incoming.split(" ")
		print a
		if len(a)>2:
			if "minute" or "minutes" in a:
				for i in range(int(a[2])):
					print a[2]
					pyautogui.hotkey('ctrl', 'right') 	
					time.sleep(1)	
		else:
			pyautogui.hotkey('ctrl', 'right') 

    elif 'volume down' in incoming:
        for i in range(4):
        	pyautogui.hotkey('ctrl', 'down')
        #pyautogui.hotkey('ctrl', 'down')
    elif 'mute' in incoming:
        pyautogui.hotkey('m')  
    
        

    elif 'volume up' in incoming:
        for i in range(4):
        	pyautogui.hotkey('ctrl', 'up')
        #pyautogui.hotkey('ctrl', 'up')
        
    elif 'delete all' in incoming:
    	pyautogui.hotkey('ctrl', 'a')
    	pyautogui.typewrite(['space'], 0.2)
   
    elif 'unmute' in incoming:
    	pyautogui.hotkey('m') 
    
    elif 'take screenshot' in incoming:
    	pyautogui.hotkey('prtsc')
    	time.sleep(2)
    	pyautogui.hotkey('enter')
    	 
    	   
    elif 'open edit' in incoming:
    	pyautogui.click(x=30,y=100,clicks=2)
 
    elif 'switch window' in incoming:
    	pyautogui.hotkey('alt','tab')
   
    elif 'open terminal' in incoming:
    	pyautogui.hotkey('ctrl','alt','t')
   
    elif len(incoming)>15:
    	pyautogui.click(x=85,y=118)
    	pyautogui.typewrite(incoming)
    	

    incoming = "";
