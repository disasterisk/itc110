import re
import os
import pprint
currentFolder = r"C:\\"
txtCount = 0
newDirectory = True
while True:
    if newDirectory:
        txts = []
        txtCount = 0
        direct = os.listdir(currentFolder)
        for file in direct:
            newDirectory = False
            txt = re.search("\.txt$", file)
            if txt is not None:
                txts.append(file)
                txtCount += 1
    print("There are "+str(txtCount)+" text files in this directory.")
    m = "You are in " + currentFolder + ". Type directory or search txt files. "
    task = input(m)
    if task == "search":
        searchterm = re.compile(input("Type in a search. "))
        for file in txts:
            print(file)
            currentFile = open(os.path.join(currentFolder, file))
            print(searchterm.findall(currentFile.read()))
    elif task == "look":
        pprint.pprint(direct)
    elif task in direct:
        newDirectory = True
        currentFolder = os.path.join(currentFolder, task)
        print(currentFolder)
    elif os.path.isdir(task):
        currentFolder = task
        newDirectory = True
    else:
        print("That is not a directory.")
