"""
Build an Adjacency List to Matrix Converter
In this lab, you will build a function that converts an adjacency 
list representation of a graph into an adjacency matrix. 
An adjacency list is a dictionary where each key represents a node, 
and the corresponding value is a list of nodes that the 
key node is connected to. An adjacency matrix is a 
2D array where the entry at position [i][j] is 1 
if there's an edge from node i to node j, and 0 otherwise.
"""





def adjacency_list_to_matrix(adj_list: dict):

    # Number of nodes (assumes nodes are labeled 0..n-1)
    n = len(adj_list)

    # Create an n x n matrix initialized with zeros
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the matrix: mark 1 where an edge exists
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            adj_matrix[node][neighbor] = 1

    # Print each row of the adjacency matrix
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)

    return adj_matrix


# ---------------------------------------------------------
# MAIN FUNCTION WITH TEST CALLS
# ---------------------------------------------------------

def main():
    # directed graph
    adj_list_1 = {
        0: [1, 2],
        1: [2],
        2: [0]
    }

    print("\n=== Test 1 ===")
    adjacency_list_to_matrix(adj_list_1)

    # Graph with a node that has no outgoing edges
    adj_list_2 = {
        0: [1],
        1: [],
        2: [0, 1]
    }

    print("\n=== Test 2 ===")
    adjacency_list_to_matrix(adj_list_2)

    # Fully connected graph
    adj_list_3 = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }

    print("\n=== Test 3 ===")
    adjacency_list_to_matrix(adj_list_3)



if __name__ == "__main__":
    main()

