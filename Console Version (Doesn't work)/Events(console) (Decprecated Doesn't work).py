import json
import glob
import os
import sys
import subprocess
jsonpath = os.path.dirname(__file__)+"\\"
files = glob.glob(jsonpath + r"**\*.json", recursive= True)
ans = "  "
color = False
usingcol = True
filestring = ""
place = ""
jsondata = {

}
events = {
    "TS1" : "Hi"
}
#for installing required package(colorama)------------------------------------------------------------
try:
    import colorama
except ImportError:
    inst = ""
    while inst != "y" and inst != "n" and inst != "yn":
        inst = input("Would you like to install required package(colorama)\nY = yes\nN = no(program may not work as intended)\nyn = install but uninstall when program is closed(you will have to reinstall when running Events)\n-").lower()
        if inst != "y" and inst != "n" and inst != "yn":
            print("Error: Invalid Entry")
        elif inst == "yn":
            usingcol = True
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
            color = True
            import colorama
            print("")
        elif inst == "y":
            usingcol = True
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
            import colorama
            print("")

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
#for installing required package(colorama)------------------------------------------------------------

if (usingcol):
#Check for file--------------------------------------------------------------------------------------------
    if len(files) < 3:
        print(colorama.Fore.RED+"Error: No Team or Individual Files")
        print(colorama.Fore.WHITE)
    else:
        while ans[0] != "i" and ans[0] != "t":
            ans = input(colorama.Fore.WHITE+"Input your ID to continue\n-").lower()

            if ans[0] != "i" and ans[0] != "t":
                print(colorama.Fore.RED+"Error: Invalid ID")
                print(colorama.Fore.RED)

            elif ans[0] == "t":
                for i in files:
                    filestring = filestring + ", "+os.path.basename(i)

                if filestring.find("team") != -1:
                    if(filestring[filestring.find("team")] == "t"):
                        if filestring.find("team"+ans[1]) != -1:
                            place = "teams//team"+ans[1]+".json"
                            with open(place, "r") as r:
                                jsondata = json.load(r)
                                print(colorama.Fore.GREEN+"Successfully loaded file")
                                print(colorama.Fore.WHITE)
                        else:
                            print(colorama.Fore.RED+"File does not exist")
                            print(colorama.Fore.WHITE)
                            quit()
                            
                        

                    
                        
            elif ans[0] == "i":
                for i in files:
                   filestring = filestring + ", "+os.path.basename(i)
                if filestring.find("indiv") != -1:
                    if(filestring[filestring.find("indiv")] == "i"):
                        if filestring.find("individual"+ans[1]) != -1:
                            place = "indivs//indiv"+ans[1]+".json"
                            with open(place, "r") as r:
                                jsondata = json.load(r)
                                print(colorama.Fore.GREEN+"Successfully loaded file")
                                print(colorama.Fore.WHITE)
                        else:
                            print(colorama.Fore.RED+"File does not exist")
                            print(colorama.Fore.WHITE)
                            quit()
                           
#Check for file--------------------------------------------------------------------------------------------
#Menu


      
                

        




else:
    print("No colours for you!")

