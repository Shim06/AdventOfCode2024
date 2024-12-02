# Time Complexity - O(m * n^2) 
# where m is the number of reports and n is the number of levels
# Space Complexity - O(n)

from enum import Enum

class reportBehaviour(Enum):
    DECREASING = 0
    INCREASING = 1

safeReports = 0

def isSafe(levels, behaviour):
    for i in range(len(levels) - 1):
        # a report only counts as safe if both of the following are true:
        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.
        firstValue = i
        secondValue = i + 1
        if behaviour == reportBehaviour.DECREASING.value:
                if not levels[firstValue] > levels[secondValue]:
                    return False
        else:
            if not levels[firstValue] < levels[secondValue]:
                return False
        
        if abs(levels[firstValue] - levels[secondValue]) < 1:
            return False
        if abs(levels[firstValue] - levels[secondValue]) > 3:
            return False
    return True


with open('.\\Day 2\\input.txt') as input:
    for report in input:
        levels = report.strip("\n").split(" ")

        for i in range(len(levels)):
            levels[i] = int(levels[i])

        if levels[0] > levels[-1]:
            behaviour = reportBehaviour.DECREASING.value
        elif levels[0] < levels[-1]:
            behaviour = reportBehaviour.INCREASING.value
        else:
            continue
                
        if isSafe(levels, behaviour):
            safeReports += 1
        else:
            for i in range(len(levels)):
                newReport = levels[:i] + levels[i+1:]
                if isSafe(newReport, behaviour):
                    safeReports += 1
                    break

print(safeReports)
