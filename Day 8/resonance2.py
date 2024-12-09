def main():
    with open('.\\Day 8\\input.txt') as input:
        lines = input.readlines()

    nodes = {}
    antinodes = set()

    for y, line in enumerate (lines):
        line = line.strip("\n")
        for x, c in enumerate(line):
            if c != "." :
                nodes.setdefault(c, []).append([y, x])

    # Get the locations of each node and create antinodes at other locations
    # depending on the distance between each pair of nodes
    grid_length = len(lines)
    for node in nodes:
        node_length = len(nodes[node])
        for i, location in enumerate(nodes[node]):
            while i < node_length - 1:
                i += 1

                node1 = [location[0], location[1]]
                node2 = [nodes[node][i][0], nodes[node][i][1]]
                y_diff = abs(node1[0] - node2[0])
                x_diff = abs(node1[1] - node2[1])

                antinode1_diff_y = "<" if node1[0] < node2[0] else ">"
                antinode1_diff_x = "<" if node1[1] < node2[1] else ">"
                antinode1 = [node1[0], node1[1]]

                antinode2_diff_y = "<" if node2[0] < node1[0] else ">"
                antinode2_diff_x = "<" if node2[1] < node1[1] else ">"
                antinode2 = [node2[0], node2[1]]

                antinode_diffs = [[antinode1_diff_y, antinode1_diff_x],
                                  [antinode2_diff_y, antinode2_diff_x]]
                for antinode, diff in zip([antinode1, antinode2], antinode_diffs):
                    while (antinode[0] >= 0 and antinode[0] < grid_length) and (
                    antinode[1] >= 0 and antinode[1] < grid_length):
                        antinodes.add(tuple(antinode))
                    
                        antinode[0] = antinode[0] - y_diff if diff[0] == "<" else antinode[0] + y_diff
                        antinode[1] = antinode[1] - x_diff if diff[1] == "<" else antinode[1] + x_diff
                
    print(f"Number of antinodes: {len(antinodes)}")
    print()

if __name__ == "__main__":
    main()