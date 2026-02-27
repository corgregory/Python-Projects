
"""
Implement the N-Queens Algorithm
The problem asks you to place N queens on an N×N 
chessboard so that no two queens attack each other 
(no two share a row, column, or diagonal).

For example, if there is a 4x4 board, one valid arrangement is:

Example Code
[1, 3, 0, 2]
That means that in row 0, 
the queen is placed in column 1; in row 1, 
the queen is placed in column 3; in row 2, 
the queen is placed in column 0; and in row 3,
the queen is placed in column 2.

Visually, this arrangement looks like:

Example Code
. Q . .
. . . Q
Q . . .
. . Q .
Where Q represents a queen and . represents an empty square.

In this lab, you will implement the N-Queens problem solver using the 
depth-first search approach.

Objective: Fulfill the user stories below and 
get all the tests to pass to complete the lab.

User Stories:

You should have a function named dfs_n_queens.
The function should accept exactly one argument: an integer n.
If n is less than 1, the function should return an empty list ([]).
The function should return a list of solutions; 
each solution is itself a list of length n, 
where the element at index i is the column index (0-based) 
of the queen in row i
"""





def dfs_n_queens(n: int):
    """
    Solve the N-Queens problem using DFS + backtracking.

    Returns:
     A list of solutions.
     Each solution is a list of length n where solution[i] = column index
     of the queen placed in row i.
    """

    # If n is invalid, return empty list as required
    if n < 1:
        return []

    solutions = []    # store all valid solutions
    current = []      # current partial placement (columns chosen so far)

    def is_safe(row, col):
        """
        Check if placing a queen at (row, col) is safe
        given the queens already placed in rows 0..row-1.
        """
        for r in range(row):        # check all previous rows
            c = current[r]

            # Same column
            if c == col:
                return False

            # Same diagonal: difference in rows == difference in columns
            if abs(r - row) == abs(c - col):
                return False

        return True

    def dfs(row):
        """
        Try to place a queen in each column of the given row.
        If row == n, we found a complete valid solution.
        """
        if row == n:
            solutions.append(current.copy())
            return

        # Try all columns in this row
        for col in range(n):
            if is_safe(row, col):
                current.append(col)   # place queen
                dfs(row + 1)          # move to next row
                current.pop()         # backtrack

    # Start DFS from row 0
    dfs(0)
    return solutions


def main():
    print("n = 1:", dfs_n_queens(1))
    print("n = 2:", dfs_n_queens(2))   # no solutions
    print("n = 3:", dfs_n_queens(3))   # no solutions
    print("n = 4:", dfs_n_queens(4))   # 2 solutions
    print("n = 5:", dfs_n_queens(5))   # 10 solutions

if __name__ == "__main__":
    main()