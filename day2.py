def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
def splitReport(inputList):
    reports = []
    for i in inputList:
        reports.append(([int(x) for x in i.split(" ")]))
    return reports

def check(acsending, level1, level2):
    if level1 == level2:
        return False
    if acsending == True and level1 > level2:
        return False
    elif acsending == False and level1 < level2:
        return False
    elif abs(level1 - level2) > 3:
        return False

def checkReport(report):
    if report[0] < report[1]:
        acsending = True
    else:
        acsending = False

    for i in range(len(report) -1):
        if check(acsending, report[i], report[i+1]) == False:
            return False, i

    return True, 0

def safetyReport(reports):
    safetyCount = 0
    for report in reports:
        safe, _ = checkReport(report)
        if safe:
            safetyCount += 1
    return safetyCount

def safetyReport2(reports):
    safetyCount = 0

    for report in reports:
        safe, index = checkReport(report)

        if safe == True:
            safetyCount += 1

        else:
            report1 = report.copy()
            report2 = report.copy()
            report3 = report.copy()

            report1.pop(index-1)
            report2.pop(index)
            report3.pop(index+1)

            retrySafe1, _ = checkReport(report1)
            retrySafe2, _ = checkReport(report2)
            retrySafe3, _ = checkReport(report3)

            if retrySafe1 == True:
                safetyCount += 1
            elif retrySafe2 == True:
                safetyCount += 1
            elif retrySafe3 == True:    
                safetyCount += 1

            

    return safetyCount

def problem1():
    reports = openFile("input2")
    reports = splitReport(reports)
    print(safetyReport(reports))

def problem2():
    reports = openFile("input2")
    reports = splitReport(reports)
    print(safetyReport2(reports))

problem2()

