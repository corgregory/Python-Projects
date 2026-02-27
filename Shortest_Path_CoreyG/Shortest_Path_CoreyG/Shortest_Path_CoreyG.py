

INF = float('inf')

# Adjacency matrix for the weighted graph
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix, start_node, target_node=None):
    """
    Compute the shortest paths from start_node to all other nodes
    using Dijkstra's algorithm.

    Returns:
        distances: list of shortest distances from start_node
        paths: list of paths (each path is a list of node numbers)
    """

    n = len(matrix)

    # Distance to each node (initialized to INF except start)
    distances = [INF] * n
    distances[start_node] = 0

    # Paths list: each node starts with a path containing only itself
    paths = [[node_no] for node_no in range(n)]

    # Track which nodes have been permanently visited
    visited = [False] * n

    # Main Dijkstra loop (runs at most n times)
    for _ in range(n):

        #Select the unvisited node with the smallest distance
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # If no reachable node remains, stop early
        if current == -1:
            break

        visited[current] = True

        # Relax edges from the current node
        for node_no in range(n):
            distance = matrix[current][node_no]

            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance

                # Found a shorter path → update distance and path
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    #Determine which nodes to print results for
    targets = [target_node] if target_node is not None else range(n)

    for node_no in targets:
        # Skip printing the start node or unreachable nodes
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Convert path list to "A -> B -> C" format
        string_path = (str(n) for n in paths[node_no])
        path = " -> ".join(string_path)

        print(f"\n{start_node}-{node_no} distance: {distances[node_no]}")
        print(f"Path: {path}")

    # Step 26: Return distances and paths for external use
    return distances, paths


# main function with test calls
def main():
    print("\n=== Test 1: From node 0 to ALL nodes ===")
    shortest_path(adj_matrix, 0)

    print("\n=== Test 2: From node 0 to node 5 ===")
    shortest_path(adj_matrix, 0, 5)

    print("\n=== Test 3: From node 2 to ALL nodes ===")
    shortest_path(adj_matrix, 2)

    print("\n=== Test 4: From node 3 to node 4 ===")
    shortest_path(adj_matrix, 3, 4)


if __name__ == "__main__":
    main()

