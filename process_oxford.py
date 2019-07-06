import re
import system_handler as sysHand


inPath = "E:/FULLTEXT/SPECIALTY/Oxford_Word_List.txt"
outPath = "E:/FULLTEXT/SPECIALTY/Oxford_Two_Word_Compound.txt"

inputText = """
Aberdeen Angus
Aberdonian
"""

regPat = r'^\w+\s\w+$'
pattern = re.compile(regPat, re.M)
#finds = re.findall(pattern, inputText)
#print(finds)

data = sysHand.readTextFile(inPath)
wordList = data.split('\n')

twoWords = []

for word in wordList:
	matchObj = re.search(pattern, word)
	if(matchObj):
		twoWords.append(word)

sysHand.writeListToFile(twoWords, outPath)
