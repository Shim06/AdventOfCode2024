import time

def main():
    start_time = time.time()
    map_x_size = 101
    map_y_size = 103
    vertical_slice = map_x_size // 2
    horizontal_slice = map_y_size // 2
    quadrant1 = 0
    quadrant2 = 0
    quadrant3 = 0
    quadrant4 = 0
    robots_pos = []
    robots_vel = []
    with open(".\\Day 14\\input.txt") as input:
        for robot in input:
            robot =robot.split(" ")
            pos = robot[0].removeprefix("p=").split(",")
            vel = robot[1].removeprefix("v=").removesuffix("\n").split(",")
            for i in range(len(pos)):
                pos[i] = int(pos[i])
            for i in range(len(vel)):
                vel[i] = int(vel[i])
            robots_pos.append(pos)
            robots_vel.append(vel)

    for i in range(len(robots_pos)):
        move(robots_pos[i], robots_vel[i], map_x_size, map_y_size, 100)

    # Count number of robots in each quadrant
    for x, y in robots_pos:
        # Quadrant 1
        if vertical_slice < x < map_x_size and 0 <= y < horizontal_slice:
            quadrant1 += 1

        # Quadrant 2
        if 0 <= x < vertical_slice and 0 <= y < horizontal_slice:
            quadrant2 += 1

        # Quadrant 3
        if 0 <= x < vertical_slice and horizontal_slice < y < map_y_size:
            quadrant3 += 1

        # Quadrant 4
        if vertical_slice < x < map_x_size and horizontal_slice < y < map_y_size:
            quadrant4 += 1

    print(f"Safety Factor: {quadrant1 * quadrant2 * quadrant3 * quadrant4}")

    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")


def move(pos, vel, width, height, times:int):
    pos[0] += (vel[0] * times)
    pos[0] %= width

    pos[1] += (vel[1] * times)
    pos[1] %= height


if __name__ == "__main__":
    main()