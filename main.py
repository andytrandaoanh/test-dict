import os, sys
import json





def loadData(inPath):
	#print('inPath:', inPath, 'dbDir:', dbDir, 'bookID:', bookID)
	#print(pathNin, pathSin)
	jsonPath = inPath
	#print(jsonPath)
	with open(jsonPath) as f:
		entries = json.load(f)
	return entries
	#dbData = []
	#for sentence in sentences:
	#	temp = sentence[0]
	#	dbData.append((int(bookID), temp['sent_cont'], temp['sent_num']))
		

pathCur = os.path.dirname(os.path.abspath(__file__))
pathIn =  os.path.join(pathCur, "data",  "a.json") 
#print(pathIn)
dictData = loadData(pathIn)

print(dictData['a cappella'])