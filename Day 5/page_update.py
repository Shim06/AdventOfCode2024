total = 0

with open('.\\Day 5\\input.txt') as input:
    lines = input.readlines()

visited = set()
cycle = set()
def is_valid(page):
    if page in cycle:
        return False
    if page in visited:
        return True
    
    cycle.add(page)
    if page not in currentPrereqs:
        visited.add(page)
        cycle.remove(page)
        return True
    
    for prereq in currentPrereqs[page]:
        if prereq not in visited:
            return False
        if is_valid(prereq) == False:
            return False
    cycle.remove(page)
    visited.add(page)
    return True

# add all prereqs to a hashmap
prereqs = {}
pageIndex = 0
for i, line in enumerate(lines):
    if line[0] == "\n":
        pageIndex = i + 1
        break

    line = line.split("|")
    page1 = int(line[0])
    page2 = int(line[1])
    prereqs.setdefault(page2, []).append(page1)

inputLength = len(lines)
    
for line in lines[pageIndex:]:
    currentPrereqs = {}
    visited = set()
    cycle = set()
    valid = True
    # Get pages and convert to int
    pages = line.split(",")
    for i in range(len(pages)):
        pages[i] = int(pages[i])

    pagesSet = set(pages)
    for page in pages:
        pagePrereqs = prereqs.get(page, [])
        for pagePrereq in pagePrereqs:
            if pagePrereq in pagesSet:
                currentPrereqs.setdefault(page, []).append(pagePrereq)

    for page in pages:
        if is_valid(page) == False:
            valid = False
            break

    if valid:
        # Add the median page number to the total
        total += pages[int((len(pages) + 1) / 2) - 1]

print(total)