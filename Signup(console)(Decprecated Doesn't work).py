import glob
import json
import os
from getpass import getpass
import subprocess
import sys
import time
color = False
usingcol = True
#https://github.com/ItBePhill/Challenge-3--I-guess-
#used for data that is read from json files
teamdata = {

}
indivdata = {

}
teams = 0
individuals = 0
tori = ""
members = 1
#path to the parent directory of folders
jsonpath = os.path.dirname(__file__)+"\\"
#dictionaries for writing to team and indiv json files
team = {
    "id" : "t0",
    "name0": "",
    "name1" : "",
    "name2" : "",
    "name3" : "",
    "name4" : ""
}
individual = {
    "id" : "i0",
    "name" : ""
}
if os.path.exists(jsonpath+"teams\\") != True:
    os.mkdir(jsonpath+"teams\\")

if os.path.exists(jsonpath+"indivs\\") != True:
    os.mkdir(jsonpath+"indivs\\")

def teamjsonwrite():
    with open(jsonpath+"teams\\"+"team"+str(teams)+".json", "w") as f:
        json.dump(team, f, indent=1)
        f.close

def indivjsonwrite():
    with open(jsonpath+"indivs\\"+"indiv"+str(individuals)+".json", "w") as f:
        json.dump(individual, f, indent=1)
        f.close
def read():
    teams = []
    indivs = []
    #gets a list of every json file in the jsonpath directory
    files = glob.glob(jsonpath + r"**\*.json", recursive= True)
    #loops through each file from glob to check if it is a team or indiv file and append to respective lists
    for i in files:
        if os.path.splitext(os.path.basename(i))[0].find("team") != -1:
            teams.append(i)
        else:
            indivs.append(i)
    #sort file lists into order of time created and reverse order so it is descending
    teams.sort(key=lambda x: os.path.getctime(x))
    teams.reverse()
    indivs.sort(key=lambda x: os.path.getctime(x))
    indivs.reverse()
    #read from the most recent file and return the result
    with open(teams[0], "r") as f:
        team = json.load(f)
    with open(indivs[0], "r") as f:
        indiv = json.load(f)
    return team, indiv


#Checks for Team file, if file doesn't exist makes default file with 0 members and with an id of 0
if os.path.exists(jsonpath+"team/"+"/team0.json") == False:
    teamjsonwrite()
#Calls read() and assigns result to teamdata
else:
    teamdata, indivdata = read()
    teams = int(str(teamdata["id"])[1])
    individuals = int(str(indivdata["id"])[1])
#Checks for Indiv file, if file doesn't exist makes default file with 0 members and with an id of 0
if os.path.exists(jsonpath+"indivs/"+"/indiv0.json") == False:
    indivjsonwrite()
#Calls read() and assigns result to indivdata
else:
    #gets amount of teams and individuals from json files
    teamdata, indivdata = read()
    teams = int(str(teamdata["id"])[1])
    individuals = int(str(indivdata["id"])[1])
#for installing required package(colorama)------------------------------------------------------------
try:
    import colorama
except:
    inst = ""
    while inst != "y" and inst != "n" and inst != "yn":
        inst = input("Would you like to install required package(colorama)\nY = yes\nN = no(program may not work as intended)\nyn = install but uninstall when program is closed(you will have to reinstall when running Events)\n-").lower()
        if inst != "y" and inst != "n" and inst != "yn":
            print("Error: Invalid Entry")
        elif inst == "yn":
            usingcol = True
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
            print("")
            color = True
            import colorama
        elif inst == "y":
            usingcol = True
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
            print("")
            import colorama
        elif inst == "n":
            print("")
            usingcol = False
            break
        pass
else:
    import colorama

def uninstall():
    if color == True:
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'colorama'])
#------------------------------------------------------------------------------------------------------------------
#Checks if you are using colour or not aka colorama is or isn't installed (this is the only way i know of doing this other than an if statement for each print)
if(usingcol):
    #Menu Code (Colour)
    while tori != "t" and tori != "i":
        print(colorama.Fore.WHITE+"Main Menu----------------------------------------------------------------------------------------------")
        tori = input(colorama.Fore.WHITE+"Teams: "+str(teams)+ "/4 Individuals: "+ str(individuals)+"/20 \nWill you be in a team or individual.\nT - Team.\nI - Individual.\nB - Close\n-").lower()
        print("")
        #Team
        if(tori == "t"):
            if teams == 4:
                print(colorama.Fore.RED+"Sorry we already have enough teams, But you can enter as an individual.")
                tori = ""
                print(colorama.Fore.WHITE+"")
            else:
                members = 1
                print(colorama.Fore.WHITE+"Enter as a Team----------------------------------------------------------------------------------------------------")
                print(colorama.Fore.WHITE+"You may have a maximum of 5 people in your team\nif you are done inputting names Type B on the next name to finish")
                ans = ""
                while members < 6 and ans != "B" and ans != "b":
                    ans = input(colorama.Fore.WHITE+"Name: "+str(members)+"\n-")
                    if ans != "B" and ans != "b":
                        members+=1
                        team["name"+str(members-2)] = ans
                    else:
                        if members < 3:
                            Con = ""
                            while Con != "y" and Con != "n":
                                Con = input(colorama.Fore.YELLOW+"Are you sure you want to continue, It will be better for you to enter as an individual\nY= Continue\nN= Return to main menu\n-").lower()
                                if Con == "n":
                                    tori = ""
                                    members = 1
                                    print("")
                                else:
                                    teams += 1
                                    team["id"] = "t"+str(teams)
                                    teamjsonwrite()
                                    print(colorama.Fore.GREEN+"Successfully entered!")
                                    getpass(colorama.Fore.WHITE+"Your Teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                                    con = ""
                                    while con != "y" and con != "n":
                                        con = input(colorama.Fore.WHITE+"Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                                        if con != "y" and con != "n":
                                            print(colorama.Fore.RED+"Error: Invalid Entry")
                                        else:
                                            if con == "y":
                                                uninstall()
                                                time.sleep(1)
                                                import Events
                                            else:
                                                uninstall()
                                                quit()
                                    
                        elif members >= 2:
                            teams += 1
                            team["id"] = "t"+str(teams)
                            teamjsonwrite()
                            print(colorama.Fore.GREEN+"Successfully entered!")
                            getpass(colorama.Fore.WHITE+"Your Teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                            con = ""
                            while con != "y" and con != "n":
                                con = input(colorama.Fore.WHITE+"Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                                if con != "y" and con != "n":
                                    print(colorama.Fore.RED+"Error: Invalid Entry")
                                else:
                                    if con == "y":
                                        uninstall()
                                        time.sleep(1)
                                        import Events
                                    else:
                                        uninstall()
                                        quit()
                    if members == 6:
                        teams += 1
                        team["id"] = "t"+str(teams)
                        teamjsonwrite()
                        print(colorama.Fore.GREEN+"Successfully entered!")
                        getpass(colorama.Fore.WHITE+"Your teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                        con = ""
                        while con != "y" and con != "n":
                            con = input(colorama.Fore.WHITE+"Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                            if con != "y" and con != "n":
                                print(colorama.Fore.RED+"Error: Invalid Entry")
                            else:
                                if con == "y":
                                    uninstall()
                                    time.sleep(1)
                                    import Events
                
                                else:
                                    uninstall()
                                    quit()
                        
                        

                
                                    
                    
        #Individual
        elif(tori == "i"):
            ans = ""
            print(colorama.Fore.WHITE+"Enter as  an Individual---------------------------------------------------------------------------------------------")
            if individuals == 20:
                print(colorama.Fore.RED+"Sorry we already have enough teams, But you can enter as an individual.")
                tori = ""
            else:
                ans = input(colorama.Fore.WHITE+"Input a name\nOr type B to quit to main menu\n-")
                if ans != "B" and ans != "b":
                    individual["name"] = ans
                    individuals += 1
                    individual["id"] = "i"+str(individuals)
                    indivjsonwrite()
                    print(colorama.Fore.GREEN+"Successfully entered!")
                    getpass(colorama.Fore.WHITE+"Your ID is i"+str(individuals)+" write it down somewhere as you will need it later, press enter to continue")

                    con = ""
                    while con != "y" and con != "n":
                        con = input(colorama.Fore.WHITE+"Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                        if con != "y" and con != "n":
                            print(colorama.Fore.RED+"Error: Invalid Entry")
                        else:
                            if con == "y":
                                uninstall()
                                time.sleep(1)
                                import Events
                            else:
                                uninstall()
                                quit()
                else:
                    tori = ""
                    print("")
        elif(tori == "b"):
            uninstall()
            quit()
        else:
            print(colorama.Fore.RED+"Error: Invalid Entry")

            
else:
    #Menu Code (No Colour)
    while tori != "t" and tori != "i":
        print("Main Menu----------------------------------------------------------------------------------------------")
        tori = input("Teams: "+str(teams)+ "/4 Individuals: "+ str(individuals)+"/20 \nWill you be in a team or individual.\nT - Team.\nI - Individual.\nB - Close\n-").lower()
        print("")
        #Team
        if(tori == "t"):
            if teams == 4:
                print("Sorry we already have enough teams, But you can enter as an individual.")
                tori = ""
                print("")
            else:
                members = 1
                print("Enter as a Team----------------------------------------------------------------------------------------------------")
                print("You may have a maximum of 5 people in your team\nif you are done inputting names Type B on the next name to finish")
                ans = ""
                while members < 6 and ans != "B" and ans != "b":
                    ans = input("Name: "+str(members)+"\n-")
                    if ans != "B" and ans != "b":
                        members+=1
                        team["name"+str(members-2)] = ans
                    else:
                        if members < 3:
                            Con = ""
                            while Con != "y" and Con != "n":
                                Con = input("Are you sure you want to continue, It will be better for you to enter as an individual\nY= Continue\nN= Return to main menu\n-").lower()
                                if Con == "n":
                                    tori = ""
                                    members = 1
                                    print("")
                                else:
                                    teams += 1
                                    team["id"] = "t"+str(teams)
                                    teamjsonwrite()
                                    print("Successfully entered!")
                                    getpass("Your Teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                                    con = ""
                                    while con != "y" and con != "n":
                                        con = input("Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                                        if con != "y" and con != "n":
                                            print("Error: Invalid Entry")
                                        else:
                                            if con == "y":
                                                import Events
                                            else:
                                                quit()
                                    
                        elif members >= 2:
                            teams += 1
                            team["id"] = "t"+str(teams)
                            teamjsonwrite()
                            print("Successfully entered!")
                            getpass("Your Teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                            con = ""
                            while con != "y" and con != "n":
                                con = input("Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                                if con != "y" and con != "n":
                                    print("Error: Invalid Entry")
                                else:
                                    if con == "y":
                                        import Events
                                    else:
                                        quit()
                    if members == 6:
                        teams += 1
                        team["id"] = "t"+str(teams)
                        teamjsonwrite()
                        print("Successfully entered!")
                        getpass("Your teams ID is t"+str(teams)+" write it down somewhere as you will need it later, press enter to continue")
                        con = ""
                        while con != "y" and con != "n":
                            con = input("Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                            if con != "y" and con != "n":
                                print("Error: Invalid Entry")
                            else:
                                if con == "y":
                                    import Events
                
                                else:
                                    quit()
                        
                        

                
                                    
                    
        #Individual
        elif(tori == "i"):
            ans = ""
            print("Enter as  an Individual---------------------------------------------------------------------------------------------")
            if individuals == 20:
                print("Sorry we already have enough teams, But you can enter as an individual.")
                tori = ""
            else:
                ans = input("Input a name\nOr type B to quit to main menu\n-")
                if ans != "B" and ans != "b":
                    individual["name"] = ans
                    individuals += 1
                    individual["id"] = "i"+str(individuals)
                    indivjsonwrite()
                    print("Successfully entered!")
                    getpass("Your ID is i"+str(individuals)+" write it down somewhere as you will need it later, press enter to continue")

                    con = ""
                    while con != "y" and con != "n":
                        con = input("Would you like to continue to the Events?\nY = Yes\nN = No\n-").lower()
                        if con != "y" and con != "n":
                            print("Error: Invalid Entry")
                        else:
                            if con == "y":
                                uninstall()
                                import Events
                            else:
                                uninstall()
                                quit()
                else:
                    tori = ""
                    print("")
        elif(tori == "b"):
            uninstall()
            quit()
        else:
            print("Error: Invalid Entry")