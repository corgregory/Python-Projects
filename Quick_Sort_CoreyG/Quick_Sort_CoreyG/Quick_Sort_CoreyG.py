"""
Implement the Quicksort Algorithm
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named quick_sort to implement the quicksort algorithm.

The quick_sort function should take a list of integers as input and return a new list of these integers in sorted order from least to greatest.

To implement the algorithm, you should:

Choose a pivot value from the elements of the input list (use the first or the last element of the list).
Partition the input list into three sublists: one with elements less than the pivot, one with elements equal to the pivot, and one with elements greater than the pivot.
Recursively call quick_sort to sort the sublists and concatenate the sorted sublists to produce the final sorted list.
"""



def quick_sort(integer_list) -> list:
    # Base case: if the list has 0 or 1 elements, it is already sorted
    if len(integer_list) <= 1:
        return integer_list

    # Choose the pivot value (using the first element of the list)
    pivot_value = integer_list[0]

    # Create three lists to hold values less than, equal to, and greater than the pivot
    less_than_pvalue = []
    equal_to_pvalue = []
    greater_than_pvalue = []

    # Partition the list into the three categories
    for value in integer_list:
        if value < pivot_value:
            less_than_pvalue.append(value)
        elif value > pivot_value:
            greater_than_pvalue.append(value)
        else:
            # Values equal to the pivot go here (including the pivot itself)
            equal_to_pvalue.append(value)
    
    # Recursively sort the 'less than' and 'greater than' lists,
    # then concatenate them with the 'equal to' list in the middle
    return quick_sort(less_than_pvalue) + equal_to_pvalue + quick_sort(greater_than_pvalue)


def main():
    # Test list
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print("Original list:")
    print(numbers)

    # Call quick_sort and store the result
    sorted_numbers = quick_sort(numbers)

    print("Sorted list:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
