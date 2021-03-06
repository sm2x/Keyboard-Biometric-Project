__version__ = '1.0'
__author__ = 'Zachary Nowak'
"""STANDARD LIBRARY IMPORTS"""
from statistics import median#FIXME

def create_dict(pressCharTimeLine,pressTimeLine,releaseCharTimeLine, releaseTimeLine, dataDict):
	
	"""FIND NUMBER OF UNIQUE CHARACTERS"""
	runningHistory = ""
	for char in pressCharTimeLine:
		if char not in runningHistory:
			runningHistory+=char
	numUniqueChar = len(runningHistory)-1#DO NOT COUNT THE /n
	pressTimingList = [[] for i in range(numUniqueChar)]
	
	"""FIND THE PRESS TIMES FOR EACH LETTER"""
	for i in range(len(pressCharTimeLine)-1):
		#The function finds the initial press time in the timeline then it subtracts
		#that from the release time and that gives the total press time.
		char = pressCharTimeLine[i]
		j = 0
		while(True):
			j = releaseCharTimeLine.index(char,j)
			sum = releaseTimeLine[j]-pressTimeLine[i]
			if (sum>0):
				break
			else:
				j += 1
				
		charIndex = runningHistory.index(char)
		pressTimingList[charIndex].append(releaseTimeLine[j] - pressTimeLine[i])
		
	"""ASSIGN THE LETTER WITH IT'S MEDIAN TOTAL PRESS TIME"""	
	for i in range(len(pressTimingList)):
		char = runningHistory[i]
		aSet = pressTimingList[i]
		dataDict[char] = median(aSet)
		
	return dataDict
