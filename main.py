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



def RunCode(START_NUMBER, proxies, headers):
	PATH_IN = "E:/FULLTEXT/SPECIALTY/NLTK_Words_List.txt"
	PATH_DATA_OUT = "E:/FULLTEXT/GOOGLE/RAW"
	PATH_LOG_OUT = "E:/FULLTEXT/GOOGLE/LOG"
	STOP_NUMBER = START_NUMBER + 100

	pathDataOut, pathStatusOut = sysHand.getIncrementPath(START_NUMBER, PATH_DATA_OUT, PATH_LOG_OUT)

	wordList = sysHand.getWordFromTextFile(PATH_IN)

	results = []
	status = []

	for i in range(START_NUMBER, STOP_NUMBER):
	    word = wordList[i]
	    (data, message) = getSingleWord(word, proxies, headers)
	    print(i, ':',  message)
	    status.append(str(i) + ' ' + message)
	    if (data):
	    	results.append(data)
	    time.sleep(3)

	sysHand.writeDataToJSON(results, pathDataOut)
	sysHand.writeListToFile(status, pathStatusOut)


if __name__ == '__main__':
	START_NUMBER = 40100
	STOP_NUMBER	 = START_NUMBER + 20000
	STEP_NUMBER = 100

	proxies = startPrivateProxy()

	for i in range(START_NUMBER, STOP_NUMBER, STEP_NUMBER):
		print('starting at:', i)
		user_agent = getRamdomUserAgent()
		print('using agent:', user_agent)
		headers = {'User-Agent': user_agent}
		#test ip 
		urlTest = "http://icanhazip.com"
		resTest = requests.get(urlTest, proxies=proxies, headers=headers)
		print('using IP:', resTest.text)

		RunCode(i, proxies, headers)
		time.sleep(10)
		#initNumber 
		
