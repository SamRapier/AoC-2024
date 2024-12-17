def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
import re
def readPuzzle(file):
    puzzles = []
    converstionErrorLOL = 10000000000000
    for i in range(0, len(file), 4):
        regexPattern = "[0-9]+"
        vector1 = [int(x) for x in re.findall(regexPattern, file[i])]
        vector2 = [int(x) for x in re.findall(regexPattern, file[i+1])]
        target = [int(x) + converstionErrorLOL for x in re.findall(regexPattern, file[i+2])]

        puzzle = {"vector1": vector1, "vector2": vector2, "target": target}
        puzzles.append(puzzle)
    return puzzles
    
import math
def checkIfPossible(v1, v2, t):
    gcdX = math.gcd(v1[0], v2[0])
    gcdY = math.gcd(v1[1], v2[1])

    if t[0] % gcdX == 0 and t[1] % gcdY == 0:
        return gcdX, gcdY
    else:
        return None, None

def getCoefficients(a, b):
    x0, y0 = 1, 0   
    x1, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return x0, y0


def solve_diophantine(v1, v2, t, gcdX, gcdY):
    x0_x, y0_x = getCoefficients(v1[0], v2[0])
    x0_y, y0_y = getCoefficients(v1[1], v2[1])

    print(f"Initial coefficients for x: {x0_x}, {y0_x}")
    print(f"Initial coefficients for y: {x0_y}, {y0_y}")

    # Scale the coefficients to match the target values
    x0_x *= t[0] // gcdX
    y0_x *= t[0] // gcdX
    x0_y *= t[1] // gcdY
    y0_y *= t[1] // gcdY

    print(f"Scaled coefficients for x: {x0_x}, {y0_x}")
    print(f"Scaled coefficients for y: {x0_y}, {y0_y}")

    # Find the correct combination of a and b
    for k in range(-9, 1000):
        a = x0_x + k * (v2[0] // gcdX)
        b = y0_x - k * (v1[0] // gcdX)

        if a >= 0 and b >= 0 and a * v1[0] + b * v2[0] == t[0] and a * v1[1] + b * v2[1] == t[1]:
            return a, b

    return None, None

def processPuzzles(puzzles):
    costA, costB = 3, 1
    totalCost = 0
    for puzzle in puzzles:
        v1 = puzzle["vector1"]
        v2 = puzzle["vector2"]
        t = puzzle["target"]

        gcdX, gcdY = checkIfPossible(v1, v2, t)
        if gcdX is not None:
            a, b = usingEquations(v1, v2, t)
            print(a,b)
            if a is None:
                print("No solution")
                continue
            print(f"Cost = {a * costA + b * costB}")
            totalCost += a * costA + b * costB
        else:
            print("No solution")
    print(totalCost)

def usingEquations(v1, v2, t):
    a1 = (t[0] * v2[1] - t[1] * v2[0])
    a2 = (v1[0] * v2[1] - v1[1] * v2[0])

    if a1 % a2 != 0:
        return None, None
    a = a1 / a2
    b = (t[0] - v1[0] * a) / v2[0]
    return a, b

def main():
    # file = openFile("example13")
    file = openFile("input13")
    puzzles = readPuzzle(file)
    print(puzzles)
    processPuzzles(puzzles)

# Example usage
# v1 = [94, 34]
# v2 = [22, 67]
# t = [8400, 5400]
# print(usingEquations(v1, v2, t))

main()
