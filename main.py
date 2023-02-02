import re

import wordlist as wordlist

fileToRead = 'Assignment 3 file.txt'
fileToWrite = 'EmailsExtracted.txt'
delimiters = [',', ';']
def validation(strEmail):
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file. Write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiters:
        item = item.replace(str(delimeter),' ')
    wordlist = item.split()
    for word in wordList:
        if(validation(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"Total number of Emails found!")
    print(uniqEmail)
    writeFile(uniqEmail)
else:
    print("Noemailsfound.")