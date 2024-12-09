def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    

def getFileBlock(diskMap):
    idNumber = 0
    totalFreeSpace = 0
    fileBlock = []
    for i in range(0, len(diskMap)-1, 2):
        files = int(diskMap[i])
        freeSpace = int(diskMap[i+1])
        totalFreeSpace += freeSpace

        # fileBlock.append([idNumber]) * files 
        [fileBlock.append(idNumber) for j in range(files)]
        [fileBlock.append(".") for j in range(freeSpace)]

        idNumber += 1
    
    [fileBlock.append(idNumber) for j in range(int(diskMap[-1]))]
    # fileBlock += str(idNumber) * int(diskMap[-1])

    return fileBlock, totalFreeSpace
    
def compactFile(fileBlock, freeSpace):
    compactedFile = []
    rhsCounter = 1

    for i in range(len(fileBlock)):
        if fileBlock[i] == ".":
            while fileBlock[-rhsCounter] == ".":
                rhsCounter += 1
            compactedFile.append(fileBlock[-rhsCounter])
            # compactedFile += fileBlock[-rhsCounter]

            rhsCounter += 1

            if rhsCounter > freeSpace:
                break
        else:           
            compactedFile.append(fileBlock[i])

    [compactedFile.append(j) for j in fileBlock[i+1:-rhsCounter + 1]]
    # compactedFile.append(fileBlock[i+1:-rhsCounter + 1])

    return compactedFile
            

def calcCheckSum(compactedFile):
    checkSum = 0
    
    for i in range(len(compactedFile)):
        if compactedFile[i] != ".":
            checkSum += i * int(compactedFile[i])

    return checkSum


def createFreeSpaceDict(diskMap):
    freeSpaces = [int(diskMap[i]) for i in range(1, len(diskMap)-1, 2)]
    files = [int(diskMap[i]) for i in range(0, len(diskMap), 2)]

    # print(files, '\n', freeSpaces, '\n')
    # print(freeSpaces)
    freeSpaceDict = {}

    for i in range (len(files)-1, 0, -1):
        for j in range(0, i):
            if files[i] <= freeSpaces[j]:
                freeSpaces[j] -= files[i]

                if j not in freeSpaceDict:
                    freeSpaceDict[j] = [(i, files[i])]
                else:
                    freeSpaceDict[j] += [(i, files[i])]

                # if i not in freeSpaceDict:
                if i<len(freeSpaces) and freeSpaces[i] != 0 and i not in freeSpaceDict:
                    freeSpaces[i-1] += files[i] + freeSpaces[i]
                    freeSpaces[i] = 0
                else:
                    freeSpaces[i-1] += files[i]
                # else:
                #     freeSpaces[i-1] += files[i]
                # if i<len(freeSpaces) and freeSpaces[i] != 0:
                #     freeSpaces[i-1] += freeSpaces[i]
                #     freeSpaces[i] = 0
                
                # if i > len(freeSpaces)-1:
                #     freeSpaces.append(files[i])
                # else:
                #     freeSpaces[i] += files[i]
                
                files[i] = 0
                # print(freeSpaces, files)
                # print(files, '\n', freeSpaces, '\n')
                break
                
    return freeSpaceDict, freeSpaces, files

def compactFile2(freeSpaceDict, freeSpaces, files):
    compactedFile = []
    
    for i in range(len(files)):
        [compactedFile.append(i) for j in range(files[i])]

        if i in freeSpaceDict:
            for n, x in freeSpaceDict[i]:
                [compactedFile.append(n) for j in range(x)]

        if i < len(freeSpaces) and freeSpaces[i] != 0:
            [compactedFile.append('.') for j in range(freeSpaces[i])]
    
    return compactedFile


def problem1():
    # diskMap = openFile("example9")
    # diskMap = openFile("input9")
    diskMap = openFile("example9.2")

    fileBlock, freeSpace = getFileBlock(diskMap[0])
    print(fileBlock)

    compactedFile = compactFile(fileBlock, freeSpace)
    # print(compactedFile)

    checkSum = calcCheckSum(compactedFile)
    print(checkSum)

def problem2():
    # diskMap = openFile("example9")
    diskMap = openFile("input9")
    # diskMap = openFile("example9.1")
    # diskMap = openFile("example9.2")

    freeSpaceDict, freeSpaces, files = createFreeSpaceDict(diskMap[0])
    # print(freeSpaces, files, freeSpaceDict)
    # print(freeSpaceDict)

    compactedFile = compactFile2(freeSpaceDict, freeSpaces, files)
    # print(compactedFile)
    with open('output.txt', 'w') as file:
        # Write the checksum to the file
        file.write(str(compactedFile))

    checkSum = calcCheckSum(compactedFile)
    print(checkSum)



problem2()
# problem1()


# testL = []
# num =1 
# # for i in range(5):
# [testL.append(num) for j in range(5)]

# print(testL)