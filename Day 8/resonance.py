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

                antinode1_y = node1[0] - y_diff if node1[0] < node2[0] else node1[0] + y_diff
                antinode1_x = node1[1] - x_diff if node1[1] < node2[1] else node1[1] + x_diff
                antinode1 = [antinode1_y, antinode1_x]

                antinode2_y = node2[0] - y_diff if node2[0] < node1[0] else node2[0] + y_diff
                antinode2_x = node2[1] - x_diff if node2[1] < node1[1] else node2[1] + x_diff
                antinode2 = [antinode2_y, antinode2_x]
                
                for antinode in [antinode1, antinode2]:
                    if (antinode[0] >= 0 and antinode[0] < grid_length) and (antinode[1] >= 0 and antinode[1] < grid_length):
                        antinodes.add(tuple(antinode))

    print(f"Number of antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()