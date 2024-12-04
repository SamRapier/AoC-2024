import re

def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
def handleCorruptMemory(memory):
    regexPattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    instructionList = []
    for m in memory:
        instructionList += (re.findall(regexPattern, m))

    return instructionList

def mul(a, b):
    return a * b

def processInstructions(memory):
    sum = 0
    skip = False
    for instruction in memory:
        if instruction == "do()":
            skip = False
            continue    
        
        if skip:
            continue

        if instruction == "don't()":
            skip = True
            continue
        
        print(instruction)

        instruction = instruction.replace("mul(", "")
        instruction = instruction.replace(")", "")
        instruction = instruction.split(",")
        sum += mul(int(instruction[0]), int(instruction[1]))

    return sum

def problem1():
    # corruptedMemory = openFile("example3")
    # corruptedMemory = openFile("example3.2")
    corruptedMemory = openFile("input3")
    cleanMemory = handleCorruptMemory(corruptedMemory)
    print(cleanMemory)
    sum = processInstructions(cleanMemory)
    print(sum)

problem1()