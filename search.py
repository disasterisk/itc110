import re
import os
import pprint
currentFolder = r"C:\\"
txtCount = 0
txts = []
newDirectory = True
while True:
    if newDirectory:
        txtCount = 0
        direct = os.listdir(currentFolder)
        for file in direct:
            newDirectory = False
            txt = re.search("\.txt$", file)
            if txt is not None:
                txts.append(currentFolder+file)
                txtCount += 1
    print("There are "+str(txtCount)+" text files in this directory.")
    task = input("You are in " + currentFolder + ". Type in directory or search txt files. ")
    if task == "search":
        searchterm = re.compile(input("Type in a search. "))
        for file in txts:
            currentFile = open(file)
            print(searchterm.findall(currentFile.read()))
    elif task == "look":
        pprint.pprint(direct)
    elif task in direct:
        backslash = re.compile(r"\$")
        if backslash.search(currentFolder):
            x = currentFolder + task
        else:
            x = currentFolder + "\\" + task
        if os.path.isdir(x):
            currentFolder = x
            newDirectory = True
        else:
            print("That is not a directory.")
    elif os.path.isdir(task):
        currentFolder = task
        newDirectory = True
    else:
        print("That is not a directory.")