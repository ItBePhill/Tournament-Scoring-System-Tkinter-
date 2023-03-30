import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
teams = 0
indivs = 0
team = {
    "id" : "t0",
    "name0" : ""
}
indiv ={
     "id" : "i0",
     "name" : ""
}
butts = []
root = tk.Tk()
root.geometry("800x600")
root.title("Tournament Scoring System")
s = ttk.Style()
def create(c):
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
            
            add = ttk.Button(names, text = "Create Team")
            add.pack(pady = 10)
        else:
            createwin.title("Create an individual")

    



lab =  ttk.Label(text = "Tournament Scoring System")
lab.pack()
indivbutt =  ttk.Button(text = "Create an Individual", command = lambda : create("i"))
indivbutt.pack()
teambutt = ttk.Button(text = "Create a Team", command = lambda : create("t"))
teambutt.pack()

root.mainloop()