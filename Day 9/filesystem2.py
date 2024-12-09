# Time Complexity - O(n^2)
# Space Complexity - O(n)

def main():
    filesystem = []
    total = 0

    with open('.\\Day 9\\input.txt') as input:
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
    i = filesystem_length - 1
    while i >= 0:
        l = 0
        file_length = 0
        swapped = False
        if filesystem[i] == ".":
            i -= 1
        elif filesystem[i] != ".":
            file_length += 1
            i -= 1
            while filesystem[i] == filesystem[i + 1]:
                i -= 1
                file_length += 1

            while l < i:
                space_length = 0
                if filesystem[l] != ".":
                    l += 1
                elif filesystem[l] == ".":
                    space_length += 1
                    l += 1
                    if space_length == file_length:
                            while space_length > 0:
                                temp = filesystem[l - space_length]
                                filesystem[l - space_length] = filesystem[i + space_length]
                                filesystem[i + space_length] = temp
                                space_length -= 1
                            swapped = True
                            break
                    
                    while filesystem[l] == filesystem[l - 1]:
                        l += 1
                        space_length += 1

                        if space_length == file_length:
                            while space_length > 0:
                                temp = filesystem[l - space_length]
                                filesystem[l - space_length] = filesystem[i + space_length]
                                filesystem[i + space_length] = temp
                                space_length -= 1
                            swapped = True
                            break

                if swapped:
                    break
        
    # Calculate hash
    for i in range(filesystem_length):
        if filesystem[i] != ".":
            total += i * filesystem[i]
    print(total)


if __name__ == "__main__":
    main()