#imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import os
import glob
import datetime
import json
import threading
import time
"hello".split
#Backend===================================================================================
#global variables like logs list and teams/individuals
logs = []
version = "0.1"
teams = 0
indivs = 0

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
        Error(e)
    #returns log file so the file can be closed when the program is closed instead of having to open the file every time the function is called
    return f
#Called when an error occurs in the program and logs the error before closing
def Error(e):
    Log("Something Went Wrong! Error: " + str(e))
    mb.showerror(message = "Something Went Wrong!\nError: " + str(e), title = "Something went wrong")
    root.quit()
    quit(0)

#team/indivs dictionary formats
team = {
    "id" : "t0",
    "teamname" : "",
    "name0" : ""
}
indiv ={
     "id" : "i00",
     "name" : ""
}

#paths to folders
filepath = os.path.dirname(__file__)+r"\\"
logspath = os.path.join(filepath, "Logs")
teampath = os.path.join(filepath, "Teams")
indivpath = os.path.join(filepath, "Indivs")

#Make logs folder and get amount of logs
if not os.path.exists(logspath):
    os.mkdir(logspath)
for i in os.listdir(logspath):
     logs.append(i)

#makes teams and indivs folders
try:
    if not os.path.exists(teampath):
        os.mkdir(teampath)
    if not os.path.exists(indivpath):
        os.mkdir(indivpath)
except Exception as e:
    Error(e)

Log("Log " + str(len(logs)))
Log("Program Started")


#Create Tkinter window and set title + size
root = tk.Tk()
root.geometry("800x600")
root.title("Tournament Scoring System Version: "+ version)

#read from most recent team and indiv file
def read():
        Log("Read")
        teams = []
        indivs = []
        #get every json from the folder the file is in and all subfolders
        files = glob.glob(filepath + "**/*.json", recursive= True)

        #appends file to teams folder if it is a team folder
        for i in files:
            if i.find("team") != -1:
                teams.append(i)
            else:
                 indivs.append(i)
        #sort teams/individuals by the time that they were created and reverse it so it is descending
        teams.sort(key = lambda x: os.path.getctime(x), reverse = True)
        indivs.sort(key = lambda x: os.path.getctime(x), reverse = True)
        Log(indivs)
        Log(teams)
        Log(teams[0])
        Log(indivs[0])
        #open files and set teamdata and indivdata
        try:
            with open(teams[0], "r") as w:
                teamdata = json.load(w)
        except Exception as e:
            Error(e)
        Log(teamdata)
        try:
            with open(indivs[0], "r") as w:
                indivdata = json.load(w)
        except Exception as e:
            Error(e)
        Log(indivdata)
        return teamdata, indivdata



    
    
#Write Function called when a file needs to be written to
def write(c, first, name):
    #checks if this is the first time a file is being written (specified when calling function)
    if first == True:
        #checks if the file being written is a team or individual (again specified when calling)
        if c == "t":
            #create an empty file to read from when there are no team or individual files
            try:
                with open(os.path.join(teampath, "empty_team"+".json"), "w") as w:
                    json.dump(team, w)
                    w.close()
            except Exception as e:
                Error(e)
        else:
            try:
                with open(os.path.join(indivpath, "empty_indiv"+".json"), "w") as w:
                    json.dump(indiv, w)
                    w.close()
            except Exception as e:
                Error(e)

    else:
        #if this isn't the first write, check if team or indiv again
        if c == "t":
            #write to team file using team dictionary
            try:
                with open(os.path.join(teampath, "team "+ name+".json"), "w") as w:
                    json.dump(team, w)
                    w.close()


                #saved for later use on team/indiv creator 
                #mb.showwarning(title = "Invalid Name", message = "There is already a team with this name")
            except Exception as e:
                Error(e)
        else:
            #write to indiv file using indiv dict
            try:
                with open(os.path.join(indivpath, "indiv "+ name + ".json"), "w") as w:
                    json.dump(indiv, w)
                    w.close()
                    
                        #mb.showwarning(title = "Invalid Name", message = "There is already a participant with this name")
            except Exception as e:
                Error(e)
        

#if there is no team or indiv files makes blank teams and indivs
for i in os.listdir():
     if i.find("t") == -1:
        try:
            write("t", True, "Empty")
        except Exception as e:
            Error(e)
for i in os.listdir():
     if i.find("i") == -1:
        try:
            write("i", True, "Empty")
        except Exception as e:
            Error(e)

#Backend===================================================================================
#Frontend==================================================================================

teamdata, indivdata = read()
teams = int(teamdata["id"][1])
indivs1 = indivdata["id"][1]
indivs2 = indivdata["id"][2]
indivs = int(str(indivs1)+str(indivs2))
Log("Teams: "+str(teams))
Log("Indivs: "+str(indivs))




def create(c):
        #Set dictionaries and call write()
        def Set(c):
            global teams
            #Set 
            if c == "t":
                total = 0
                if person1.get() != "":
                    total +=1
                if person2.get() != "":
                    total +=1
                if person3.get() != "":
                    total +=1
                if person4.get() != "":
                    total +=1
                if person5.get() != "":
                    total +=1
                if nameent.get() != "":
                    if total >= 2:
                        teams +=1
                        team["id"] = "t"+str(teams)
                        team["teamname"] =  nameent.get()
                        team["name0"] = person1.get()
                        team["name1"] = person2.get()
                        team["name2"] = person3.get()
                        team["name3"] = person4.get()
                        team["name4"] = person5.get()
                        try: 
                            write("t", False, nameent.get())
                        except Exception as e:
                            Error(e)
                        Log("Team Created, Teams: "+str(teams))
                        createwin.destroy()
                        return teams

                    else:
                        mb.showwarning(title = "Invalid team", message = "A team must contain at least two people")
                else:
                    mb.showwarning(title = "Invalid team", message = "Your team needs a name!")
                
                
                


            else:
                global indivs
                if namei.get() != "":
                    indivs+=1
                    if indivs < 10:
                        indiv["id"] = "i"+str(str(0)+str(indivs))
                    else:
                        indiv["id"] = "i"+str(indivs)
                    indiv["name"] = namei.get()
                    try:
                        write("i", False, namei.get())
                    except Exception as e:
                        Error(e)
                    Log("Individual Created, Indivs: "+str(indivs))
                    createwin.destroy()
                    return indivs
                else:
                    mb.showwarning(title = "Invalid individual", message = "Name required!")
                
            
        createwin = tk.Toplevel(root)
        createwin.geometry("400x600")
        if c == "t":
            #Check if there are 4 teams if so tell user they cant enter
            if teams == 4:
                if mb.showwarning(message="Sorry we already have enough Teams", title="Team limit reached"):
                    createwin.destroy()
            else:
                #otherwise make buttons for making a team
                createwin.title("Create a team")
                addlab = ttk.Label(createwin, text = "Create a Team, (names can be left empty)")
                addlab.pack()
                name = ttk.Label(createwin, text = "Input a name for your team")
                name.pack()
                nameent = ttk.Entry(createwin)
                nameent.pack()


                #Make a frame for holding entries for entering names.
                names = tk.Frame(createwin)
                names.pack(pady = 20)
                person1l = ttk.Label(names,text = "Person 1")
                person1l.pack()
                person1 = ttk.Entry(names)
                person1.pack()
                person2l = ttk.Label(names,text = "Person 2")
                person2l.pack()
                person2 = ttk.Entry(names)
                person2.pack()
                person3l = ttk.Label(names,text = "Person 3")
                person3l.pack()
                person3 = ttk.Entry(names)
                person3.pack()
                person4l = ttk.Label(names,text = "Person 4")
                person4l.pack()
                person4 = ttk.Entry(names)
                person4.pack()
                person5l = ttk.Label(names,text = "Person 5")
                person5l.pack()
                person5 = ttk.Entry(names)
                person5.pack()
                #button for making the team
                add = ttk.Button(names, text = "Create Team", command = lambda: Set("t"))
                add.pack(pady = 10)


        
        else:
            #Check if there are already 20 individuals and if so tell the user they cant enter and close creation window
            if indivs == 20:
                if mb.showwarning(message="Sorry we already have enough Individuals", title = "Individual limit reached"):
                    createwin.destroy()
            else:
                #if there are slots left create buttons/labels for creating an individual
                createwin.title("Create an individual")
                nameil = ttk.Label(createwin, text= "What is your name?")
                nameil.pack()
                namei = ttk.Entry(createwin)
                namei.pack()
                addi = ttk.Button(createwin, text = "Create Individual", command = lambda: Set("i"))
                addi.pack(pady = 10)

        


    


#Title of main window
lab =  ttk.Label(text = "Tournament Scoring System", font = ("Segoe UI", 16))
lab.pack(pady = 10)

#Creates a frame for teams and indivs that lists/buttons are put in
indivframe = tk.Frame()
indivframe.pack()
teamframe = tk.Frame()
teamframe.pack()
#labels for amount of individuals/teams
amt = ttk.Label(indivframe, text = "Individuals: "+ str(indivs) + "\nTeams: "+ str(teams))
amt.pack()
#Buttons for making teams/individuals
indivbutt =  ttk.Button(indivframe, text = "Create an Individual", command = lambda: create("i"))
indivbutt.pack()
teambutt = ttk.Button(teamframe, text = "Create a Team", command = lambda: create("t"))
teambutt.pack()

teamsf = ttk.Frame()
teamsf.pack(anchor="n", side = "left")

indivsf = ttk.Frame()
indivsf.pack(anchor="n", side = "right")

teamslab = ttk.Label(teamsf, text = "Teams:")
teamslab.pack(padx = 50)
indivlab = ttk.Label(indivsf, text = "Individuals:")
indivlab.pack(padx = 50)


ifiles = []
tfiles = []
ibutts = []
tbutts = []
def update():
    global teams, indivs
    first = True
    firstthread = True
    #There's definitely a better way of doing this like checking for changes in the directory but i cba
    def editpressed(x):
        def edit(c):
            #overwriting the file
            def overwrite(c):
                Log("overwrite "+x)
                if c == "t":
                    try:
                        with open(os.path.join(teampath, x), "w") as w:
                            json.dump(team, w)
                            w.close()
                    except Exception as e:
                        Error(e)
                    else:
                        with open(os.path.join(teampath, x), "w") as w:
                            json.dump(team, w)
                            w.close()
                        editwindow.destroy()

                else:
                    try:
                        with open(os.path.join(indivpath, x), "w") as w:
                            json.dump(indiv, w)
                            w.close()
                    except Exception as e:
                        Error(e)
                    else:
                        with open(os.path.join(indivpath, x), "w") as w:
                            json.dump(indiv, w)
                            w.close()
                        editwindow.destroy()



            if c == "t":
                total = 0
                if person1.get() != "":
                    total +=1
                if person2.get() != "":
                    total +=1
                if person3.get() != "":
                    total +=1
                if person4.get() != "":
                    total +=1
                if person5.get() != "":
                    total +=1
                if nameent.get() != "":

                    if total >= 2:
                        team["teamname"] =  nameent.get()
                        team["name0"] = person1.get()
                        team["name1"] = person2.get()
                        team["name2"] = person3.get()
                        team["name3"] = person4.get()
                        team["name4"] = person5.get()
                        try:
                            overwrite("t")
                        except Exception as e:
                            Error(e)
                        Log("Team Edited: "+x)
                        editwindow.destroy
                    else:
                        mb.showwarning(title = "Invalid team", message = "A team must contain at least two people!")
                else:
                    mb.showwarning(title = "Invalid team", message = "Your team needs a name!")

            if c == "i":
                if namei.get() != "":
                    indiv["name"] = namei.get()
                    try:
                        overwrite("i")
                    except Exception as e:
                        Error(e)
                    Log("Indiv Edited: "+x)
                    editwindow.destroy()
                else:
                    mb.showwarning(title = "Invalid individual", message = "Name required!")


        # used for deleting files
        def dele():
            #asks the user if they if they are sure they want to delete
            if mb.askyesno(message = "Are you sure you want to delete: "+ str(x), title = "Delete File"):
                #checks if the file being deleted is a team or individual
                if str(x).startswith("t"):
                    #deletes file and closes window
                    try:
                        os.remove(os.path.join(teampath, x))
                        editwindow.destroy()
                    except Exception as e:
                        Error(e)
                if str(x).startswith("i"):
                    #deletes file and closes window
                    try:
                        os.remove(os.path.join(indivpath, x))
                        editwindow.destroy()
                    except Exception as e:
                       Error(e)

        #create Editing window and sets title/size
        editwindow = tk.Toplevel(root)
        editwindow.geometry("400x600")
        #create Delete Button/title for file being deleted
        delete = ttk.Button(editwindow, text = "Delete", command = lambda x = x : dele())
        delete.pack(anchor = "nw", side="top")
        
        
        if str(x).startswith("t"):
            with open(os.path.join(teampath, x), "r") as r:
                teamname = json.load(r)["teamname"]
            xlab = ttk.Label(editwindow, text = "editing " + teamname + "; " + x)
            xlab.pack()
            #open file we are editing to get names out of it.
            try:
                with open(os.path.join(teampath, x), "r") as r:
                    data = json.load(r)  
                    r.close()
            except Exception as e:
                #My own function for outputting and logging error I know realise I could've just used the Log function but oh well
                Error(e)
            
            editwindow.title("Edit a team")
            #Add Buttons for editing team
            addlab = ttk.Label(editwindow, text = "Edit a Team, (names can be left empty)")
            addlab.pack()
            name = ttk.Label(editwindow, text = "Input a name for your team")
            name.pack()
            nameent = ttk.Entry(editwindow)
            nameent.pack()
            names = tk.Frame(editwindow)
            names.pack(pady = 20)
            person1l = ttk.Label(names,text = "Person 1")
            person1l.pack()
            person1 = ttk.Entry(names)
            person1.pack()
            person2l = ttk.Label(names,text = "Person 2")
            person2l.pack()
            person2 = ttk.Entry(names)
            person2.pack()
            person3l = ttk.Label(names,text = "Person 3")
            person3l.pack()
            person3 = ttk.Entry(names)
            person3.pack()
            person4l = ttk.Label(names,text = "Person 4")
            person4l.pack()
            person4 = ttk.Entry(names)
            person4.pack()
            person5l = ttk.Label(names,text = "Person 5")
            person5l.pack()
            person5 = ttk.Entry(names)
            person5.pack()
            nameent.insert(0,data["teamname"])
            person1.insert(0,data["name0"])
            person2.insert(0,data["name1"])
            person3.insert(0,data["name2"])
            person4.insert(0,data["name3"])
            person5.insert(0,data["name4"])
            add = ttk.Button(names, text = "Save Edits?", command = lambda: edit("t"))
            add.pack(pady = 10)

        if str(x).startswith("i"):
            with open(os.path.join(indivpath, x), "r") as r:
                name = json.load(r)["name"]
            xlab = ttk.Label(editwindow, text = "editing " + name + "; " + x)
            xlab.pack()
            with open(os.path.join(indivpath, x), "r") as r:
                data = json.load(r)
                r.close()
            editwindow.title("Edit an individual")
            nameil = ttk.Label(editwindow, text= "What is your name?")
            nameil.pack()
            namei = ttk.Entry(editwindow)
            namei.pack()
            addi = ttk.Button(editwindow, text = "Save Edits", command = lambda: edit("i"))
            addi.pack(pady = 10)
            namei.insert(0, data["name"])


    #checks if update sub-threads are running and if they are join them back to the main thread.
    while True:
        if firstthread != True:
            t1.join()
            t2.join()
        
        #Updates Teams List by making a new thread so that each list updates at the same time.
        def updateteams(thread):
            global tbutts, tfiles
            #delete all team buttons
            for i in tbutts:
                i.pack_forget()
            #for every file in the list of team files if the file exists open it and create a button for the file with the teamname of the team
            for i in tfiles:
                if os.path.exists(os.path.join(teampath, i)):
                    with open(os.path.join(teampath, i), "r") as r:
                        data = json.load(r)
                        r.close()
                    name = data["teamname"]
                    tbutts.append(ttk.Button(teamsf, text = name, command = lambda x = i: editpressed(x)))
                    tbutts[-1].pack()
                else:
                    tfiles.remove(i)
            Log("Thread: "+str(thread)+" Updated: "+str(tfiles))
            return tbutts, tfiles
        #Updates Individuals List by making a new thread so that each list updates at the same time.
        def updateindivs(thread):
            global ibutts, ifiles
            #delete all individual buttons
            for i in ibutts:
                i.pack_forget()
            #for every file in the list of individual files if the file exists open it and create a button for the file with the name of the individual
            for i in ifiles:
                if os.path.exists(os.path.join(indivpath, i)):
                    with open(os.path.join(indivpath, i), "r") as r:
                        data = json.load(r)
                        r.close()
                    name = data["name"]
                    ibutts.append(ttk.Button(indivsf, text = name, command = lambda x = i: editpressed(x)))
                    ibutts[-1].pack()
                else:
                    ifiles.remove(i)

            Log("Thread: "+str(thread)+" Updated: "+str(ifiles))
            return ibutts, ifiles

        teams = len(tfiles)
        indivs = len(ifiles)
        amt.config(text = "Individuals: "+ str(len(ifiles)) + "\nTeams: "+ str(len(tfiles)))

        #Gets a list of every indiv/team file
        for i in os.listdir(indivpath):
            if i.find("empty") == -1:
                if str(ifiles).find(i) == -1:
                    ifiles.append(i)


        for i in os.listdir(teampath):
            if i.find("empty") == -1:
                if str(tfiles).find(i) == -1:
                    tfiles.append(i)


        # Starts Team and Update List Update Threads
        try:
            t1 = threading.Thread(name = "Team Worker Update Sub-Thread", daemon= True, target = lambda: updateteams(t1))
            t1.start()
            t2 = threading.Thread(name = "Indiv Worker Update Sub-Thread", daemon= True, target = lambda: updateindivs(t2))
            t2.start()
            firstthread = False
        except Exception as e:
            Error(e)
        

        
        
        #Checks for missing Folders
        if first == False:
            if(not os.path.exists(teampath)):
                Error("Team Folder Missing!")
            if(not os.path.exists(indivpath)):
                Error("Indiv Folder Missing!")
        time.sleep(3)
        first = False


        
#Starts update main thread
t1 = threading.Thread(target=update, daemon = True, name = "Update Worker Thread")
t1.start()


                

def on_closing():
    if mb.askyesno(title = "Quitting", message= "Are you sure you want to quit?"):
        Log("Closing")
        #close log file
        f.close()
        #close window and quit
        root.destroy()
        root.quit()
        quit(0)

# checks for closing the window and runs on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
#Frontend==================================================================================