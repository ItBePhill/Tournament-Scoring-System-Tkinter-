from locale import normalize
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import datetime
import threading
import os
import sys
logs = []
version = "0.1"
teams = 0
indivs = 0
class util:
    #Logging
    def Log(ob):
        global f
        now = datetime.datetime.now()
        ob = str(ob)
        #create a string for the time and date that gets appended to the front of a log
        final = "\n\n["+now.strftime("%Y-%m-%d %H:%M:%S") + "]: " + ob
        print(final)
        try:
            #write to / create a log file
            with open(os.path.join(os.getcwd(), "Logs", str(len(logs)))+ " " +now.strftime("%Y-%m-%d")+ " log.txt" , "a") as f:
                f.write(final)
        except Exception as e:
            util.Error(e)
        #returns log file so the file can be closed when the program is closed instead of having to open the file every time the function is called
        return f
    #Called when an error occurs in the program and logs the error before closing
    def Error(e):
        util.Log("Something Went Wrong! Error:  " + str(e))
        mb.showerror(message = "Something Went Wrong! Closing!\nError: \n\n" + str(e), title = "Something went wrong")
        normal.root.quit()
        quit(0)

    def show_exception_and_exit(exc_type):
        util.Error(str(exc_type))

    sys.excepthook = show_exception_and_exit
    threading.excepthook = show_exception_and_exit

root =  tk.Tk()
root.geometry("800x600")
root.title("Events")

class normal:
    options = ["choose an option", "option1", "option2", "option3"]
    #Main window stuff
    WindowTitle = ttk.Label(root, text = "Events", font = ("Segoe UI", 16))
    WindowTitle.pack()
    



    def on_closing():

        if mb.askyesno(title = "Quitting", message= "Are you sure you want to quit?"):
            util.Log("Closing")
            #close log file
            f.close()
            #close window and quit
            root.destroy()
            root.quit()
            quit(0)



# checks for closing the window and runs on_closing function
root.protocol("WM_DELETE_WINDOW", normal.on_closing)
root.mainloop()
