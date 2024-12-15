import time

def main():
    start_time = time.time()
    numbers = []
    with open(".\\Day 11\\input.txt") as input:
        for line in input:
            line = line.split()
            for i in line:
                numbers.append(int(i))

    for i in range(15):
        numbers = blink(numbers)
    print(f"Number of stones: {len(numbers)}")

    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")


def blink(numbers: list[int]) -> None:
    new_numbers = []
    for number in numbers:
        if number == 0:
                new_numbers.append(1)
        elif len(str(number)) % 2 == 0:
             mid = len(str(number)) // 2
             left = int(str(number)[:mid])
             right = int(str(number)[mid:])
             new_numbers.append(left)
             new_numbers.append(right)
        else:
             new_numbers.append(number * 2024)
    return new_numbers

if __name__ == "__main__":
    main()