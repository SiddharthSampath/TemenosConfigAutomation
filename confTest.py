#Conf File Testing
#C:\T24_DEV\Temenos\TAFJ\data\DEV\classes
import fileinput
import re
import fnmatch

areaVersion = input("Enter the area you want configured : (default : T24_DEV, Press Enter to default value)")
if areaVersion == "":
    areaVersion = "T24_DEV"

conf = "C:\\Temenos\\TAFJ\\conf"
tafjHome = "C:\\Temenos\TAFJ\\"
linkFile = conf + "\\tafj.link.txt"
devFile = conf + "\\dev.properties.txt"
encode = input("Enter the type of encoding (cp1252/UTF-8). Recommended : cp1252 (Default : cp1252)")
if encode =="":
    encode = "cp1252"
#print(linkFile)
#print(devFile)



with open(devFile) as fp2:
    devContents = fp2.read()
    devContents = devContents.split('\n')
    #print(y)
tafjHomeIndex = 0
insertIndex = 0
javaIndex = 0
classesIndex = 0
precompileIndex = 0
encodingIndex = 0

for item in range(len(devContents)):
    if devContents[item].startswith('tafj.home'):
        tafjHomeIndex = item
    elif devContents[item].startswith('temn.tafj.directory.insert'):
        insertIndex = item
    elif devContents[item].startswith('temn.tafj.directory.java'):
        javaIndex = item
    elif devContents[item].startswith('temn.tafj.directory.classes'):
        classesIndex = item
    elif devContents[item].startswith('temn.tafj.directory.precompile'):
        precompileIndex = item
    elif devContents[item].startswith('temn.tafj.runtime.ud.encoding'):
        encodingIndex = item

#TafjHome        
tafjHomeDev = fnmatch.filter(devContents,'tafj.home*')
tafjHomeDev = tafjHomeDev[0].split('=')
tafjHomeDev = tafjHomeDev[0] + "= " + tafjHome

#Lib Files
insertFiles = fnmatch.filter(devContents,'temn.tafj.directory.insert*')
insertFiles = insertFiles[0].split('=')
insertFiles = insertFiles[0] + "= " + 'C:\\Temenos\\T24\\libs\\t24lib'

#Java Files
javaFiles = fnmatch.filter(devContents,'temn.tafj.directory.java*')
javaFiles = javaFiles[0].split('=')
javaFiles = javaFiles[0] + "= " + 'C:\T24_DEV\Temenos\TAFJ\data\DEV\java'

#Class Files
classFiles = fnmatch.filter(devContents,'temn.tafj.directory.classes*')
classFiles = classFiles[0].split('=')
classFiles = classFiles[0] + "= " + 'C:\T24_DEV\Temenos\TAFJ\data\DEV\classes'

#Encoding
encoding = fnmatch.filter(devContents,'temn.tafj.runtime.ud.encoding*')
encoding = encoding[0].split('=')
encoding = encoding[0] + "= " + encode


devContents[tafjHomeIndex] = tafjHomeDev
devContents[insertIndex] = insertFiles
devContents[javaIndex] = javaFiles
devContents[classesIndex] = classFiles
devContents[precompileIndex] = insertFiles
devContents[encodingIndex] = encoding

devContents = "\n".join(devContents)
print(devContents)
with open(devFile,'w') as fp:
    fp.write(devContents)
#print(newTafjHomeDev)
    

# Copying lib files from one location to the other
'''
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
    
'''















'''
textToSearch = "path=*"

with fileinput.FileInput(linkFile, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, (textToSearch + tafjHome)), end='')
        '''

