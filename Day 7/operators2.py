# Time Complexity - O(3^n-1 * n)
# Space Complexity - O(3^n-1 * n)

def main():
    total = 0
    with open('.\\Day 7\\input.txt') as input:
        for line in input:
            line = line.split(":")
            equation_total = int(line[0])
            numbers = line[1][1:].split(" ")
            numbers[-1] = numbers[-1].replace("\n", "")
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])

            total += check(equation_total, numbers)

    print(f"Total: {total}")


def check(total:int, numbers:list[int]) -> int:
    num_operators = len(numbers) - 1
    operators_list = generate_permutations(num_operators)
    for operators in operators_list:
        equation_total =  numbers[0]
        for i, op in enumerate(operators):
            if i == num_operators:
                break  
            
            if op == "+":
                equation_total += numbers[i + 1]
            elif op == "*":
                equation_total *= numbers[i + 1]
            else:
                equation_total = int(str(equation_total) + str(numbers[i + 1]))

            if equation_total == total:
                return equation_total
    return 0


def generate_permutations(length, current_permutation=None, all_permutations=None):
    if current_permutation == None:
        current_permutation = []
    if all_permutations == None:
        all_permutations = []

    operators = ['+', '*', "||"]
    if length == 0:
        all_permutations.append(current_permutation[:])
        return

    for op in operators:
        current_permutation.append(op)
        generate_permutations(length - 1, current_permutation, all_permutations)
        current_permutation.pop()
    return all_permutations

if __name__ == "__main__":
    main()