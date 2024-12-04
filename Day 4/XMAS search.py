# Time Complexity - O(n * m)
# Space Complexity - O(n * m)

puzzle = []
total = 0

def check(word, grid, x, y):
    total = 0
    wordLength = len(word)
    gridLength = len(grid)
    directions = [[0,-1], # Up
                  [1,-1], # Upper-right
                  [1,0],  # Right
                  [1,1],  # Bottom-right
                  [0,1],  # Bottom
                  [-1,1], # Bottom-left
                  [-1,0], # Left
                  [-1,-1]]# Upper-left
    
    # Check all directions for word
    for direction in directions:
        dx = x
        dy = y
        # Check for word
        for i in range(wordLength):
            if not (0 <= dx < gridLength and 0 <= dy < gridLength):
                break
            if word[i] != grid[dx][dy]:
                break

            dx += direction[0]
            dy += direction[1]
            
        else:
            total += 1

    return total


with open('.\\Day 4\\input2.txt') as input:
    for line in input:
        puzzle.append(line)


for y, line in enumerate(puzzle):
    for x in range(len(line)):
        if puzzle[y][x] == "X":
                total += check("XMAS", puzzle, y, x)

print(total)