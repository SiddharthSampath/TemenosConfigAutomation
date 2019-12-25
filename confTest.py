#Conf File Testing
import fileinput
import re
import fnmatch
conf = "C:/Temenos/TAFJ/conf"
tafjHome = "C:\Temenos\TAFJ\\"
linkFile = conf + "/tafj.link.txt"
devFile = conf + "/dev.properties.txt"
#print(linkFile)
#print(devFile)

textToSearch = "path=*"

with fileinput.FileInput(linkFile, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, (textToSearch + tafjHome)), end='')
'''        
x = ""
with open(linkFile) as fp1:
    x = fp1.read()
x = fp1.split()
if len(x) == 1:
    x.append(tafjHome)

    #print(x)
'''    
with open(devFile) as fp2:
    y = fp2.read()
    y = y.split('\n')
    #print(y)
tafjHomeIndex = 0
for item in range(len(y)):
    if y[item].startswith('temn.TAFJ.home'):
        tafjHomeIndex = item
print(tafjHomeIndex)
        
tafjHomeDev = fnmatch.filter(y,'temn.TAFJ.home*')
#print(tafjHomeDev)
newTafjHomeDev = tafjHomeDev[0].split('=')
#print(newTafjHomeDev[0])

newTafjHomeDev = newTafjHomeDev[0] + "=" + tafjHome
y[tafjHomeIndex] = newTafjHomeDev
y = "\n".join(y)
print(y)
with open(devFile,'w') as fp:
    fp.write(y)
#print(newTafjHomeDev)
    

# Copying lib files from one location to the other

from shutil import copyfile,copy
import os
destination = 'C:/Temenos/T24/libs/t24lib'
source = 'C:/libs/'
srcFiles = os.listdir(source)
for file in srcFiles:
    fileName = source + file
    print(fileName)
    if os.path.isfile(fileName):
        copy(fileName,destination)
    


