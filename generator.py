#standard library imports
import argparse
import secrets

#third party imports
import pyperclip

#local imports
import constants

def readFile(filename:str)->list:
    with open(filename) as file:
        return file.readlines()
    
def splitDictionary(wordList, length:int)->tuple:
    longWordList = list()
    shortWordList = list()

    for word in wordList:
        if len(word) > length:
            longWordList.append(word)
        else:
            shortWordList.append(word)

    return shortWordList, longWordList 

def generatePassphrase(*, wordList:list[str], wordCount = 4, lowercase = True, numbers = False, symbols = False) -> str:
    numberList = '0123456789'
    symbolList = "~`!@#$%^&*()-+=?<>"
    chosenWords = list()
    randomNumber = secrets.choice(numberList)
    randomSymbol = secrets.choice(symbolList)
    joiner = ''
    
    for _ in range(wordCount):
        word = secrets.choice(wordList)
        if not lowercase:
            word = word.capitalize()
        chosenWords.append(word.strip())

    passphrase = joiner.join(chosenWords)

    if numbers:
        passphrase = passphrase + randomNumber

    if symbols:
        passphrase = passphrase + randomSymbol
    
    return passphrase

def generatePassword(length:int)->str:
    numberList = '0123456789'
    symbolList = "~`!@#$%^&*()-+=?<>"
    letterList = "abcdefghijklmnopqrstuvwxyz"
    upperLetterList = letterList.upper()
    allCharacters = numberList + symbolList + letterList + upperLetterList

    password = ""
    while len(password) < length:
        password += secrets.choice(allCharacters)
    
    return password

if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('wordCount', type=int, default = 4, help="The number of words to use in a passphrase, or the number of characters in a password")
    argumentParser.add_argument('-m', "--mode", default='phrase', choices=['phrase', 'word'], help="Specifies whether to create a random password or a human-readable passphrase, defaults to passphrase")
    argumentParser.add_argument("-d", "--dictionary", default = "dictionary.txt", help="The relative path to the word list file; default: dictionary.txt")
    argumentParser.add_argument("-l", "--lowercase", action="store_true", help="NOT RECOMMENDED: only use lowercase letters")
    argumentParser.add_argument("-n", "--numbers", action="store_true", help="includes a number in the generated password")
    argumentParser.add_argument("-y", "--symbols", action="store_true", help="includes a symbol in the generated password")
    argumentParser.add_argument("-s", "--short", action="store_true", help="Only use words with six or fewer characters")

    args = argumentParser.parse_args()

    if args.mode == 'phrase':
        wordList = readFile(args.dictionary)
        shortWordList, longWordList = splitDictionary(wordList, constants._SHORT_WORD_LENGTH)

        if args.short:
            wordList = shortWordList

        password = generatePassphrase(wordList=wordList, wordCount=args.wordCount, lowercase=args.lowercase, numbers=args.numbers, symbols=args.symbols)
    elif args.mode == 'word':
        password = generatePassword(args.wordCount)
        
    print(password)
    print(f"Password Length: {len(password)}")
    pyperclip.copy(password)
    print("Password copied to clipboard")