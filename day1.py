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

def problem1():
    inputList = openFile('inputs/input1.txt')
    # list1 = [1, 7, 4, 1, 10, 9, -2]
    # list2 = [4, 5, 8, 3, 2, 1, 0]
    list1, list2 = splitList(inputList)
    list1 = quickSort(list1)
    list2 = quickSort(list2)
    # print(list1)
    # print(list2)
    print(calcDiff(list1, list2))
    


problem1()
