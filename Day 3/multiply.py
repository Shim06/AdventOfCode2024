# Time Complexity - O(n)
# Space Complexity - O(n)

result = 0

with open('.\\Day 3\\input.txt') as input:
    for line in input:
        i = 0
        while i < len(line):
            letter = line[i]
            if letter == "m":
                if line[i:i+4] == "mul(":
                    l = i + 4
                    r = l + 1
                    left = i + 4
                    number = 0
                    number2 = 0
                    while line[l:r].isnumeric():
                        r += 1
                    if line[r-1] == ",":
                        number = int(line[l:r-1])
                        l = r
                        r = l + 1
                        while line[l:r].isnumeric():
                            r += 1
                            if line[r-1] == ")":
                                number2 = int(line[l:r-1])
                                product = number * number2
                                result += product
                            else:
                                i = r - 1
                    else:
                        i = r - 1

                    

            i += 1

print(result)