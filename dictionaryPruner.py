def readFile(filename:str)->list:
    with open(filename) as file:
        return file.readlines()

def writeDictionary(filename:str, content:list)->None:
    with open(filename, "w") as file:
        for word in content:
            file.write(f"{word}")

def splitDictionary(wordList, length:int)->tuple:
    longWordList = list()
    shortWordList = list()

    for word in wordList:
        if len(word) > length:
            longWordList.append(word)
        else:
            shortWordList.append(word)

    return shortWordList, longWordList 

if __name__ == "__main__":
    filename = input("Enter a filename: ")
    wordList:list = readFile(filename)
    wordLength = int(input("Enter maximum length of short words: "))

    shortWordList, longWordList = splitDictionary(filename, wordLength)

    print(f"Original Word Count: {len(wordList)}")
    
    print(f"Long Word Count: {len(longWordList)}")
    print(f"Short Word Count: {len(shortWordList)}")
    writeDictionary("longWords.txt", longWordList)
    print(f"Long words written to longWords.txt")
    writeDictionary("shortWords.txt", shortWordList)
    print(f"Short words written to shortWords.txt")