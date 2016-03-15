import os
import re
import pprint
import shutil

while True:
    directory = None
    while directory is None:
        directory = input('Enter a folder. ')
        if os.path.isdir(directory) is False:
            directory = None
            print('Sorry, I can\'t find that folder. ')
    items = os.listdir(directory)
    print(items)
    subdir = []
    files = []
    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            subdir.append(item)
        elif os.path.isfile(path):
            files.append(item)
    print('There are '+ str(len(subdir)) + ' subdirectories!')
    pprint.pprint(subdir)
    print('There are '+ str(len(files)) + ' files!')
    pprint.pprint(files)
    search = input("Enter search. Blank to exit. ")
    results = []
    if search is '':
        continue
    else:
        search = '^(' + search + ')(\d)*(\.\w*)'
        print(search)
        search = re.compile(search)
        for file in files:
            if search.search(file) is not None:
                results.append(file)
        print(results)

        noGaps = True
        count = search.search(results[0])
        count = int(count.group(2))
        for result in results:
            name = search.search(result)
            if noGaps is True:
                print(name.group(2))
                print(count)
                if int(name.group(2)) == count:
                    print(result)
                else:
                    noGaps = False
                    nn = name.group(1) + str(count) + name.group(3)
                    print(nn)
                    result = os.path.join(directory, result)
                    nn = os.path.join(directory, nn)
                    shutil.move(result, nn)
            else:
                newName = name.group(1) + str(count) + name.group(3)
                print(newName)
                result = os.path.join(directory, result)
                newName = os.path.join(directory, newName)
                shutil.move(result, newName)
            count += 1