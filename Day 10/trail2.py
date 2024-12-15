def main():
    map = []
    total = 0
    with open('.\\Day 10\\input.txt') as input:
        for y, line in enumerate(input):
            map.append(line.replace("\n",""))

    rows = len(map)
    cols = len(map[0])
    for y in range(rows):
        for x in range(cols):
            if map[y][x] == "0":
                total += dfs(map, y, x)
    print(f"Sum of trailheads: {total}")


def dfs(grid, x, y):
    if not grid:
        return 0
    if grid[x][y] == "9":
        return 1
    
    
    rating = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy

        if 0 <= next_x < rows and 0 <= next_y < cols:
            if int(grid[next_x][next_y]) == int(grid[x][y]) + 1:
                rating += dfs(grid, next_x, next_y)

    return rating

if __name__ == "__main__":
    main()