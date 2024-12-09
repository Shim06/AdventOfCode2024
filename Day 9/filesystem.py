# Time Complexity - O(n)
# Space Complexity - O(n)

def main():
    filesystem = []
    total = 0

    with open('.\\Day 9\\input2.txt') as input:
        for line in input:
            id = 0
            for i, c in enumerate(line):
                if i % 2 == 0:
                    for i in range(int(c)):
                        filesystem.append(id)
                    id += 1
                else:
                    for i in range(int(c)):
                        filesystem.append(".")

    filesystem_length = len(filesystem)
    l = 0
    r = filesystem_length - 1
    while l < r:
        if filesystem[l] == "." and filesystem[r] != ".":
            temp = filesystem[l]
            filesystem[l] = filesystem[r]
            filesystem[r] = temp
        elif filesystem[l] != ".":
            l += 1
        elif filesystem[r] == ".":
            r -= 1

    for i in range(filesystem_length):
        if filesystem[i] != ".":
            total += i * filesystem[i]

    print(total)


if __name__ == "__main__":
    main()