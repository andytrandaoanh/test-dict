from nltk.corpus import words, stopwords
import system_handler as sysHand


#english_stopwords = stopwords.words('english')

#filePath = "E:/FULLTEXT/SPECIALTY/English_Stop_Words.txt"

#sysHand.writeListToFile(english_stopwords, filePath)


filePath = "E:/FULLTEXT/SPECIALTY/Full_Words_List.txt"
wordlist = words.words()

sysHand.writeListToFile(wordlist, filePath)

#print(english_stopwords)