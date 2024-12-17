def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def checkPerimeter(map, x, y, plant):
    perimeterSquares = []
    for (i, j) in directions:
        if map[y + i][x + j] == plant:
            perimeterSquares.append((x + j, y + i))
    
    return perimeterSquares

# loop through each square
# for square not visited
    # set to visited
    # calc perimeters
    # for each similar plant from perimeter
    # recursively check all similar but not visited/in region
    # storing visited squares and plants in region
    # return perimeter calc and area and store visited

def traverseMap(map):
    visited = []
    totalFencePrice = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) in visited:
                continue
            plant = map[i][j]
            sides = {
                (1, 0): [],
                (0, 1): [],
                (-1, 0): [],
                (0, -1): []
            }

            region, regionPerimeter, sides = findRegion(map, i, j, plant, [(i, j)], 0, sides)

            visited += region
            regionArea = len(region)
            fencePrice1 = regionArea * regionPerimeter
            numberSides = caclSides(sides)
            fencePrice2 = regionArea * numberSides
            # print(f"Region {plant}: {regionArea} * {regionPerimeter} = {fencePrice1}")
            print(f"Region {plant}: {regionArea} * {numberSides} = {fencePrice2}")
            totalFencePrice += fencePrice2
    print(f"\nTotal: {totalFencePrice}")

def findRegion(map, x, y, plant, region, perimeter, sides):
    for (i, j) in directions:
        checkPosition = (x + i, y + j)

        if x + i < 0 or y + j < 0 or x + i >= len(map[0]) or y + j >= len(map):
            perimeter += 1
            sides[(i, j)].append(checkPosition)
            continue

        newPlant = map[x + i][y + j]

        if newPlant == plant and checkPosition not in region:
            region.append(checkPosition)
            region, perimeter, sides = findRegion(map, x + i, y + j, plant, region, perimeter, sides)

        if newPlant != plant:
            perimeter += 1
            sides[(i, j)].append(checkPosition)

    return region, perimeter, sides

def caclSides(sides):
    sidesCount = 0
    for (i, j), squares in sides.items():
        if i == 0:
            m, n = (1, 0)
        else:
            m, n = (0, 1)

        currSides = {}
        squares.sort()
        for (a, b) in squares:
            currSides[(a, b)] = []
            x, y = a, b
            while (x + m, y + n) in squares:
                currSides[(a, b)].append((x + m, y + n))
                squares.remove((x + m, y + n))
                x += m
                y += n
                if len(squares) == 0:
                    break
        
        sidesCount += len(currSides)
    return sidesCount

def problem():
    # file = openFile("example12.1")
    # file = openFile("example12.2")
    # file = openFile("example12.3")
    # file = openFile("example12.4")
    # file = openFile("example12.5")
    file = openFile("input12")

    traverseMap(file)


problem()