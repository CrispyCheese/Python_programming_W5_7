DELIMITER = ","
def collectWords():
    words = ""
    while True:
        feed = input("Insert word(empty stops): ")
        if (len(feed) == 0):
            break
        elif (len(words) == 0):
            words += feed
        else:
            words += DELIMITER + feed
    return words

def analyzeWords(Pwords):
    characters = 0
    wordCount = 0
    if (len(Pwords) > 0):
        wordCount += 1
        for i in range (len(Pwords)):
            if (Pwords[i] == DELIMITER):
                wordCount += 1
                continue
            else:
                characters += 1
    average = characters / wordCount
    print (f"- {wordCount} Words\n- {characters} Characters") 
    print ("- {:.2f} Average word length".format(average))
    return None

def main():
    print ("Program starting.")
    collectedWords = collectWords()
    analyzeWords(collectedWords)
    print ("Program ending.")

main()
