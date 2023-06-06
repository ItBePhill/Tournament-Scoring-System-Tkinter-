import tkinter as tk
from tkinter import messagebox as mb, ttk
import datetime
import threading
import os
import sys
import json
logs = []
version = "0.1"
teams = 0
indivs = 0
filepath = os.path.dirname(__file__)+r"\\"
logspath = os.path.join(filepath, "Logs")
teampath = os.path.join(filepath, "Teams")
indivpath = os.path.join(filepath, "Indivs")
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
ti = ""
def eventcallback(eventvar):
        def selected(var):
            global ti
            if var.find("--") == -1:
                print(f"You picked: {var}")
                if str(os.listdir(teampath)).find(var) != -1:
                    ti = "t"
                    print(ti)
                else:
                    ti = "i"
                    print(ti)
            else:
                mb.showwarning(title="Invalid Option", message = "You need to pick one of the options!")
                return ti



                
        pickervar = tk.StringVar()


        if eventvar.find("--") != -1:
            mb.showwarning(title="Invalid Option", message="You need to pick one of the options!")
        else:
            options = ["Please select a Team or Individual", "--Teams--"]
            for i in os.listdir(teampath):
                print(i)
                if i.find("empty") == -1:
                    with open(os.path.join(teampath, i), "r") as f:
                        j = json.load(f)["teamname"]
                        print(j)
                        f.close()
                    options.append(j)
            options.append("--Individuals--")
            for i in os.listdir(indivpath):
                print(i)
                if i.find("empty") == -1:
                    with open(os.path.join(indivpath, i), "r") as f:
                        j = json.load(f)["name"]
                        print(j)
                        f.close()
                    options.append(j)
                
            

            pickpar = tk.Toplevel(root)
            pickpar.geometry("400x300")
            pickpar.title("Choose a team / Individual")
            pickpartitle = ttk.Label(pickpar, text = "Pick a Participant")
            pickpartitle.pack()
            picker = ttk.OptionMenu(pickpar, pickervar, *options, command = selected)
            picker.pack()

            def addpoints(amt):
                    if options.index(pickervar.get()) != 0 and pickervar != "--Teams--" and pickervar != "--Individuals--":
                        if ti == "t":
                            print(f"t add {amt} to {pickervar.get()}")
                            with open(os.path.join(teampath, f"team {pickervar.get()}")+".json", "r") as f:
                                data = json.load(f)
                                f.close()
                                with open(os.path.join(teampath, f"team {pickervar.get()}")+".json", "w") as f:
                                    try:
                                        data[eventvar] += amt
                                    except KeyError:
                                        data[eventvar] = amt

                                    json.dump(data, f)
                                    f.close()
                        elif ti == "i":
                            print(f"i add {amt} to {pickervar.get()}")
                            with open(os.path.join(indivpath, f"indiv {pickervar.get()}")+".json", "r") as f:
                                data = json.load(f)
                                f.close()
                                with open(os.path.join(indivpath, f"indiv {pickervar.get()}")+".json", "w") as f:
                                    try:
                                        data[eventvar] += amt
                                    except KeyError:
                                        data[eventvar] = amt

                                    json.dump(data, f)
                                    f.close()

            def rempoints(amt):
                if options.index(pickervar.get()) != 0 and pickervar != "--Teams--" and pickervar != "--Individuals--":
                        if ti == "t":
                            print(f"t rem {amt} to {pickervar.get()}")
                            with open(os.path.join(teampath, f"team {pickervar.get()}")+".json", "r") as f:
                                data = json.load(f)
                                f.close()
                                with open(os.path.join(teampath, f"team {pickervar.get()}")+".json", "w") as f:
                                    try:
                                        data[eventvar] -= amt
                                    except KeyError:
                                        data[eventvar] = -amt

                                    json.dump(data, f)
                                    f.close()
                        elif ti == "i":
                            print(f"i rem {amt} to {pickervar.get()}")
                            with open(os.path.join(indivpath, f"indiv {pickervar.get()}")+".json", "r") as f:
                                data = json.load(f)
                                f.close()
                                with open(os.path.join(indivpath, f"indiv {pickervar.get()}")+".json", "w") as f:
                                    try:
                                        data[eventvar] -= amt
                                    except KeyError:
                                        data[eventvar] = -amt

                                    json.dump(data, f)
                                    f.close()

            buttonframe =  ttk.Frame(pickpar)
            buttonframe.pack(pady = 20)

            addframe = ttk.Frame(pickpar)
            addframe.pack(anchor = "nw", side = "left", padx = 30)
            remframe = ttk.Frame(pickpar)
            remframe.pack(anchor = "ne", side = "right", padx = 30)


            atitle = ttk.Label(addframe, text = "Add Points:")
            atitle.pack()
            atenbutton = ttk.Button(addframe, text = "+ 10 Points", command  = lambda : addpoints(10))
            atenbutton.pack()
            atwentybutton = ttk.Button(addframe, text = "+ 20 Points", command  = lambda : addpoints(20))
            atwentybutton.pack()
            athirtybutton = ttk.Button(addframe, text = "+ 30 Points", command  = lambda : addpoints(30))
            athirtybutton.pack()
            afortybutton = ttk.Button(addframe, text = "+ 40 Points", command  = lambda : addpoints(40))
            afortybutton.pack()
            rtitle = ttk.Label(remframe, text = "Remove Points:")
            rtitle.pack()
            rtenbutton = ttk.Button(remframe, text = "- 10 Points", command  = lambda : rempoints(10))
            rtenbutton.pack()
            rtwentybutton = ttk.Button(remframe, text = "- 20 Points", command  = lambda : rempoints(20))
            rtwentybutton.pack()
            rthirtybutton = ttk.Button(remframe, text = "- 30 Points", command  = lambda : rempoints(30))
            rthirtybutton.pack()
            rfortybutton = ttk.Button(remframe, text = "- 40 Points", command  = lambda : rempoints(40))
            rfortybutton.pack()



class normal:
    options = ["Please Select an Event", "--Sporting--", "Sporting1", "Sporting2","--Academic--", "Academic1", "Academic2"]
    #Main window stuff
    WindowTitle = ttk.Label(root, text = "Events", font = ("Segoe UI", 16))
    WindowTitle.pack()
    eventvar = tk.StringVar()

    eventmenu = ttk.OptionMenu(root, eventvar, *options, command = eventcallback)
    eventmenu.pack()    
    
    
    
    

    



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
