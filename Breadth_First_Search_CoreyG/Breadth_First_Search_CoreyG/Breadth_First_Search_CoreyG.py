"""
    Generate all valid combinations of parentheses using BFS.

    Each state in the BFS queue is a tuple:
        (current_string, opens_used, closes_used)

    BFS explores all partial strings level-by-level, ensuring
    we build shorter strings first and expand them systematically.
    """



def gen_parentheses(pairs):
    
    # Input validation
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'

    # Initial BFS state
    # Start with an empty string and zero parentheses used
    queue = [('', 0, 0)]
    result = []

    # Main BFS loop
    # Continue until the queue is empty
    while queue:
        # Remove the next item from the queue (FIFO)
        current, opens_used, closes_used = queue.pop(0)

        # If the string is complete (2 * pairs characters), store it
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            # Option 1: Add '(' if we still have open parentheses left to use
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))

            # Option 2: Add ')' only if it won't break validity
            # (we can only close if we have more opens than closes)
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))

    return result



def main():
    print("Testing gen_parentheses...\n")

    print("pairs = 1:")
    print(gen_parentheses(1))
    print()

    print("pairs = 2:")
    print(gen_parentheses(2))
    print()

    print("pairs = 3:")
    print(gen_parentheses(3))
    print()

    print("pairs = 4:")
    print(gen_parentheses(4))
    print()

if __name__ == "__main__":
    main()

