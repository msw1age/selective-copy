#!/usr/bin/env python3
#Walk through a folder tree and copy files with a certain file extension to a new folder
import os, shutil, sys
usage = "./selectivecopy.py .ext"
#Exit if program is used incorrectly
if len(sys.argv) != 2 or len(sys.argv[1]) < 2:
    print(usage)
    sys.exit()
extension = sys.argv[1]
#Create a directory for the files if it does not already exist
print("Creating directory '%s' in " % extension[1:] + os.path.abspath('.'))
try:
    os.makedirs(extension[1:])
except FileExistsError:
    print("Directory already exists. Continuing...")
newFolder = os.path.join('.', extension[1:])
#Walk through a folder tree
for folderName, subFolders, subFiles in os.walk('.'):
    #Search for files with the given file extension. Ignore the folder we just made
    if folderName != newFolder:
        for subFile in subFiles:
            if subFile.endswith(extension):
                #Copy these files to a new folder
                print("Copying file " + subFile + " from " + folderName + " to " + os.path.abspath(newFolder))
                try:
                    shutil.copy(os.path.join(folderName, subFile), newFolder)
                except PermissionError:
                    print("Could not copy file " + subFile + ": PermissionError")
~                                                                                             
