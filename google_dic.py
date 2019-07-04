import time 	
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
	    print(message)
	    status.append(message)
	    if (data):
	    	results.append(data)
	    time.sleep(5)

	sysHand.writeDataToJSON(results, pathDataOut)
	sysHand.writeListToFile(status, pathStatusOut)




#myWord = getSingleWord('a')
#print(myWord)

START_NUMBER = 1400
STOP_NUMBER = 1499
PATH_IN = "E:/FULLTEXT/SPECIALTY/Full_Words_List.txt"
PATH_OUT = "E:/FULLTEXT/GOOGLE/"


RunCode(START_NUMBER, STOP_NUMBER, PATH_IN, PATH_OUT)


