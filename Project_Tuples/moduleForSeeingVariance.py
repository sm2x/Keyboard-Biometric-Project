"""
Get all of the files
"""
import matplotlib.pyplot as plt
import numpy
import glob
import os
import json
"""
xValues = [1,2,3,4,4,4]
yValues = [4,3,2,1,2,3]
plt.figure("test figure")
plt.scatter(xValues,yValues)
plt.show()
"""
#For Testing in differentparts of a sentence
word = open("Blank TEXT.txt","r")
sentence = word.readlines()
passage = sentence[1]
print(passage)
#passage = "even at the best of times it was seldom working, and at present the electric current was cut off during daylight hours"
plt.figure("Varience")
os.chdir("library/Sentence")
listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

referenceDict = json.load(open(listOfTxtFiles[0],'r'))
keys = list(referenceDict.keys())

nonKey = "CKB t@,"
print(referenceDict)

perfList = listOfTxtFiles[0:30:10]+listOfTxtFiles[1:30:10]+listOfTxtFiles[2:30:10]+listOfTxtFiles[3:30:10]+listOfTxtFiles[4:30:10]
for file in perfList:#Every Other Terms[::2] for others
    print(file)
    dict = json.load(open(file,'r'))
    xValues = []
    yValues = []
    i = 0
    for key in keys:
        if not (key in nonKey):
            xValues.append(i)
            yValues.append(dict[key])
            print(i, "is", key, "and the value is", dict[key])
            i = i+1
            
    plt.plot(xValues,yValues,label = file)

plt.legend()
plt.show()
