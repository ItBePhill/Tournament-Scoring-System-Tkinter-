import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import os
import glob
import datetime
import json
import threading
#Backend===================================================================================
logs = []
version = "0.0"
teams = 0
indivs = 0
def Log(ob):
    global f
    now = datetime.datetime.now()
    ob = str(ob)
    final = "\n\n"+now.strftime("%Y-%m-%d %H:%M:%S") + ": " + ob
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

#Make logs and get amount of logs
if not os.path.exists(logspath):
    os.mkdir(logspath)
for i in os.listdir(logspath):
     logs.append(i)
#makes teams and indivs folders
if not os.path.exists(teampath):
    os.mkdir(teampath)
if not os.path.exists(indivpath):
    os.mkdir(indivpath)
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
Log("Started")

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
            createwin.title("Create an individual")
            nameil = ttk.Label(createwin, text= "What is your name?")
            nameil.pack()
            namei = ttk.Entry(createwin)
            namei.pack()
            addi = ttk.Button(createwin, text = "Create Individual", command = lambda: Set("i"))
            addi.pack(pady = 10)


    



lab =  ttk.Label(text = "Tournament Scoring System", font = ("Segoe UI", 16))
lab.pack(pady = 10)
indivbutt =  ttk.Button(text = "Create an Individual", command = lambda : create("i"))
indivbutt.pack()
teambutt = ttk.Button(text = "Create a Team", command = lambda : create("t"))
teambutt.pack()

teamsf = ttk.Frame()
teamsf.pack(anchor="n", side = "left")
indivsf = ttk.Frame()
indivsf.pack(anchor="n", side = "right")

teamslab = ttk.Label(teamsf, text = "Teams:")
teamslab.pack(padx = 50)
indivlab = ttk.Label(indivsf, text = "Individuals:")
indivlab.pack(padx = 50)

tbutts = []
tfile = []
ibutts = []
ifile = []

for i in os.listdir(teampath):
    if i.find("empty_team.json") == -1:
        with open(os.path.join(teampath,i), "r") as teamf:
            name = json.load(teamf)["teamname"]
            teamf.close()
        tfile.append(i)
        tbutts.append(ttk.Button(teamsf, text = name))
        tbutts[-1].pack(padx = 50)

for i in os.listdir(indivpath):
    if i.find("empty_indiv.json") == -1:
        with open(os.path.join(indivpath,i), "r") as indivf:
            name = json.load(indivf)["name"]
            teamf.close()
        ifile.append(i)
        ibutts.append(ttk.Button(indivsf, text = name))
        ibutts[-1].pack(padx = 50)


def update():
    Log("updated")
    for i in os.listdir(filepath):
        if i != "empty_team.json":
            for i in ibutts:
                i.pack_forget()
                
    threading.Timer(5, update).start()
                

    
update()

def on_closing():
    Log("Closing")
    #close log file
    f.close()
    #close window and quit
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
#Frontend==================================================================================