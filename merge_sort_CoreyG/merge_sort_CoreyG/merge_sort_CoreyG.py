def merge_sort(array):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(array) <= 1:
        return
    
    # Find the midpoint to split the array into two halves
    middle_point = len(array) // 2
    
    # Slice the array into left and right halves
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort each half
    merge_sort(left_part)
    merge_sort(right_part)

    # Index trackers for left_part, right_part, and the main array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the two sorted halves back into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Compare elements from each half and place the smaller one into the array
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        
        sorted_index += 1

    # Copy any remaining elements from the left half
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements from the right half
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


def main():
    # Initial unsorted list
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print('Unsorted array:')
    print(numbers)

    # Perform merge sort
    merge_sort(numbers)

    print('Sorted array:')
    print(numbers)

if __name__ == '__main__':
    main()

