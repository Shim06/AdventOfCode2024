# Time Complexity - O(n)
# Space Complexity - O(n)

totalCount = {}
leftList = []
similarityScore = 0

with open('.\\Day 1\\input.txt') as input:
    for line in input:
        slice = line.split()
        leftList.append(slice[0])
        totalCount[int(slice[1])] = 1 + totalCount.get(int(slice[1]), 0)

for i in leftList:
    similarityScore += (int(i) * totalCount.get(int(i), 0))

print(similarityScore)