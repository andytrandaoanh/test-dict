import sys, time 	
import requests, json
import system_handler as sysHand
from alternate_agent import getRamdomUserAgent
from start_private_proxy import startPrivateProxy


def getSingleWord(word, proxies, headers):
	DATA_STATUS_OK = 200

	url = "https://googledictionaryapi.eu-gb.mybluemix.net/?define=" + word + "&lang-en"
	#response = requests.get(url)
	#response = requests.get(url, proxies={"http": proxy, "https": proxy}, headers = {'User-Agent': agent})
	response = requests.get(url, proxies=proxies, headers=headers)
	#response = session.get(url, headers=headers)

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



def RunCode(START_NUMBER, proxies, headers, mode, location):
	
	PATH_IN = "E:/FULLTEXT/DICTIONARY/SPECIALTY/NLTK_Words_List.txt"
	PATH_DATA_OUT = ''
	PATH_LOG_OUT = ''


	print('Path In:', PATH_IN)
	#For Home only

	if (mode == "local"):
		PATH_DATA_OUT = "E:/FULLTEXT/GOOGLE/RAW"
		PATH_LOG_OUT = "E:/FULLTEXT/GOOGLE/LOG"
	
	elif (mode == "remote"):
		if (location == "home"):
			PATH_DATA_OUT = "C:/Users/Andy Anh/Dropbox/PROGRAMMING/FULLTEXT/GOOGLE/RAW"
			PATH_LOG_OUT = "C:/Users/Andy Anh/Dropbox/PROGRAMMING/FULLTEXT/GOOGLE/LOG"
		elif (location == "office"): 
			PATH_DATA_OUT = "C:/Users/Administrator/Dropbox/PROGRAMMING/FULLTEXT/GOOGLE/RAW"
			PATH_LOG_OUT = "C:/Users/Administrator/Dropbox/PROGRAMMING/FULLTEXT/GOOGLE/LOG"

	print('\nData Path:', PATH_DATA_OUT, '\nLog Path:', PATH_LOG_OUT)



	STOP_NUMBER = START_NUMBER + 100

	print('starting at:', START_NUMBER)
	print('using agent:', headers['User-Agent'])
	urlTest = "http://icanhazip.com"
	resTest = requests.get(urlTest, proxies=proxies, headers=headers)
	print('using IP:', resTest.text)



	pathDataOut, pathStatusOut = sysHand.getIncrementPath(START_NUMBER, PATH_DATA_OUT, PATH_LOG_OUT)

	wordList = sysHand.getWordFromTextFile(PATH_IN)
	
	results = []
	status = []
	dateStamp = sysHand.getDateStamp()
	status.append('Starting scraping Google at  ' + dateStamp)
	status.append('Starting scraping at index ' + str(START_NUMBER))
	status.append('Starting scraping using IP ' + resTest.text)
	status.append('Starting scraping using agent ' + headers['User-Agent'])



	for i in range(START_NUMBER, STOP_NUMBER):
	    word = wordList[i]
	    (data, message) = getSingleWord(word, proxies, headers)
	    print(i, ':',  message)
	    status.append(str(i) + ' ' + message)
	    if (data):
	    	results.append(data)
	    time.sleep(3)

	sysHand.writeDataToJSON(results, pathDataOut)
	dateStamp = sysHand.getDateStamp()
	status.append('Ending scraping Google at ' + dateStamp)
	sysHand.writeListToFile(status, pathStatusOut)


def main(startNumber, mode, location):
	#START_NUMBER = 107200
	START_NUMBER = startNumber 
	STOP_NUMBER	 = START_NUMBER + 50000
	STEP_NUMBER = 100

	proxies = startPrivateProxy()

	for i in range(START_NUMBER, STOP_NUMBER, STEP_NUMBER):		
		user_agent = getRamdomUserAgent()		
		headers = {'User-Agent': user_agent}
		RunCode(i, proxies, headers, mode, location)
		time.sleep(10)


if __name__ == '__main__':
	try:

		#default argument
		startNumber = 119000		
		mode = "local"
		location = "home"


		lenArgs = len(sys.argv)
		#print('length of argument list:', lenArgs)

		if (lenArgs > 1):
			startNumber = int(sys.argv[1])			
		
		if (lenArgs > 2):
			if (sys.argv[2] == "local" or sys.argv[2] == "remote"):
				mode = sys.argv[2]

		if (lenArgs > 3):
			if (sys.argv[3] == "home" or sys.argv[3] == "office"):
				location = sys.argv[3]


		print('\nstartNumber:', startNumber, '\nmode:', mode, '\nlocation:', location)
		main(startNumber, mode, location)



	except Exception as e:
		print (e)

		
