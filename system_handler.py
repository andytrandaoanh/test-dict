import os, sys, json


def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)


	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  

def getIncrementPath(incNumber, outDir):
	JSON_HEADER = "Dict_Extract"
	TEXT_HEADER = "Handling_Status"
	JSON_EXT = ".json"
	TEXT_EXT = ".txt"
	incString = str(incNumber)
	increment = incString.zfill(8)
	
	normal_path =  os.path.join(outDir, JSON_HEADER + increment + JSON_EXT) 
	status_path =  os.path.join(outDir, TEXT_HEADER + increment + TEXT_EXT) 

	return(normal_path, status_path)


def getRawPath(pathIn, dirOut):
	JSON_EXTENSION = ".json"
	temp_path = pathIn
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	pathOut =  os.path.join(dirOut, fname + JSON_EXTENSION) 
	return(pathOut)


def getWordFromTextFile(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
        

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")



def openExclusionList():
	FILE_NAME = 'exclusion.txt'
	try:
	    fh = open(FILE_NAME, 'r', encoding ='utf-8')
	    # Store configuration file values
	    data = fh.read()
	    fh.close()   
	    mylist = data.split('\n')
	    return mylist   
	    
	except FileNotFoundError:
		print('file not found')
		return None

def fileToList(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words
    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    

def loadDictionaries(dirDic):
	dicFiles = os.listdir(dirDic)
	bigDic = []
	for fp in dicFiles:
		bigDic  += fileToList(os.path.join(dirDic, fp))

	dicData = list(dict.fromkeys(bigDic))
	dicData.sort()
	return dicData



def writeDataToJSON(dataIn, pathOut):
	with open(pathOut, 'w', encoding ="utf-8") as outfile:  
		json.dump(dataIn, outfile)
