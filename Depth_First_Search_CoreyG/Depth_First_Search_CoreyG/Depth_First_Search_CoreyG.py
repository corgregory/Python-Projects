"""Implement the Depth-First Search Algorithm
In this lab, you will implement a graph traversal algorithm called depth-first search.

Whereas the breadth-first search searches incremental edge lengths away from the source node, depth-first search first goes down a path of edges as far as it can.

Once it reaches one end of a path, the search will backtrack to the last node with an un-visited edge path and continue searching.

Unlike breadth-first search, every time a node is visited, it doesn't visit all of its neighbors. Instead, it first visits one of its neighbors and continues down that path until there are no more nodes to be visited on that path.

To implement this algorithm, you'll want to use a stack (an array where the last element added is the first to be removed, following the Last-In-First-Out principle). A stack is helpful in depth-first search algorithms because, as you add neighbors to the stack, you want to visit the most recently added neighbors first and remove them from the stack.

A simple output of this algorithm is a list of nodes which are reachable from a given node. Therefore, you'll also want to keep track of the nodes you visit.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

"""




def dfs(adj_matrix, start_node):
    

    n = len(adj_matrix)            # Total number of nodes in the graph
    visited = [False] * n          # Track which nodes we've already visited
    result = []                    # Store nodes in the order they are visited
    stack = []                     # DFS uses a LIFO stack

    # Start the DFS by pushing the starting node onto the stack
    stack.append(start_node)

    # Continue until there are no more nodes left to explore
    while stack:
        node = stack.pop()         # Pop the most recently added node (LIFO)

        # Only process the node if it hasn't been visited yet
        if not visited[node]:
            visited[node] = True   # Mark the node as visited
            result.append(node)    # Record the visit

            # Look at all possible neighbors of this node.
            # We iterate from high → low so that lower-numbered neighbors
            # get visited first (because stack reverses the order).
            for neighbor in range(n - 1, -1, -1):
                # If there is an edge AND the neighbor hasn't been visited,
                # push it onto the stack to explore later.
                if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result



def main():
 
    adj_matrix = [
        [0,1,0,1,0],
        [1,0,1,0,1],
        [0,1,0,0,0],
        [1,0,0,0,1],
        [0,1,0,1,0]
    ]

    print("DFS starting at node 0:", dfs(adj_matrix, 0))
    print("DFS starting at node 1:", dfs(adj_matrix, 1))
    print("DFS starting at node 2:", dfs(adj_matrix, 2))
    print("DFS starting at node 3:", dfs(adj_matrix, 3))
    print("DFS starting at node 4:", dfs(adj_matrix, 4))


if __name__ == "__main__":
    main()
