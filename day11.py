def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()

from functools import lru_cache

@lru_cache(maxsize=None)
def applyRules(num):
    if num == 0:
        return 1, None
    elif len(str(num)) % 2 == 0:
        strNum = str(num)
        halfPoint = len(strNum) // 2
        # print(strNum)
        stone1 = int(strNum[:halfPoint])
        stone2 = int(strNum[halfPoint:])
        return stone1, stone2
    else:
        return num*2024, None
    
def splitStones(file):
    return [int(x) for x in file[0].split(" ")]

from collections import defaultdict
def splitStones2(file):
    stones = defaultdict(int)
    for stone in file[0].split():
        stone = int(stone)
        stones[stone] += 1

    return stones

def processStones(stones):
    newStones = []
    for stone in stones:
        stone1, stone2 = applyRules(stone)
        if stone2 is not None:
            # print(stone1, stone2)
            newStones.append(stone1)
            newStones.append(stone2)
        else:
            newStones.append(stone1)

    return newStones

def mainLoop1(stones, n):
    for i in range(n):
        stones = processStones(stones)
        # print(stones)
    
    print(len(stones))

def processStones1(stones):
    count = 0
    for stone in stones:
        stone1, stone2 = applyRules(stone)
        if stone2 is not None:
            count += 2
        else:
            count += 1

    return count

def recursion(stone, index, count, memo):
    if index == 0:
        return count + 1
    stone1, stone2 = applyRules(stone)
    if stone2 == None:
        count = recursion(stone1, index-1, count, memo)
    else:
        count = recursion(stone1, index-1, count, memo)
        count = recursion(stone2, index-1, count, memo)
    return count


def depthFirstSearch(stones, n):
    stack = list(stones)
    count = 0
    for _ in range(n):
        newStack = []
        while stack:
            stone = stack.pop()
            stone1, stone2 = applyRules(stone)
            newStack.append(stone1)
            if stone2 is not None:
                newStack.append(stone2)
        stack = newStack

    print(len(stack))


from collections import deque
def breadthFirstSearch(stones, n):
    queue = deque(stones)
    for _ in range(n):
        level_size = len(queue)
        for _ in range(level_size):
            stone = queue.popleft()
            stone1, stone2 = applyRules(stone)
            queue.append(stone1)
            if stone2 is not None:
                queue.append(stone2)
    print(len(queue))





def mainLoop2(stones, n):
    count = 0
    for stone in stones:
        count += recursion(stone, n, 0, {})
        # print(count)

    print(count)
    return count

def mainLoop3(stones, n):
    for i in range(n):
        stones = blink(stones)
        print(i, len(stones))

    # print(len(stones))
    return stones

def blink(stones):
    stones2 = dict(stones)
    for stone, count in stones2.items():
        if count == 0: 
            continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif  len(str(stone)) % 2 == 0:
            strNum = str(stone)
            halfPoint = len(strNum) // 2
            stone1 = int(strNum[:halfPoint])
            stone2 = int(strNum[halfPoint:])
            stones[stone1] += count
            stones[stone2] += count
            stones[stone] -= count
        else:
            stones[stone*2024] += count
            stones[stone] -= count
    return stones


def problem1():
    # file = openFile("example11")
    file = openFile("input11")

    stones = splitStones(file)
    print(stones)
    mainLoop1(stones, 35)

def problem2():
    # file = openFile("example11")
    file = openFile("input11")

    stones = splitStones2(file)
    # print(stones)
    stones = mainLoop3(stones, 75)
    # print(stones)

    sum = 0
    for value in stones.values():
        sum += value
    
    print(sum)
    # depthFirstSearch(stones, 40)
    # breadthFirstSearch(stones, 75)
    # print(stones)
    # count = mainLoop2(stones, 40)



# problem2()
problem2()