import time

def main():
    start_time = time.time()
    wires = {}
    operations = {}
    adj_list = {}
    with open(".\\Day 24\\input.txt") as input:
        for line in input:
            if ":" in line:
                wire, value = line.split(":")
                wires[wire.strip()] = int(value.strip())
                adj_list[wire.strip()] = []
                operations[wire.strip()] = []
            elif "->" in line:
                line = line.split(" ")
                wire1 = line[0]
                op = line[1]
                wire2 = line[2]
                out = line[4].removesuffix("\n")
                operations[out] = []
                operations[out].append([wire1, op, wire2])

                if out not in wires:
                    wires[out] = 0
                if out not in adj_list:
                    adj_list[out] = []
                    
                adj_list[out].append(wire1)
                adj_list[out].append(wire2)

    operation_list = topologicalSort(adj_list, wires)
    for ops in operation_list:
        for op in operations[ops]:
            wire1, operation, wire2 = op
            wires[ops] = logicalOperation(wires[wire1], wires[wire2], operation)
        
    number = ""
    for key, value in sorted(wires.items()):
        if key.startswith("z"):
            number += str(value)
    number = number[::-1]
    print(number)
    print(int(number, 2))
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")


def topologicalSort(adj_list:list, wires:list):
    visit = set()
    cycle = set()
    result = []
    def dfs(wire):
        if wire in cycle:
            return
        if wire in visit:
            return
        
        cycle.add(wire)
        for neighbor in adj_list[wire]:
            dfs(neighbor)

        cycle.remove(wire)
        visit.add(wire)
        result.append(wire)

    for wire in wires:
        if wire in adj_list:
            dfs(wire)
    return result


def logicalOperation(a:bool, b:bool, operation:str) -> bool:
    if operation == "AND":
        return AND(a, b) 
    elif operation == "OR":
        return OR(a, b)
    elif operation == "XOR":
        return XOR(a, b)
    return 0


def AND(a:bool, b:bool) -> bool:
    if a and b:
        return 1
    return 0


def OR(a:bool, b:bool) -> bool:
    if a or b:
        return 1
    return 0


def XOR(a:bool, b:bool) -> bool:
    if a != b:
        return 1
    return 0


if __name__ == "__main__":
    main()