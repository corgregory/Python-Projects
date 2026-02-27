def binary_search(search_list, value):
    # This list will record every midpoint value we inspect during the search.
    path_to_target = []

    # Set the initial search boundaries to the full list.
    low = 0
    high = len(search_list) - 1

    # Continue searching as long as the interval is valid.
    while low <= high:
        # Find the midpoint index using floor division.
        mid = (low + high) // 2

        # Get the value at the midpoint.
        value_at_middle = search_list[mid]

        # Record the value we checked for the path output.
        path_to_target.append(value_at_middle)

        # If we found the target, return the path and a success message.
        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"

        # If the target is larger, search the right half.
        elif value > value_at_middle:
            low = mid + 1

        # Otherwise, search the left half.
        else:
            high = mid - 1

    # If we exit the loop, the value was not found.
    # Return an empty path and a clear message.
    return [], "Value not found"


# Test calls
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))

