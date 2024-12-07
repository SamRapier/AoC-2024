def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()


directionMap = {
    "up": [-1, 0],
    "right": [0, 1],
    "down": [1, 0],
    "left": [0, -1]
}

def turnRight(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"
    else:
        return False
    
def locateGuard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in ("^", "V", "<", ">"):
                return [i, j], map[i][j]
    return False

def identifyDirection(direction):
    if direction == "^":
        return "up"
    elif direction == "V":
        return "down"
    elif direction == "<":
        return "left"
    elif direction == ">":
        return "right"
    else:
        return False
    

def getNextPosition(guard, direction):
    return [guard[0] + directionMap[direction][0], guard[1] + directionMap[direction][1]]

def lookAhead(map, guard, direction, positions, positionMap, path, extraObsticle = []):
    path.append([guard, direction])
    positionMap[direction].append(guard)

    # nextPosition = [guard[0] + directionMap[direction][0], guard[1] + directionMap[direction][1]]
    nextPosition = getNextPosition(guard, direction)
    if nextPosition[0] < 0 or nextPosition[0] >= len(map):
        return guard, direction, positions, positionMap, False, path
        
    if nextPosition[1] < 0 or nextPosition[1] >= len(map[0]):
        return guard, direction, positions, positionMap, False, path
    
    if map[nextPosition[0]][nextPosition[1]] == "#":
        direction = turnRight(direction)
        nextPosition = getNextPosition(guard, direction)
        path.append([guard, direction])
        positionMap[direction].append(guard)

    if extraObsticle != [] and nextPosition == extraObsticle:
        direction = turnRight(direction)
        nextPosition = getNextPosition(guard, direction)
        path.append([guard, direction])
        positionMap[direction].append(guard)
    
    guard = nextPosition
    if guard not in positions:
        positions.append(guard)


    return guard, direction, positions, positionMap, True, path



import copy
def plotRoute(map, guard, direction):
    positions = [guard]
    positionMap = {
        "right": [],
        "left": [],
        "up": [],
        "down": []
    }
    obsticles = []
    path = []

    while True:
        guard, direction, positions, positionMap, inBounds, path = lookAhead(map, guard, direction, positions, positionMap, path)
        if not inBounds:
            break
        
        isObsticle, obsticles = checkLoops(map, guard, direction, positions[0], positions, positionMap, path, obsticles)
        

    return positions, obsticles 

def checkLoops(map, position, direction, startingPosition, positions, positionMap, path, obsticles: list):
    
    # for i in range(len(path)):
    #     position = path[i][0]
    #     direction = path[i][1]
    #     testObsticle = getNextPosition(position, direction)
    #     if testObsticle not in path or testObsticle == startingPosition:
    #             break

    # for direction, positions in positionMap.items():
    #     for position in positions:
            
    testObsticle = getNextPosition(position, direction)
    if testObsticle[0] < 0 or testObsticle[0] >= len(map):
        return False, obsticles
        
    if testObsticle[1] < 0 or testObsticle[1] >= len(map[0]):
        return False, obsticles
    
    if map[testObsticle[0]][testObsticle[1]] == "#":
        return False, obsticles
    
    if testObsticle == startingPosition: #or testObsticle not in path:
        return False, obsticles
        # break

    if testObsticle in obsticles:
        return False, obsticles
    
    testMap = copy.deepcopy(map)
    row = list(testMap[testObsticle[0]])
    row[testObsticle[1]] = "#"
    row[testObsticle[0]] = "".join(row)

    testDirection = turnRight(direction)
    testPositionMap = {
        "right": [],
        "left": [],
        "up": [],
        "down": []
    }
    testPath = []
    testPositions = []
    testGuard = position

    while True:
        
        testGuard, testDirection, testPositions, testPositionMap, inBounds, testPath = lookAhead(testMap, testGuard, testDirection, testPositions, testPositionMap, testPath)
        if not inBounds:
            break

        if testGuard in testPath:
            # print(testGuard, testObsticle)
            # print("current guard path:", path)
            # print("potential Obstical: ", testObsticle)
            # print("Tets Path: ", testPath)
            # print("intersection point: ", testGuard)
            # print("intersection direction: ", testDirection)
            # print("\n-----------------------\n")
            # print(obsticles)
           obsticles.append(testObsticle)
           
            
    
        
        
    return False, obsticles



def checkDirection(map, position, direction):
    if position[0] < 0 or position[0] >= len(map):
        return False
    if position[1] < 0 or position[1] >= len(map[0]):
        return False
    
    if map[position[0]][position[1]] == "#":
        direction = turnRight(direction)
    
    return direction


def runMap(map, position, direction):
    testedPath = []
    positions = []
    loop = False

    while True:
        if [position, direction] in testedPath:
            loop = True
            break

        newDirection = checkDirection(map, position, direction)
        if newDirection == False:
            loop = False
            break 
        elif newDirection != direction:
            if len(positions) == 0:
                break
            position = testedPath[-1][0]
            direction = newDirection

        testedPath.append([position, direction])
        if position not in positions:
            positions += [position]

        position = getNextPosition(position, direction)
        
        
        

    return testedPath, len(positions), loop

def runRoute(map, guardStart, direction):
    
    path, pathLength, loop = runMap(map, guardStart, direction)
    print("part1: ", pathLength, loop)
    # print(path)

    testedObsticles = [guardStart]
    obsticleCount = 0

    for i in range(len(path)):
        obsticlePos = path[i][0]
        if obsticlePos in testedObsticles:
            continue

        testStart = path[i-1][0]
        
        testMap = copy.deepcopy(map)
        testMap[obsticlePos[0]][obsticlePos[1]] = '#'
        # row = list(testMap[obsticlePos[0]])
        # row[obsticlePos[1]] = "#"
        # testMap[obsticlePos[0]] = "".join(row)
        testDir = turnRight(path[i-1][1])

        # testStart = getNextPosition(step[0], testDir)
        testedPath, testedPathLength, loop = runMap(testMap, testStart, testDir)

        if loop:
            obsticleCount += 1
            # print("Obsticle: ", obsticlePos)

        testedObsticles.append(obsticlePos)

        if i%100 == 0:
            print(i, obsticleCount)

    print("part2: ", obsticleCount)

    



def problem1():
    OGmap = openFile("example6")
    # OGmap = openFile("input6")
    map = []
    for row in OGmap:
        map.append(list(row))

    print(map)
    guard, directionIdentifier = locateGuard(map)
    direction = identifyDirection(directionIdentifier)

    positions, obsticles = plotRoute(map, guard, direction)
    print(len(positions))

def problem2():
    # OGmap = openFile("example6")
    OGmap = openFile("input6")
    map = []
    for row in OGmap:
        map.append(list(row))

    guard, directionIdentifier = locateGuard(map)
    direction = identifyDirection(directionIdentifier)

    # positions, obsticles = plotRoute(map, guard, direction)
    runRoute(map, guard, direction)

    # print(len(positions), len(obsticles))

problem2()
print("done")