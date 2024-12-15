import time

def main():
    start_time = time.time()
    numbers = []
    with open(".\\Day 11\\input.txt") as input:
        for line in input:
            line = line.split()
            for i in line:
                numbers.append(int(i))

    numbers = blink(numbers, 75)
    print(f"Number of stones: {numbers}")
    
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")


def blink(numbers: list[int], times:int) -> list[int]:
    memo = {}

    def change_stone(number, i):
        if i == 0:
            return 1

        if (number, i) in memo:
            return memo[(number, i)]
        else:
            if number == 0:
                result = [1]
            else:
                num_digits = 0
                temp = number
                while temp > 0:
                    num_digits += 1
                    temp //= 10
                
                if num_digits % 2 == 0:
                    mid = num_digits // 2
                    left = number // (10 ** mid)
                    right = number % (10 ** mid)
                    result = [left, right]
                else:
                    result = [number * 2024]
            count = 0
            for n in result:
                count += change_stone(n, i-1)

        memo[(number, i)] = count
        return count

    count = 0
    for number in numbers:
        count += change_stone(number, times)
    return count
      

if __name__ == "__main__":
    main()