def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()

def findStartingNode(searchSpace, letter):
    letterLocations = []
    for i in range(len(searchSpace)):
        for j in range(len(searchSpace[i])):
            if searchSpace[i][j] == letter:
                letterLocations.append((i, j))
    return letterLocations

def findTrail(searchSpace, x, y, searchNode, trailheads: list, rating):

    if searchNode == 10:
        # print(x, y)
        rating += 1
        if type(trailheads) != list:
            return [(x, y)], rating
        else:
            if (x, y) not in trailheads:
                return trailheads.append((x, y)), rating
            else:
                return trailheads, rating
        
    
    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if x + i >= 0 and x + i < len(searchSpace) and y + j >= 0 and y + j < len(searchSpace[0]):
            if searchSpace[x + i][y + j] == str(searchNode):
                _, rating = findTrail(searchSpace, x + i, y + j, searchNode + 1, trailheads, rating)

    return trailheads, rating
    

def mainLoop(searchSpace, startingNodes):
    totalTrailheads = 0
    totalRating = 0
    for x, y in startingNodes:
        trailheads = []
        rating = 0
        # print(x, y)
        trailheads, rating = findTrail(searchSpace, x, y, 1, trailheads, rating)
        print(trailheads)
        print(rating)
        # print(len(trailheads))
        totalRating += rating
        if type(trailheads) == list:
            totalTrailheads += len(trailheads)
        
        print(totalTrailheads, totalRating)

    
    print(totalTrailheads, totalRating)




def problem1():
    # searchSpace = openFile("example10")
    searchSpace = openFile("input10")

    startingNodes = findStartingNode(searchSpace, "0")
    mainLoop(searchSpace, startingNodes)


def problem2():
    pass

problem1()