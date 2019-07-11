def fixQuote(sInput):
	try:
		strTemp = str(sInput)
		sOutput = strTemp.replace("'", "''")
		return sOutput
	except Exception as e:
		print(e) 



#inputString = "you're my love"

#print(fixQuote(inputString))