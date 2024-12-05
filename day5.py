import math
def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    

def splitRulesUpdates(file):
    splitIndex = file.index("")

    rules = file[:splitIndex]
    updates = file[splitIndex+1:]

    return rules, updates

def getRulesDict(rules):
    rulesDict = {}

    for rule in rules:
        _rule=[int(x) for x in rule.split("|")]

        if _rule[0] in rulesDict:
            rulesDict[_rule[0]].append(_rule[1])
        else:
            rulesDict[_rule[0]] = [_rule[1]]
        
    return rulesDict

def checkRules(rulesDict, num1, num2):
    if num1 in rulesDict and num2 in rulesDict[num1]:
        return True
    else:
        # print(f"Rule not found: {num1} -> {num2}")
        return False
    

def validateUpdate(rulesDict, update):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if not checkRules(rulesDict, update[i], update[j]):
                return False
        
    return True

def checkUpdates(rulesDict, updates):
    validUpdates = 0

    for update in updates:
        # _update = update.split(",")
        _update = [int(x) for x in update.split(",")]

        if validateUpdate(rulesDict, _update):
            middle = math.floor(len(_update) / 2)
            validUpdates += _update[middle]

    return validUpdates

def correctUpdates(rulesDict, update):
    corrected = False
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if not checkRules(rulesDict, update[i], update[j]):
                corrected = True
                _update = update[i]
                update[i] = update[j]
                update[j] = _update

    return corrected, update

def checkUpdates2(rulesDict, updates):
    validUpdates = 0

    for update in updates:
        # _update = update.split(",")
        _update = [int(x) for x in update.split(",")]

        corrected, correctUpdate = correctUpdates(rulesDict, _update)
        if corrected:
            middle = math.floor(len(correctUpdate) / 2)
            validUpdates += correctUpdate[middle]

    return validUpdates

def problem1():
    # file = openFile("example5")
    file = openFile("input5")

    rules, updates = splitRulesUpdates(file)
    rulesDict = getRulesDict(rules)
    # print(rulesDict)
    print(checkUpdates(rulesDict, updates))

def problem2():
    # file = openFile("example5")
    file = openFile("input5")

    rules, updates = splitRulesUpdates(file)
    rulesDict = getRulesDict(rules)
    # print(rulesDict)
    print(checkUpdates2(rulesDict, updates))


problem2()