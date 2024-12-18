def openFile(fileName):
    with open(f"inputs/{fileName}.txt", 'r') as file:
        return file.read().splitlines()
    
import re
def initiateRobots(file):
    robots = []
    for i in range(len(file)):
        regexPattern = r'[\-0-9]+,[\-0-9]+'
        data = re.findall(regexPattern, file[i])
        position = [int(x) for x in data[0].split(",")]
        velocity = [int(x) for x in data[1].split(",")]
        robots.append({"position": position, "velocity": velocity})
    return robots



def moveRobot(robot):

    robot["position"][0] += robot["velocity"][0]
    robot["position"][1] += robot["velocity"][1]

    if robot["position"][0] >= maxX:
        robot["position"][0] -= maxX 
    if robot["position"][0] < 0:
        robot["position"][0] += maxX

    if robot["position"][1] >= maxY:
        robot["position"][1] -= maxY 
    if robot["position"][1] < 0:
        robot["position"][1] += maxY

    return robot

def simulate(robots):
    for i in range(seconds):
        for robot in robots:
            robot = moveRobot(robot)
        plot_positions(robots, i)
    return robots

import math
def countQuadrants(robots):
    quadrants = {1:0, 2:0, 3:0, 4:0}
    halfX = math.floor(maxX/2)
    halfY = math.floor(maxY/2)
    for robot in robots:
        if robot["position"][0] < halfX and robot["position"][1] < halfY:
            quadrants[1] += 1
        elif robot["position"][0] > halfX and robot["position"][1] < halfY:
            quadrants[2] += 1
        elif robot["position"][0] < halfX and robot["position"][1] > halfY:
            quadrants[3] += 1
        elif robot["position"][0] > halfX and robot["position"][1] > halfY:
            quadrants[4] += 1

    safetyFactor = 1
    for robots in quadrants.values():
        if robots != 0:
            safetyFactor *= robots
    
    print(safetyFactor)
    return safetyFactor

def simulate2(robots, time):
    for robot in robots:
        pos = robot["position"]
        vel = robot["velocity"]
        pos[0] = (pos[0]+time*vel[0]) % maxX
        pos[1] = (pos[1]+time*vel[1]) % maxX
        robot = {"position": pos, "velocity": vel}
    return robots

import matplotlib.pyplot as plt
# Plot positions
def plot_positions(robots, second):
    plt.figure()
    x = [robot['position'][0] for robot in robots]
    y = [robot['position'][1] for robot in robots]
    plt.scatter(x, y)
    plt.title(f'Robot Positions at Second {second}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.show()


seconds = 100
def update_positions(robots):
    for robot in robots:
        pos = robot["position"]
        vel = robot["velocity"]
        pos[0] = (pos[0] + vel[0]) % maxX
        pos[1] = (pos[1] + vel[1]) % maxY
        robot['position'] = pos

import numpy as np
# Calculate entropy
def calc_entropy(robots, w, h):
    grid = np.zeros((h, w), dtype=int)
    for robot in robots:
        x, y = robot['position']
        grid[y, x] += 1
    counts = np.bincount(grid.flatten())
    probs = counts[counts > 0] / counts.sum()
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

# Animation function
def animate(frame, robots, scatter, ax,entropies):
    update_positions(robots)
    x = [robot['position'][0] for robot in robots]
    y = [robot['position'][1] for robot in robots]
    scatter.set_offsets(list(zip(x, y)))
    ax.set_title(f'Robot Positions at Frame {frame}')

    # Calculate and store entropy
    entropy = calc_entropy(robots, maxX, maxY)
    entropies.append(entropy)

    return scatter,

from matplotlib.animation import FuncAnimation

def visualise(robots):
    
    fig, ax = plt.subplots()
    x = [robot['position'][0] for robot in robots]
    y = [robot['position'][1] for robot in robots]
    scatter = ax.scatter(x, y)
    ax.set_xlim(-1, maxX)
    ax.set_ylim(-1, maxY)
    # ax.set_title('Robot Positions Over Time')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.grid(True)

    entropies = []
    ani = FuncAnimation(fig, animate, frames=7092, fargs=(robots, scatter, ax, entropies), interval=1, repeat=False)
    plt.show()
    # print(robots)

    # Identify the frame with the lowest entropy
    min_entropy_frame = np.argmin(entropies)
    print(f'Frame with the lowest entropy: {min_entropy_frame}')
    print(f'Lowest entropy value: {entropies[min_entropy_frame]}')


# def calc_entropy(pos, w, h):
#     grid = np.zeros((h, w), dtype=int)
#     np.add.at(grid, (pos[:,1], pos[:,0]), 1)
#     counts = np.bincount(grid.flatten())
#     probs = counts[counts > 0] / counts.sum()
#     entropy = -np.sum(probs * np.log2(probs))
#     return entropy

# maxX = 11
# maxY = 7

maxX = 101
maxY = 103
def main():
    # file = openFile("example14")
    file = openFile("input14")
    initrobots = initiateRobots(file)

    visualise(initrobots)

    # robots1 = simulate(initrobots)
    # robtos2 = simulate2(initrobots, seconds)
    # if robots1 == robtos2:
    #     print("They are the same")
    # countQuadrants(robots)
    # print(robots)

   
    


main()

# robot = {"position": [2, 4], "velocity": [2, -3]}
# for i in range(5):
#     robot = moveRobot(robot)
#     print(robot)

# print(maxX/2)
# print(math.ceil(maxY/2))

