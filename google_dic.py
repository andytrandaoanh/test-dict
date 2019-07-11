import sys, time 	
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
				statusMessage = "Successfully get the word: " + word
				
				#print(data)
				return (data, statusMessage) 
			except:				
				statusMessage = "An exception occurred while getting " + word
				return (None, statusMessage)
				
		
	else:		
		statusMessage = "Fail to remotely get the word " + word
		return (None, statusMessage)



def RunCode(START_NUMBER, PATH_IN, PATH_OUT):
	STOP_NUMBER = START_NUMBER + 100

	pathDataOut, pathStatusOut = sysHand.getIncrementPath(START_NUMBER, PATH_OUT)

	wordList = sysHand.getWordFromTextFile(PATH_IN)

	results = []
	status = []

	for i in range(START_NUMBER, STOP_NUMBER):
	    word = wordList[i]
	    (data, message) = getSingleWord(word)
	    print(i, ':',  message)
	    status.append(str(i) + ' ' + message)
	    if (data):
	    	results.append(data)
	    time.sleep(3)

	sysHand.writeDataToJSON(results, pathDataOut)
	sysHand.writeListToFile(status, pathStatusOut)


if __name__ == '__main__':
	START_NUMBER = 23600
	PATH_IN = "E:/FULLTEXT/SPECIALTY/NLTK_Words_List.txt"
	PATH_OUT = "E:/FULLTEXT/GOOGLE/"
	RunCode(START_NUMBER, PATH_IN, PATH_OUT)
	sysHand.openDir(PATH_OUT)
	sys.exit()

