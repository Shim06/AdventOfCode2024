# Time Complexity - O(n log n)
# Space Complexity - O(n)

leftList = []
rightList = []
totalDistance = 0

with open('.\\Day 1\\input.txt') as input:
    for line in input:
        slice = line.split()
        leftList.append(int(slice[0]))
        rightList.append(int(slice[1]))

leftList.sort()
rightList.sort()
size = len(leftList)
for i in range(size):
    distance = abs(leftList[i] - rightList[i])
    totalDistance += distance

print(totalDistance)