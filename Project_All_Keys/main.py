#cmd /K "$(FULL_CURRENT_PATH)"
"""
Author: Zachary Nowak 
Date:10/31/2017

Program Description: This code can record the 
Press Time and Flight Time of a user as they 
type a passage and saves the matrix to a file. 
"""
import win32api
import os
import moduleForCreatingAPassword
import listOfAllKeys
import moduleForCreatingAMatrix
import time
import numpy as np
#TO-DO
#FIXME IMPROVE FLIGHT TIME

stateDict = listOfAllKeys.stateDict
nameDict = listOfAllKeys.nameDict
xDict = listOfAllKeys.xDict
yDict = listOfAllKeys.yDict
keyToIndex = moduleForCreatingAMatrix.newDict

"""[letter(in the keyToIndex), startPress, AVGPressTime,  AVGFlightTime, counter, hand(0-1)"""
#dataMatrix info
startPress 		= 1
AVGPressTime	= 2
AVGFlightTime 	= 3
counter 		= 4
hand 			= 5

person = input('Enter your name: ')
filename = "library/"+person+".txt"

try:
	dataMatrix = np.loadtxt(filename, delimiter=",", unpack=False)#OPEN IF EXISTS
except FileNotFoundError:
	dataMatrix = moduleForCreatingAMatrix.matrix #MAKE A NEW ONE IF NOT
	

passageTyped = ""
passage = moduleForCreatingAPassword.Create("Story", 60)#60 is the length of the story
startFlight = 0 #INTIALIZING
print(passage)

end = True
while end:
	for i in range(0,256):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				
				char = nameDict[i]
				char2 = char
				
				"""DETERMINE WHAT CHAR IT IS"""
				
				if i<=57 and i>=48:#NUMBERS
					if stateDict["SHIFT"] == 0:
						char2 = nameDict[i-16]
					else:pass						
				elif (char == "SHIFT") or (stateDict["SHIFT"] == 0) or (char == '.'):#SHIFT KEY, PERIOD, or UPPERCASE
					pass
				else:#LOWERCASE
					try:
						char2 = nameDict[i+32]
					except KeyError:
						pass
						
				dM = dataMatrix[int(keyToIndex[char2])]
				
				if char == "SHIFT" or char == "DELETE": #DO NOT ADD TO STRING
					if stateDict[char] == 0:
						stateDict[char] = -32768 #CHANGE STATES
					else: 
						stateDict[char] = 0 #CHANGES STATE
						os.system('cls')#CLEARS THE COMMAND PROMPT
						if char == "DELETE":#DELETE
							passageTyped = passageTyped[:-1]
						print(passage)
						print(passageTyped)
						dM[counter] += 1
						
					"""RELEASED"""				
				elif stateDict[char] == 0:
					dM[AVGPressTime] = (dM[AVGPressTime]*dM[counter]+(time.time()-dM[startPress]))/(dM[counter]+1)
					#if dM[AVGPressTime]>.3:
					#	dM[AVGPressTime] = (dM[AVGPressTime]*(dM[counter]+1)-(time.time()-dM[startPress]))/dM[counter]
					#	dM[counter] -= 1
					#startFlight = time.time() FIXME
					stateDict[char] = -32768 #CHANGE STATES
				
					"""PRESSED"""
				else:	
					passageTyped += char2
					if startFlight>0:#MEANS STARTED CODE
						dM[AVGFlightTime] = (dM[AVGFlightTime]*dM[counter]+(time.time()-startFlight))/(dM[counter]+1)
						startFlight = time.time()#FIXME
					else:
						startFlight = time.time()
						
					dM[startPress] = time.time()
					dM[counter] += 1#ADD ONE TO THE COUNTER BECAUSE IT WAS PRESSED
					
					os.system('cls')#CLEARS THE COMMAND PROMPT
					
					if (char == '\n')and (dM[counter]>1):#IF ENTER IS PRESSED BREAK THE CODE
						end = False
		
					print(passage)
					print(passageTyped)
					stateDict[char] = 0 #CHANGES STATE
					
		except KeyError:
			pass
			
print("Errors: ", dataMatrix[0][counter])
#RESET ENTERS and BACKSPACES SO THEY CAN BE USED AGAIN
dataMatrix[1][counter] = 0;
dataMatrix[0][counter] = 0;

np.savetxt(filename, dataMatrix, fmt ='%1.7e', delimiter=',')#SAVES ARRAY TO FILE WITH THE PERSONS NAME