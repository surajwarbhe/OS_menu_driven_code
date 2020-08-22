#importing applications in Windows

import os 
import pyttsx3
import calender
import date
username="Suraj"
secret_code="17042001"
flag=1
    while (flag==1):
	print(" Enter your Username : ")
	pyttsx3.speak("Enter your Username")
	u=input()
	print("Enter your Secret code : ")
	pyttsx3.speak("Enter your Secret code ")
	s=input()
	if username==u and  secret_code==s:
	        pyttsx3.speak("Welcome to Windows 10")
		print("**Welcome to Windows 10 !!!**")
		pyttsx3.speak("Hello Suraj")
		print("Hello Suraj!!!")
		pyttsx3.speak("How can I help you")
		print("How can I help you :)")
		p=input()
		
                 while(True):
                      if(("run" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p) or ("notes" in p)):
 	                      pyttsx3.speak("Launching notepad")
                              os.system("notepad")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("Google" in p)):
 	                      pyttsx3.speak("Launching chrome")  
                              os.system("chrome")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("browser" in p):
 	                      pyttsx3.speak("Launching Browser") 
                              os.system("browser")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("internet" in p) or ("explorer" in p) or ("search" in p)):
 	                      pyttsx3.speak("Launching internet explorer")
                              os.system("explorer")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("mozilla firefox" in p):
 	                      pyttsx3.speak("Launching mozilla firefox") 
                              os.system("firefox") 
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("mxplayer" in p):
 	                      pyttsx3.speak("Launching mxplayer") 
                              os.system("mxplayer")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("photo viewer" in p):
                              pyttsx3.speak("Launching windows photo viewer")
                              os.system("windows photo viewer")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("ms office" in p) or ("microsoft office" in p):
                              pyttsx3.speak("Launching microsoft office")
                              os.system("microsoft office")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("ms word" in p) or ("microsoft word" in p):
                              pyttsx3.speak("Launching microsoft word")
                              os.system("microsoft word")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("ms powerpoint" in p) or ("microsoft powerpoint" in p)):
                              pyttsx3.speak("Launching microsoft powerpoint")
                              os.system("microsoft powerpoint")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("ms word" in p) or ("microsoft excel" in p)):
                              pyttsx3.speak("Launching microsoft excel")	
                              os.system("microsoft excel")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or (("ms outlook" in p) or ("microsoft outlook" in p)):
                              pyttsx3.speak("Launching microsoft outlook") 
                              os.system("microsoft outlook")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or (("ms access" in p) or ("microsoft access" in p)):
                              pyttsx3.speak("Launching microsoft access")	
                              os.system("microsoft access")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("game" in p):
                              pyttsx3.speak("Launching game")
                              os.system("game")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("music player" in p):
                              pyttsx3.speak("Launching music player")	    
                              os.system("music player")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and (("turboc" in p) or ("turbo" in p):
                              pyttsx3.speak("Launching Turbo C++")
                              os.system("turbocpp")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("anaconda" in p):
                              pyttsx3.speak("Launching anaconda")
                              os.system("Anaconda")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("eclipse" in p):
 	                      pyttsx3.speak("Launching eclipse")
                              os.system("eclipse")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("jupyter notebook" in p):
 	                      pyttsx3.speak("Launching Jupyter notebook")
                              os.system("jupyter notebook")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("devc++" in p):
                              pyttsx3.speak("Launching dev C++")
                              os.system("devcpp")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("paint" in p):
 	                      pyttsx3.speak("Launching microsoft paint")
                              os.system("microsoft paint")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("vlc" in p):
                              pyttsx3.speak("Launching VLC Player")
                              os.system("vlc")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) and (("fb" in p) or ("facebook")):
                              pyttsx3.speak("Launching Facebook")
                              os.system("facebook")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) and ("whatsapp" in p):
                              pyttsx3.speak("Launching WhatsApp")
                              os.system("whatsapp")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("linkedin" in p):
                              pyttsx3.speak("Launching LinkedIn")
                              os.system("linkedIn")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("insta" in p) or ("instagram" in p)):
                              pyttsx3.speak("Launching Instagram")
                              os.system("instagram")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("Slack in p"):
                              pyttsx3.speak("Launching Slack")
                              os.system("slack")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("safari" in p):
                              pyttsx3.speak("Launching Safari")	
                              os.system("safari")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("spotisfy" in p):
                              pyttsx3.speak("Launching Spotify") 
                              os.system("spotisfy")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("desktop" in p):
 	                      pyttsx3.speak("Launching desktop")  
                              os.system("desktop")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("PC" in p):
                              pyttsx3.speak("Launching this PC")
                              os.system("this pc")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("computer" in p):
                              pyttsx3.speak("Launching computer")
                              os.system("computer")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("recycle" in p) or ("bin" in p)):
 	                      pyttsx3.speak("Launching Recycle bin")  
                              os.system("recycle bin")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("documents" in p):
                              pyttsx3.speak("Launching my documents") 
                              os.system("my documents")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("adobe reader" in p):
                              pyttsx3.speak("Launching Adobe reader 8")
                              os.system("adobe reader 8")
                      elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("control panel" in p):
                              pyttsx3.speak("Launching control panel") 
                              os.system("control panel")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("command prompt" in p):
 	                      pyttsx3.speak("Launching command prompt") 
                              os.system("command prompt")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("onedrive" in p):
 	                      pyttsx3.speak("Launching Onedrive")    
                              os.system("onedrive")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("network" in p):
 	                      pyttsx3.speak("Launching network")   
                              os.system("network")
                      elif(("run" in p) or ("open" in p) or ("execute" in p) or ("play" in p)) and ("calculator" in p):
 	                      pyttsx3.speak("Launching calculator") 
                              os.system("calc") 
                      elif("date" in p):
 	                      os.system("date")
                      elif("calender" in p):
 	                      os.system("calender")
                      elif("time" in p):
 	                      os.system("time")
                      elif (("create folder" in p) or ("create directory" in p) or ("new folder" in p)):
 		              pyttsx3.speak("provide name of the directory")
 		              print("provide name for the directory : ")
			        f=input()
				x="mkdir "+f
				os.system(f)
				print("New directory created succesfully!!!")
		      elif ("remove directory" in p) or ("delete folder" in p) :
			      pyttsx3.speak("provide name of the directory")
			      print("provide name of the directory : ")
				f=input()
				x="rmdir "+f
				os.system(f)
				print("Directory removed succesfully!!!")
		      else :
			      pyttsx3.speak("Sorry, not found")
			      print("Sorry, Not found!!!")
		              print("\nDo you want to continue(y/n):")
				a=input()
				if("y" in a):
				     flag=1
				else:
				     pyttsx3.speak("Thank you!!")
				     print("Thank you Suraj!!!")
				     break
