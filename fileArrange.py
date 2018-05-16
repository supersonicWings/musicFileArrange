import os

currPath = os.getcwd()
for file in os.listdir(currPath):
    fileSplit = file.split('-')
    name = fileSplit[0].strip()
    if len(fileSplit) != 1:
        title = fileSplit[1].strip()
        srcPath = currPath + "/" + file
        dstPath = currPath + "/" + name
        if os.access(dstPath, os.F_OK) == False:
            os.mkdir(dstPath)
        if os.access(dstPath + "/" + file, os.F_OK) == False:
        	os.rename(srcPath, dstPath + "/" + file)
    else:
        pass
