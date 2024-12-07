# Time Complexity - O(n * m)
# Space Complexity - O(n * m)

total = 0
map = []
position = []
facing = 0
direction = [[0, -1], # Facing Up
             [1, 0],  # Facing Right
             [0, 1],  # Facing Down
             [-1, 0]] # Facing Left

with open('.\\Day 6\\input.txt') as input:
    #lines = input.readlines()
    for y, line in enumerate(input):
        currentLine = []
        for x, c in enumerate(line):
            if c == ".":
                currentLine.append(c)
            elif c == "#":
                currentLine.append(c)
            elif c == "^":
                position = [y, x]
                currentLine.append(c)
        map.append(currentLine)

mapSize = len(map)
while 0 <= position[0] < mapSize and 0 <= position[1] < mapSize:
    map[position[0]][position[1]] = "X"
    front_x = position[0] + direction[facing][1]
    front_y = position[1] + direction[facing][0]
    if (front_x < 0 or front_x >= mapSize) or (front_y < 0 or front_y >= mapSize):
        break 

    front = map[position[0] + direction[facing][1]][position[1] + direction[facing][0]]
    if front == "#":
        facing += 1
        if facing >= 4: facing = 0
    else:
        position[0] += direction[facing][1]
        position[1] += direction[facing][0]

for line in map:
    for c in line:
        if c == "X":
            total += 1

print(total)