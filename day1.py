# Read input file
# Order 2 lists
# loop through length of list and calc diff between numbers
# save difference 

def openFile(filePath):
    with open(filePath, 'r') as file:
        return file.read().splitlines()
    
def splitList(inputList):
    list1 = []
    list2 = []
    for element in inputList:
        list1.append(int(element.split("   ")[0]))
        list2.append(int(element.split("   ")[1]))

    return list1, list2

def quickSort(inputList):
    if len(inputList) <= 1:
        return inputList
    else:
        pivot = inputList[0]
        left = []
        right = []
        for num in inputList[1:]:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return quickSort(left) + [pivot] + quickSort(right)

def calcDiff(list1, list2):
    diffCalc = 0
    for i in range(len(list1)):
        diffCalc += abs(list1[i] - list2[i])
    return diffCalc

def frequency(inputList):
    freqDict = {}
    for i in inputList:
        if i in freqDict:
            freqDict[i] += 1
        else:
            freqDict[i] = 1
    return freqDict

def calcSimilarity(inputList, freqDict):
    similarityScore = 0
    for i in inputList:
        if i in freqDict:
            similarityScore += i * freqDict[i]

    return similarityScore

def getSortedLists(fileName):
    inputList = openFile(f"inputs/{fileName}.txt")
    list1, list2 = splitList(inputList)
    list1 = quickSort(list1)
    list2 = quickSort(list2)
    return list1, list2

def problem1():
    list1, list2 = getSortedLists("input1")
    print(calcDiff(list1, list2))
    
def problem2():
    list1, list2 = getSortedLists("input1")
    freqDict = frequency(list2)
    print(calcSimilarity(list1, freqDict))


# problem1()
problem2()
