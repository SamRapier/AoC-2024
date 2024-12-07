def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
operators = ["+", "*", "||"]

def getEquations(file):
    equations = []
    for line in file:
        target = int(line.split(": ")[0])
        values = [int (x) for x in line.split(": ")[1].split(" ")]
        equations.append((target, values))
        # print(line.split(": "))
    return equations

def func2(target, total, index, values, operationList):
    if index == len(values):
        return total == target
    
    for operator in operators:
        if operator == "||":
            runningTotal = int(str(total) + str(values[index]))
        else:
            runningTotal = eval(f"{total} {operator} {values[index]}")

        if func2(target, runningTotal, index+1, values, operationList+[operator]):
            return True
    
    return False


def processEquations(equations):
    sumTargets = 0
    for target, values in equations:
        if func2(target, values[0], 1, values, []):
            # print(target)
            sumTargets += target
    
    print(sumTargets)


def main():
    # file = openFile("example7")
    file = openFile("input7")
    equations = getEquations(file)
    processEquations(equations)



main()

# print(func1(191, [10, 19]))
# print(eval("10 || 19"))
# print(int(str(10) + str("19")))
# print(func2(19, 10, 1, [10, 19], []))