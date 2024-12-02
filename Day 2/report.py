# Time Complexity - O(m * n) 
# where m is the number of reports and n is the number of levels
# Space Complexity - O(n)

from enum import Enum

class reportBehaviour(Enum):
    DECREASING = 0
    INCREASING = 1

safeReports = 0

with open('.\\Day 2\\input.txt') as input:
    for report in input:
        safe = True
        levels = report.strip("\n").split(" ")

        for i in range(len(levels)):
            levels[i] = int(levels[i])

        if levels[0] > levels[-1]:
            behaviour = reportBehaviour.DECREASING.value
        elif levels[0] < levels[-1]:
            behaviour = reportBehaviour.INCREASING.value
        else:
            continue

        for i in range(len(levels) - 1):
            # a report only counts as safe if both of the following are true:
            # The levels are either all increasing or all decreasing.
            # Any two adjacent levels differ by at least one and at most three.
            firstValue = i
            secondValue = i + 1
            if behaviour == reportBehaviour.DECREASING.value:
                if not levels[firstValue] > levels[secondValue]:
                    safe = False
            else:
                if not levels[firstValue] < levels[secondValue]:
                    safe = False
            
            if abs(levels[firstValue] - levels[secondValue]) < 1:
                safe = False
            if abs(levels[firstValue] - levels[secondValue]) > 3:
                safe = False
                
        if safe:
            safeReports += 1

print(safeReports)
