import time

def main():
    total = 0
    start_time = time.time()
    with open(".\\Day 22\\input.txt") as input:
        for line in input:
            line = line.removesuffix("\n")
            total += evolve(int(line), 2000)

    print(total)

    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")

def evolve(number:int, times:int):
    def evolve_once(number):
        temp = number * 64
        number ^= temp
        number %= 16777216

        temp2 = number // 32
        number ^= temp2
        number %= 16777216

        temp3 = number * 2048
        number ^= temp3
        number %= 16777216
        return number
    for i in range(times):
        number = evolve_once(number)
    return number


if __name__ == "__main__":
    main()