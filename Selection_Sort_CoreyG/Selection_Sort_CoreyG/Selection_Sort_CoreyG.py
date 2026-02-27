"""
Implement the Selection Sort Algorithm
Selection sort is another popular sorting algorithm taught in most computer science courses.

This algorithm works by repeatedly finding the smallest element from the unsorted portion of the list and swapping it with the first unsorted element. It begins by selecting the minimum value in the entire list and swapping it with the first element. Then it moves to the second position, finds the smallest value in the remaining unsorted elements, and swaps it with the second element. This process continues, moving through the list one element at a time, until the entire list is sorted.

Selection sort results in a quadratic time complexity in the best, average, and worst case scenarios. The space complexity will be constant O(1) because the sorting is done in place and a constant amount of memory is being used regardless of the size of the list.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named selection_sort.
Your selection_sort function should have one parameter that represents the list of items.
Your selection_sort function should take a list and sort the items in place from smallest to largest.
Your selection_sort function should modify the input list in-place, and return it once it's sorted.
Your selection_sort function should follow the selection sort algorithm, swapping the smallest element from the unsorted portion of the list with the first unsorted element.
Your selection_sort function should not perform unnecessary swaps when the smallest element is already in the correct position.
Your selection_sort function should not use either the built-in sort() method or sorted() function.

"""




def selection_sort(items) -> list:
    # Loop through each index in the list.
    # Everything before 'index' is considered sorted.
    for index in range(len(items)):
        
        # Assume the current index holds the smallest value.
        small_value = index

        # Scan the rest of the list to find the true smallest value.
        for j_index in range(index + 1, len(items)):
            # If a smaller value is found, update small_value.
            if items[j_index] < items[small_value]:
                small_value = j_index

        # Only swap if the smallest value is not already in the correct position.
        if small_value != index:
            items[index], items[small_value] = items[small_value], items[index]

    # Return the now-sorted list.
    return items


def main():
    # Test list
    numbers = [29, 10, 14, 37, 13]

    print("Original list:")
    print(numbers)

    # Perform selection sort
    sorted_numbers = selection_sort(numbers)

    print("Sorted list:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
