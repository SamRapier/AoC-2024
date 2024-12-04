up = [-1,0]
down = [1,0]
left = [0,-1]
right = [0,1]

topRight = [-1,1]
topLeft = [-1,-1]
bottomRight = [1,1]
bottomLeft = [1,-1]

proximitySearch = [up, down, left, right, topRight, topLeft, bottomRight, bottomLeft]

def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
def findStartingLetter(searchSpace, letter):
    letterLocations = []
    for i in range(len(searchSpace)):
        for j in range(len(searchSpace[i])):
            if searchSpace[i][j] == letter:
                letterLocations.append([i, j])
    return letterLocations


def findWords(searchSpace, word, startingLocations):
    wordCount = 0
    for location in startingLocations:

        for direction in proximitySearch:
            if findNextLetter(searchSpace, word, 1, location, direction):
                wordCount += 1
        
    return wordCount


def findNextLetter(searchSpace, word, index, start, direction):
    searchX = start[0] + direction[0]
    searchY = start[1] + direction[1]

    if searchX < 0 or searchX >= len(searchSpace):
        return False
    if searchY < 0 or searchY >= len(searchSpace[0]):
        return False
    
    if searchSpace[searchX][searchY] == word[index]:
        if index == len(word) - 1:
            return True
        else:
            return findNextLetter(searchSpace, word, index + 1, [searchX, searchY], direction)

    return False

def checkXshape(searchSpace, startingLocations):
    wordCount = 0
    
    for location in startingLocations:
        count = 0
        if checkLetter(searchSpace, location, topRight, "M") and checkLetter(searchSpace, location, bottomLeft, "S"):
            count += 1
        if checkLetter(searchSpace, location, topLeft, "M") and checkLetter(searchSpace, location, bottomRight, "S"):
            count += 1
        if checkLetter(searchSpace, location, topRight, "S") and checkLetter(searchSpace, location, bottomLeft, "M"):
            count += 1
        if checkLetter(searchSpace, location, topLeft, "S") and checkLetter(searchSpace, location, bottomRight, "M"):
            count += 1

        if count == 2:
            wordCount += 1

    return wordCount


def checkLetter(searchSpace, start, direction, letter):
    searchX = start[0] + direction[0]
    searchY = start[1] + direction[1]

    if searchX < 0 or searchX >= len(searchSpace):
        return False
    if searchY < 0 or searchY >= len(searchSpace[0]):
        return False
    
    if searchSpace[searchX][searchY] == letter:
        return True

def problem1():
    # searchSpace = openFile("example4.1")
    # searchSpace = openFile("example4.2")
    searchSpace = openFile("input4")

    searchWord = "XMAS"

    xLocations = findStartingLetter(searchSpace, searchWord[0])
    numWords = findWords(searchSpace, searchWord, xLocations)

    print(numWords)


def problem2():
    # searchSpace = openFile("example4.1")
    # searchSpace = openFile("example4.2")
    # searchSpace = openFile("example4.3")
    searchSpace = openFile("input4")

    # searchWord = "XMAS"
    aLocations = findStartingLetter(searchSpace, "A")
    numWords = checkXshape(searchSpace, aLocations)
    print(numWords)

problem2()