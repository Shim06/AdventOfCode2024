# Time Complexity - O((n * m)^2)
# Space Complexity - O(n * m)

import copy
total = 0
map = []
startingPosition = []
direction = [[0, -1], # Facing Up
             [1, 0],  # Facing Right
             [0, 1],  # Facing Down
             [-1, 0]] # Facing Left

def check(position, grid):
    turning = False
    intersect = 0
    facing = 0 
    gridSize = len(grid)
    while 0 <= position[0] < mapSize and 0 <= position[1] < mapSize:
        if grid[position[0]][position[1]] == "X" and not turning:
            intersect += 1
        elif not turning:
            grid[position[0]][position[1]] = "X"

        if intersect > gridSize:
            return False
        
        front_x = position[0] + direction[facing][1]
        front_y = position[1] + direction[facing][0]
        if (front_x < 0 or front_x >= mapSize) or (front_y < 0 or front_y >= mapSize):
            return True

        front = grid[position[0] + direction[facing][1]][position[1] + direction[facing][0]]
        if front == "#":
            facing += 1
            turning = True
            if facing >= 4: facing = 0
        else:
            if front != "X": 
                intersect = 0
            turning = False
            position[0] += direction[facing][1]
            position[1] += direction[facing][0]


with open('.\\Day 6\\input.txt') as input:
    #lines = input.readlines()
    for y, line in enumerate(input):
        currentLine = []
        for x, c in enumerate(line):
            if c == "\n":
                continue
            currentLine.append(c)
            if c == "^":
                startingPosition = [y, x]
        map.append(currentLine)

mapSize = len(map)
mapCopy = copy.deepcopy(map)
position = copy.deepcopy(startingPosition)
check(position, map)

for y, line in enumerate(map):
    for x, c in enumerate(line):
        if c == "X":
            if startingPosition == [y, x]:
                continue
            position = copy.copy(startingPosition)
            map2 = copy.deepcopy(mapCopy)
            map2[y][x] = "#"
            if not check(position, map2):
                total += 1

print(total)