total = 0

with open('.\\Day 5\\input.txt') as input:
    lines = input.readlines()

visited = set()
cycle = set()
def is_valid(page: int):
    if page in cycle:
        return False
    if page in visited:
        return True
    
    cycle.add(page)
    if page not in currentPrereqs:
        visited.add(page)
        cycle.remove(page)
        output.append(page)
        return True
    
    for prereq in currentPrereqs[page]:
        if prereq not in visited:
            cycle.remove(page)
            visited.add(page)
            output.append(page)
            return False
        if is_valid(prereq) == False:
            return False
    cycle.remove(page)
    visited.add(page)
    output.append(page)
    return True

def topologicalSort(edges: list):
    topSort = []
    visit = set()
    for prereqs in list(currentPrereqs.keys()):
        dfs(prereqs, currentPrereqs, visit, topSort)
    return topSort

def dfs(src, adj, visit, topSort):
    if src in visit:
        return True
    visit.add(src)

    if src not in adj:
        adj[src] = []

    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)

# Add all prereqs to a hashmap
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
    output = []
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

    if not valid:
        total += topologicalSort(pages)[int((len(pages) + 1) / 2) - 1]


print(total)