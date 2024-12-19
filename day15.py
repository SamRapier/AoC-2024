def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
instructionSet = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

def getMapAndInstructions(file):
    map = []
    instructions = []
    for i in range(len(file)):
        if "" == file[i]:
            break
        map.append(list(file[i]))
    for j in range(i+1, len(file)):
        instructions += file[j]
    return map, instructions

def increaseMap(map):
    newMap = [['.' for i in range(len(map[0])*2)] for j in range(len(map))]
    for i in range(len(map)):
        jCounter = 0
        for j in range(len(map[i])):
            if map[i][j] == '#':
                    newMap[i][jCounter] = '#'
                    newMap[i][jCounter+1] = '#'
                    jCounter += 2
            if map[i][j] == 'O':
                newMap[i][jCounter] = '['
                newMap[i][jCounter+1] = ']'
                jCounter += 2
            if map[i][j] == '.':
                newMap[i][jCounter] = '.'
                newMap[i][jCounter+1] = '.'
                jCounter += 2
            if map[i][j] == '@':
                newMap[i][jCounter] = '@'
                newMap[i][jCounter+1] = '.'
                jCounter += 2
    return newMap

def findRobot(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '@':
                return (i, j)
            
from copy import deepcopy
def updateMap(map, instruction, rx, ry, piece='@', prevPiece='.'):
    cx = rx + instructionSet[instruction][0]
    cy = ry + instructionSet[instruction][1]
    checkSquare = map[cx][cy]

    if checkSquare == '#':
        return map, False

    if checkSquare == '.':
        map[cx][cy] = piece
        map[rx][ry] = prevPiece
        return map, True
    
    if (checkSquare == '[' or checkSquare == ']') and (instruction == '^' or instruction == 'v'):
        if (checkSquare == '['):
            map_ = deepcopy(map)
            map, moved1 = updateMap(map, instruction, cx, cy, checkSquare, piece)
            if not moved1:
                return map_, False
            if piece == '@':
                map, moved2 = updateMap(map, instruction, cx, cy+1, ']', '.')
            else:
                # map, moved2 = updateMap(map, instruction, cx, cy+1, ']', map[rx][ry+1])
                map, moved2 = updateMap(map, instruction, cx, cy+1, ']', '.')

            if moved1 and moved2:
                map[cx][cy] = piece
                map[rx][ry] = prevPiece
                return map, True
            else:
                return map_, False
            
        else:
            map_ = deepcopy(map)
            map, moved1 = updateMap(map, instruction, cx, cy, checkSquare, piece)
            if not moved1:
                return map_, False
            if piece == '@':
                map, moved2 = updateMap(map, instruction, cx, cy-1, '[', '.')
            else:
                # map, moved2 = updateMap(map, instruction, cx, cy-1, '[', map[rx][ry-1])
                map, moved2 = updateMap(map, instruction, cx, cy-1, '[', '.')

            if moved1 and moved2:
                map[cx][cy] = piece
                map[rx][ry] = prevPiece
                return map, True
            else:
                return map_, False

    if checkSquare == 'O' or checkSquare == '[' or checkSquare == ']':  
        map, moved = updateMap(map, instruction, cx, cy, checkSquare, piece)
        if moved:
            map[cx][cy] = piece
            map[rx][ry] = prevPiece
            return map, True
        else:
            return map, False

    return map, True

def printMap(map):
    for i in range(len(map)):
        print(''.join(map[i]))

def moveRobot(map, instructions, robot):
    count = 0
    for instruction in instructions:
        map, moved = updateMap(map, instruction, robot[0], robot[1])
        if moved:
            x = robot[0] + instructionSet[instruction][0]
            y = robot[1] + instructionSet[instruction][1]
            robot = (x, y)
        count += 1
        # print(instruction, count)
        # printMap(map)
        # print()
    return map
    
def calculateSumGPS(map):
    totalBoxSums = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O' or map[i][j] == '[':    
                totalBoxSums += (100 * i) + j

    print(totalBoxSums)

def main():
    # file = openFile("example15")
    # file = openFile("example15.2
    # file = openFile("example15.3")
    file = openFile("input15")
    map, instructions = getMapAndInstructions(file)
    newMap = increaseMap(map)

    map = newMap
    printMap(map)
    print()
    # print(instructions)
    robot = findRobot(map)
    # print(robot)
    map = moveRobot(map, instructions, robot)
    printMap(map)
    calculateSumGPS(map)


main()