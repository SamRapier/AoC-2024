def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
# read file
# identify frequencies (digits, capitals and lowercase)
# identify frequency positions
    # store in dictionary
# for each frequency identify vectors between them
# compute anit-nodes for frequency vectors
    # sotre vector and anti-ndoes in dictionary with frequecy index as key
    # global anti-node store in list

import re
def getFrequencies(map):

    regexPattern = "[a-zA-Z0-9]+"
    frequncyList = []
    for m in map:
        frequncys = (re.findall(regexPattern, m))
        for freq in frequncys:
            if freq not in frequncyList:
                frequncyList.append(freq)

    return frequncyList

def findFrequencyPosition(searchSpace, freq):
    freqPos = []
    for i in range(len(searchSpace)):
        for j in range(len(searchSpace[i])):
            if searchSpace[i][j] == freq:
                freqPos.append([i, j])
    return freqPos

def getAllFreqPositions(map, freqList):
    freqPosDict = {}
    for freq in freqList:
        freqPosDict[freq] = findFrequencyPosition(map, freq)
        
    return freqPosDict

# def getAntiNodes(vector):
#     x = vector[0]
#     y = vector[1]

#     antiNodes = [[2*x, 2*y], [-2*x, -2*y]]

#     return antiNodes



def getAntiNodes(map, freqNodePos):
    maxX = len(map)
    maxY = len(map[0])
    for i in range(len(freqNodePos)-1):
        for j in range(i, len(freqNodePos)):
            a = freqNodePos[i]
            b = freqNodePos[j]

            x = b[0] - a[0]
            y = b[1] - a[1]
            vector = [x, y]

            vX = vector[0]
            vY = vector[1]
            a1 = [a[0] - vX, a[1] - vY]
            a2 = [b[0] + vX, b[1] + vY]

            # print(a, b, vector, a1, a2)

            if a1[0] < 0 or a1[0] >= maxX or a1[1] < 0 or a1[1] >= maxY or a1 in freqNodePos:
                a1 = None
            if a2[0] < 0 or a2[0] >= maxX or a2[1] < 0 or a2[1] >= maxY or a2 in freqNodePos:
                a2 = None

            # antiNodes = [a1, a2]
            if a1 not in globalAntiNodes:
                globalAntiNodes.append(a1)
            if a2 not in globalAntiNodes:
                globalAntiNodes.append(a2)

            # memo[(i, j)] = [vector, antiNodes]
            # memo[(j, i)] = [vector, antiNodes]

            


def processAllFreq(map, freqDict):
   
    for freq in freqDict.values():
        # print(freq)
        getAntiNodes(map, freq)


globalAntiNodes = []
def main():
    # map = openFile("example8")
    map = openFile("input8")
    freqList = getFrequencies(map)
    freqPosDict = getAllFreqPositions(map, freqList)
    # print(freqPosDict)
    processAllFreq(map, freqPosDict)

    globalAntiNodes.remove(None)

    # print("answers: ", globalAntiNodes)
    print(len(globalAntiNodes))

main()

# test = openFile("answer8")
# answerPos = findFrequencyPosition(test, "#") 

# # print("answers: ", answerPos)
# # print(len(answerPos))