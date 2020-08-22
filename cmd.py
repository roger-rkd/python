# making the entire code under a while loop so that the code dies not shuts down until or unless asked
while True:
    # importing two libraries 
    import os
    import pyttsx3
    a=input("How can I help you? : ")
    
    # for launching notepad
    if(("notepad" in a) or ("editor" in a))and(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("notepad")
        pyttsx3.speak("Launching notepad for you")
    
    # for launching google chrome
    elif(("chrome" in a) or ("google chrome" in a) or ("browser" in a))and(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("start chrome")
        pyttsx3.speak("Launching Google chrome for you")
    
    # for launching microsoft edge
    elif(("edge" in a) or ("microsoft edge" in a) or ("browser" in a))and(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("msedge")
        pyttsx3.speak("Launching Google chrome for you")

    # for launching visual studio code
    elif(("code" in a) or ("code editor" in a) or ("ide" in a) or ("vs code" in a) or ("visual studio code" in a))quitand(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("Code")
        pyttsx3.speak("Launching visual studio code for you")
        
     # for launching vlc media player
    elif(("vlc" in a) or ("audio player" in a) or ("video player" in a) or ("audio video player" in a) or ("vlc player" in a))quitand(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("vlc")
        pyttsx3.speak("Launching vlc player for you")

    # for launching windows media player
    elif(("windows media player" in a) or ("audio player" in a) or ("video player" in a) or ("audio video player" in a))quitand(("run" in a) or ("execute" in a) or ("launch" in a)or ("open" in a)):
        os.system("wmplayer")
        pyttsx3.speak("Launching windows media player for you")
    
    # for stoping the code
    elif(("quit" in a)or("stop" in a)):
        pyttsx3.speak("shutting down the program for you, have a good day")
        break
    
    # for an invalid statement entered
    else:
        print("Command is not recognized, Sorry!")
        pyttsx3.speak("Command is not recognized, Sorry")
