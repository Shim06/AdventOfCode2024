# Time Complexity - O(n * m)
# Space Complexity - O(n * m)

puzzle = []
total = 0

def check(grid, x, y):
    left = right = False
    gridLength = len(grid)

    leftLine = [[1,1],   # Bottom-right
            [-1,-1]] # Upper-left
    
    rightLine = [[1,-1], # Upper-right
             [-1,1]] # Bottom-left
    lines = [leftLine, rightLine]

    
    # Check all directions for word  
    for i, directions in enumerate(lines):
        S = 0
        M = 0  
        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]
            if not (0 <= dx < gridLength and 0 <= dy < gridLength):
                break
            if grid[dx][dy] == "S":
                S += 1
            if grid[dx][dy] == "M":
                M += 1
            if S == 1 and M == 1:
                if i == 0:
                    left = True
                else:
                    right = True

        if left and right:
            return 1

    return 0


with open('.\\Day 4\\input.txt') as input:
    for line in input:
        puzzle.append(line)


for y, line in enumerate(puzzle):
    for x in range(len(line)):
        if puzzle[y][x] == "A":
                total += check(puzzle, y, x)

print(total)