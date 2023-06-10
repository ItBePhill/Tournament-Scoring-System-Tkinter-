import tkinter as tk
from tkinter import ttk, messagebox as mb
import subprocess
import os
import json
import sys

def catchexception(exc_type, exc_value, exc_traceback):
    print(f"{exc_type} {exc_value} {exc_traceback}")
    mb.showerror(title = "Something went wrong", message = e)
sys.excepthook = catchexception

filepath = os.getcwd()+"\\"
logspath = os.path.join(filepath, "Logs")
teampath = os.path.join(filepath, "Teams")
indivpath = os.path.join(filepath, "Indivs")

try:
    if not os.path.exists(teampath):
        os.mkdir(teampath)
    if not os.path.exists(indivpath):
        os.mkdir(indivpath)
except Exception as e:
    mb.showerror(title = "Something went wrong: ", message = e)

def startup(c):
    if c == "s":
        try:
            subprocess.check_call("python Signup(tk).py", shell = True)
        except Exception as e:
            mb.showerror(title = "Something went wrong", message = f"Something went wrong:  {e}")
    else:
        try:
            subprocess.check_call("python Events(tk).py", shell = True)
        except Exception as e:
            mb.showerror(title = "Something went wrong", message = f"Something went wrong:  {e}")
def viewselected(c):
    total = 0
    if c.find("--") != -1:
        mb.showwarning(title="Invalid Option", message = "You need to select an option")
    else:
        try:
            os.listdir(teampath).index(f"team {c}.json")

        except Exception as e:
            view = tk.Toplevel()
            view.geometry("400x600")
            view.title("View a Team / Individual")
            with open(os.path.join(indivpath, f"indiv {c}.json"), "r") as f:
                data = json.load(f)
                f.close()
            title = ttk.Label(view, text = data['name'], font = ("Segoe UI", 16))
            title.pack()
            for i in data:
                if data[i] == "":
                    result = "N/A"
                else:
                    result = data[i]
                ttk.Label(view, text = f"{i}:   {result}", font=("Segue UI", 10)).pack(pady=10)
                if i.find("name") == -1 and i != "id":
                    total += data[i]
                
            Ltotal = ttk.Label(view, text = f"Total Points = {total}", font=("Segue UI", 10))
            Ltotal.pack(pady = 10)
        else:
            view = tk.Toplevel()
            view.geometry("400x600")
            view.title("View a Team / Individual")
            with open(os.path.join(teampath, f"team {c}.json"), "r") as f:
                data = json.load(f)
                f.close()
            title = ttk.Label(view, text = data['teamname'], font = ("Segoe UI", 16))
            title.pack()
            for i in data:
                if data[i] == "":
                    result = "N/A"
                else:
                    result = data[i]
                ttk.Label(view, text = f"{i}:   {result}", font=("Segue UI", 10)).pack(pady=10)
                if i.find("name") == -1 and i != "id":
                    total += data[i]
                
            Ltotal = ttk.Label(view, text = f"Total Points = {total}", font=("Segue UI", 10))
            Ltotal.pack(pady = 10)
            
    

        




root =  tk.Tk()
root.geometry("800x600")
root.title("Tournament Scoring System Launcher")

viewvar = tk.StringVar()
viewoptions =  ["Please select an option", "--Teams--"]
#Teams
for i in os.listdir(teampath):
    if i.find("empty") == -1:
        with open(os.path.join(teampath, i), "r") as f:
            data = json.load(f)
            f.close()
        viewoptions.append(data["teamname"])
viewoptions.append("--Individuals--")
#Indivs
for i in os.listdir(indivpath):
    if i.find("empty") == -1:
        with open(os.path.join(indivpath, i), "r") as f:
            data = json.load(f)
            f.close()
        viewoptions.append(data["name"])

Title =  ttk.Label(text = "Tournament Scoring System Launcher", font = ("Segoe UI", 16))
Title.pack()

SFrame = ttk.Frame(root)
SFrame.pack(anchor="nw", side="left", pady=30)
EFrame = ttk.Frame(root)
EFrame.pack(anchor="ne", side="right", pady=30)
VFrame = ttk.Frame(root)
VFrame.pack(pady = 30)

SignupL = ttk.Label(SFrame, text = "Click here to create a team or participant:")
SignupL.pack()
EventsL = ttk.Label(EFrame, text = "Click here to add or remove points:")
EventsL.pack()

SignupB = ttk.Button(SFrame, text = "Signup", command = lambda: startup("s"))
SignupB.pack()
EventsB = ttk.Button(EFrame, text = "Events", command = lambda: startup("e"))
EventsB.pack()

ViewL = ttk.Label(VFrame, text = "Select a team or participant to view it:")
ViewL.pack()

ViewO = ttk.OptionMenu(VFrame, viewvar, *viewoptions, command = viewselected)
ViewO.pack()

def on_closing():
 
        if mb.askyesno(title = "Quitting", message= "Are you sure you want to quit?"):
            #close window and quit
            root.destroy()
            root.quit()
            quit(0)

# checks for closing the window and runs on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()