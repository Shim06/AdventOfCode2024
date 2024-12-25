import time

def main():
    total = 0
    start_time = time.time()
    map = []
    with open(".\\Day 12\\input.txt") as input:
        for line in input:
            line = line.split()
            for i in line:
                map.append(i)

    # Initialize visited matrix
    visited = []
    for y, line in enumerate(map):
        temp = []
        for x in range(len(line)):
            temp.append(False)
        visited.append(temp) 

    for y, line in enumerate(map):
        for x in range(len(line)):
            area, perimeter = dfs(map, visited, y, x, map[y][x])
            total += area * perimeter
    print(f"Total price: {total}")

    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")

def dfs(grid:list[list[int]], visited:list[list[bool]], x:int, y:int, type:int) -> int:
    directions = [[1, 0], # Up
                  [0, 1], # Right
                  [-1, 0],# Down
                  [0, -1]]# Left
    
    if visited[x][y]:
        return 0, 0
    visited[x][y] = True

    rows = len(grid)
    cols = len(grid[0])
    area = 1
    sides = 0

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if 
                added_area, added_perimeter = dfs(grid, visited, new_x, new_y, type)
                perimeter += added_perimeter
                area += added_area

    return area, sides
      

if __name__ == "__main__":
    main()