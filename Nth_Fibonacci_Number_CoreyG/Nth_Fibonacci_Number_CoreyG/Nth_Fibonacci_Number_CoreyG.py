"""
Build an Nth Fibonacci Number Calculator
Objective: Fulfill the user stories below and get all the tests to pass 
to complete the lab.

User Stories:

You should create a function named fibonacci.
You should define a list named sequence within the fibonacci function, 
and it should be initialized with the values [0, 1].
The fibonacci function should accept one parameter, a positive integer n.
Calling fibonacci(n) should use a dynamic programming approach 
to compute and return the n-th number from the Fibonacci sequence
, where each number is the sum of the two preceding numbers.
Each computed number at the position n in the Fibonacci sequence 
should be stored in the sequence list at index n - 1.

"""



def fibonacci(n):
    """
    Compute the n-th Fibonacci number using a dynamic programming approach.

    The Fibonacci sequence starts with:
        sequence[0] = 0
        sequence[1] = 1

    Each new value is the sum of the previous two values.
    This function builds the sequence iteratively and returns sequence[n].
    """

    # Required starting list for dynamic programming
    sequence = [0, 1]

    # Handle the first two Fibonacci numbers directly
    if n == 0:
        return sequence[0]   # 0th Fibonacci number
    if n == 1:
        return sequence[1]   # 1st Fibonacci number

    # Build the sequence up to index n
    # We start at 2 because 0 and 1 are already defined
    for i in range(2, n + 1):        #(2, n + 1) to include n in the sequence
        next_value = sequence[i - 1] + sequence[i - 2]  # DP recurrence
        sequence.append(next_value)                      # store result at index i

    # Return the n-th Fibonacci number
    return sequence[n]


def main():
    print("fibonacci(0):", fibonacci(0))     # Expected 0
    print("fibonacci(1):", fibonacci(1))     # Expected 1
    print("fibonacci(2):", fibonacci(2))     # Expected 1
    print("fibonacci(3):", fibonacci(3))     # Expected 2
    print("fibonacci(5):", fibonacci(5))     # Expected 5
    print("fibonacci(10):", fibonacci(10))   # Expected 55
    print("fibonacci(15):", fibonacci(15))   # Expected 610

if __name__ == "__main__":
    main()

