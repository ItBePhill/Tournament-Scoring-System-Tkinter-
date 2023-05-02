import os
filepath = os.path.dirname(__file__)+r"\\"
logspath = os.path.join(filepath, "Logs")
teampath = os.path.join(filepath, "Teams")
indivpath = os.path.join(filepath, "Indivs")
print(filepath, "\n\n", logspath,"\n\n", teampath,"\n\n", indivpath)