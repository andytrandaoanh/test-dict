<<<<<<< HEAD
import time, sys 	
=======
import sys, time 	
>>>>>>> 63466e5b5c00b6bbd5e67e9b2278ee09a911e92c
import requests, json
import system_handler as sysHand



def getSingleWord(word):
	DATA_STATUS_OK = 200

	url = "https://googledictionaryapi.eu-gb.mybluemix.net/?define=" + word + "&lang-en"
	response = requests.get(url)
	if (response.status_code == DATA_STATUS_OK):
		if (response.content):
			try:
				data = json.loads(response.content)
				statusMessage = "Sucessfully get this word: " + word
				
				#print(data)
				return (data, statusMessage) 
			except:				
				statusMessage = "An exception occurred while getting " + word
				return (None, statusMessage)
				
		
	else:		
		statusMessage = "Remote get failed at " + word
		return (None, statusMessage)



def RunCode(START_NUMBER, STOP_NUMBER, PATH_IN, PATH_OUT):

	pathDataOut, pathStatusOut = sysHand.getIncrementPath(START_NUMBER, PATH_OUT)

	wordList = sysHand.getWordFromTextFile(PATH_IN)

	results = []
	status = []

	for i in range(START_NUMBER, STOP_NUMBER):
	    word = wordList[i]
	    (data, message) = getSingleWord(word)
	    print(i, ':',  message)
	    status.append(message)
	    if (data):
	    	results.append(data)
	    time.sleep(3)

	sysHand.writeDataToJSON(results, pathDataOut)
	sysHand.writeListToFile(status, pathStatusOut)




<<<<<<< HEAD


if __name__ == "__main__":
	START_NUMBER = 3600
	STOP_NUMBER = START_NUMBER + 99
	PATH_IN = "E:/FULLTEXT/SPECIALTY/Full_Words_List.txt"
	PATH_OUT = "E:/FULLTEXT/GOOGLE/"

=======
#myWord = getSingleWord('a')
#print(myWord)
if __name__ == '__main__':
	START_NUMBER = 4500
	STOP_NUMBER = START_NUMBER + 99
	PATH_IN = "E:/FULLTEXT/SPECIALTY/Full_Words_List.txt"
	PATH_OUT = "E:/FULLTEXT/GOOGLE/"


	RunCode(START_NUMBER, STOP_NUMBER, PATH_IN, PATH_OUT)
	sysHand.openDir(PATH_OUT)
	sys.exit()
>>>>>>> 63466e5b5c00b6bbd5e67e9b2278ee09a911e92c

	RunCode(START_NUMBER, STOP_NUMBER, PATH_IN, PATH_OUT)

	sysHand.openDir(PATH_OUT)
	sys.exit()

