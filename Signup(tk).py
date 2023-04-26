import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import os
import glob
import datetime
import json
import threading
import time
#Backend===================================================================================
logs = []
version = "0.1"
teams = 0
indivs = 0
def Log(ob):
    global f
    now = datetime.datetime.now()
    ob = str(ob)
    final = "\n\n["+now.strftime("%Y-%m-%d %H:%M:%S") + "]: " + ob
    print(final)
    with open(os.path.join(os.getcwd(), "Logs", str(len(logs)))+ " " +now.strftime("%Y-%m-%d")+ " log.txt" , "a") as f:
        f.write(final)
    return f
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
if not os.path.exists(teampath):
    os.mkdir(teampath)
if not os.path.exists(indivpath):
    os.mkdir(indivpath)
Log("Log " + str(len(logs)))
Log("Program Started Successfully!")
#Create Tkinter window and set title + size
root = tk.Tk()
root.geometry("800x600")
root.title("Tournament Scoring System Version: "+ version)
#read from most recent team and indiv file
def read():
        Log("Read")
        teams = []
        indivs = []
        #read from team
        files = glob.glob(filepath + "**/*.json", recursive= True)

        for i in files:
            if i.find("team") != -1:
                teams.append(i)
            else:
                 indivs.append(i)
        teams.sort(key = lambda x: os.path.getctime(x), reverse = True)
        indivs.sort(key = lambda x: os.path.getctime(x), reverse = True)
        Log(indivs)
        Log(teams)
        Log(teams[0])
        Log(indivs[0])
        with open(teams[0], "r") as w:
            teamdata = json.load(w)
        Log(teamdata)
        with open(indivs[0], "r") as w:
            indivdata = json.load(w)
        Log(indivdata)
        return teamdata, indivdata



    
    

def write(c, first):
    if first == True:
        if c == "t":

            with open(os.path.join(teampath, "empty_team"+".json"), "w") as w:
                json.dump(team, w)
                w.close()
        else:

            with open(os.path.join(indivpath, "empty_indiv"+".json"), "w") as w:
                json.dump(indiv, w)
                w.close()

    else:
        if c == "t":
            with open(os.path.join(teampath, "team "+str(teams)+".json"), "w") as w:
                json.dump(team, w)
                w.close()
        else:
            with open(os.path.join(indivpath, "indiv "+str(indivs)+".json"), "w") as w:
                json.dump(indiv, w)
                w.close()
        

#if there is no team or indiv files makes blank teams and indivs
for i in os.listdir():
     if i.find("t") == -1:
        write("t", True)
for i in os.listdir():
     if i.find("i") == -1:
        write("i", True)

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
            if c == "t":
                global teams
                teams +=1
                team["id"] = "t"+str(teams)
                team["teamname"] =  nameent.get()
                team["name0"] = person1.get()
                team["name1"] = person2.get()
                team["name2"] = person3.get()
                team["name3"] = person4.get()
                team["name4"] = person5.get()
                write("t", False)
                Log("Team Created, Teams: "+str(teams))
                createwin.destroy()
                return teams
            else:
                global indivs
                indivs+=1
                if indivs < 10:
                    indiv["id"] = "i"+str(str(0)+str(indivs))
                else:
                    indiv["id"] = "i"+str(indivs)
                indiv["name"] = namei.get()
                write("i", False)
                Log("Individual Created, Indivs: "+str(indivs))
                createwin.destroy()
                return indivs
            
        createwin = tk.Toplevel(root)
        createwin.geometry("400x600")
        if c == "t":
            if teams == 4:
                if mb.showwarning(message="Sorry we already have enough Teams", title="Team limit reached"):
                    createwin.destroy()
            else:
                createwin.title("Create a team")
                addlab = ttk.Label(createwin, text = "Create a Team, (names can be left empty)")
                addlab.pack()
                name = ttk.Label(createwin, text = "Input a name for your team")
                name.pack()
                nameent = ttk.Entry(createwin)
                nameent.pack()

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
                add = ttk.Button(names, text = "Create Team", command = lambda: Set("t"))
                add.pack(pady = 10)


        
        else:
            if indivs == 20:
                if mb.showwarning(message="Sorry we already have enough Individuals", title = "Individual limit reached"):
                    createwin.destroy()
            else:
                createwin.title("Create an individual")
                nameil = ttk.Label(createwin, text= "What is your name?")
                nameil.pack()
                namei = ttk.Entry(createwin)
                namei.pack()
                addi = ttk.Button(createwin, text = "Create Individual", command = lambda: Set("i"))
                addi.pack(pady = 10)

        


    



lab =  ttk.Label(text = "Tournament Scoring System", font = ("Segoe UI", 16))
lab.pack(pady = 10)


indivframe = tk.Frame()
indivframe.pack()
teamframe = tk.Frame()
teamframe.pack()
amt = ttk.Label(indivframe, text = "Individuals: "+ str(indivs) + "\nTeams: "+ str(teams))
amt.pack()
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
    first = True
    firstthread = True
    #There's definitely a better way of doing this like checking for changes in the directory but i cba
    def editpressed(x):
        def edit(c):
            def overwrite():
                Log("overwrite "+x)
                try:
                    with open(os.path.join(teampath, x), "w") as w:
                        json.dump(team, w)
                        w.close()
                except Exception as e:
                    Log(e)
                    quit(0)
                else:
                    with open(os.path.join(teampath, x), "w") as w:
                        json.dump(team, w)
                        w.close()
                    editwindow.destroy()


            if c == "t":
                global teams
                team["teamname"] =  nameent.get()
                team["name0"] = person1.get()
                team["name1"] = person2.get()
                team["name2"] = person3.get()
                team["name3"] = person4.get()
                team["name4"] = person5.get()
                overwrite()
                Log("Team Edited: "+x)
                editwindow.destroy
                return teams
        
            
        def dele():
            if mb.askyesno(message = "Are you sure you want to delete: "+ str(x), title = "Delete File"):
                if str(x).startswith("t"):
                    os.remove(os.path.join(teampath, x))
                    editwindow.destroy()
                if str(x).startswith("i"):
                    os.remove(os.path.join(indivpath, x))
                    editwindow.destroy()
        
        editwindow = tk.Toplevel(root)
        editwindow.geometry("400x300")
        delete = ttk.Button(editwindow, text = "Delete", command = lambda x = x : dele())
        delete.pack(anchor = "nw", side="top")
        xlab = ttk.Label(editwindow, text = "editing " + x)
        xlab.pack()
        if str(x).startswith("t"):
            with open(os.path.join(teampath, x), "r") as r:
                data = json.load()
                r.close()
            editwindow.title("Edit a team")
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
            add = ttk.Button(names, text = "Save Edits?", command = lambda: edit("t"))
            add.pack(pady = 10)



    while True:
        if firstthread != True:
            t1.join()
            t2.join()
        def updateteams(thread):
            global tbutts, tfiles
            Log("Teams")
            for i in tbutts:
                i.pack_forget()
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
        def updateindivs(thread):
            global ibutts, ifiles
            Log("Indivs")
            for i in ibutts:
                i.pack_forget()
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

        amt.config(text = "Individuals: "+ str(indivs) + "\nTeams: "+ str(teams))

        for i in os.listdir(indivpath):
            if i.find("empty") == -1:
                if str(ifiles).find(i) == -1:
                    ifiles.append(i)
                    
        for i in os.listdir(teampath):
            if i.find("empty") == -1:
                if str(tfiles).find(i) == -1:
                    tfiles.append(i)

        t1 = threading.Thread(name = "Team Worker Update Sub-Thread", daemon= True, target = lambda: updateteams(t1))
        t1.start()
        t2 = threading.Thread(name = "Indiv Worker Update Sub-Thread", daemon= True, target = lambda: updateindivs(t2))
        t2.start()
        firstthread = False
        

        
            
            



        Log("Updated")
        time.sleep(3)
        first = False
t1 = threading.Thread(target=update, daemon = True, name = "Update Worker Thread")
t1.start()


                

def on_closing():
    Log("Closing")
    #close log file
    f.close()
    #close window and quit
    root.destroy()
    root.quit()
    quit(0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
#Frontend==================================================================================