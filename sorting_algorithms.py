## Bubble Sort compares two elements in a given input array and checks if the first element is larger than the second element
# If it is larger we swap the elements, this way the sort iterates through moving the largest element to the end of the array
# We do this calling a swap function for every element in the array and every index that each element can be compared to
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


# Comparing 3 elements in the array and swapping them if the left element is larger than the right element, while keeping track
# of the total number of iterations required for completion
def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


# Accounting for the elements that have already been placed (largest elements at the end), this reduces the total number of
# checks required, although runtime is still O(N^2)
def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
# Time complexity O(N^2), Space complexity O(1)
# Output here will be:
"""
PRE SORT: [9, 8, 7, 6, 5, 4, 3, 2, 1]
PRE-OPTIMIZED ITERATION COUNT: 72
POST-OPTIMIZED ITERATION COUNT: 36
POST SORT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


## Merge Sort splits a given input array recursively into multiple individual elements then merges depending on if the left
# element is smaller than the right element, when all elements on one side are depleted we add the remaining elements from
# the other side and this occurs recursively through the split and merged sublists until the original list has been sorted
def merge_sort(items):
    # Base case, if input list length is 1 or less, simply return the input list
    if len(items) <= 1:
        return items
    # Labelling a middle index to use recursively to split our input list
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    # Calling the function recursively until we reach the base case to then run the merge function on the individual elements
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


# Merge function takes a left and right input to be merged and initiates an empty result list to store the sorted values
def merge(left, right):
    result = []
    # Using a loop to check that elements exist in both input lists, then comparing the first left element to the first right
    # element and appending this to result, we then pop this element from its list
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # When one or both input lists have been depleted, we add the remaining elements from the other list to the end of result
    if left:
        result += left
    if right:
        result += right
    # Returns the sorted list
    return result


unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
ordered_list1 = merge_sort(unordered_list1)
print(ordered_list1)
unordered_list2 = [
    787,
    677,
    391,
    318,
    543,
    717,
    180,
    113,
    795,
    19,
    202,
    534,
    201,
    370,
    276,
    975,
    403,
    624,
    770,
    595,
    571,
    268,
    373,
]
ordered_list2 = merge_sort(unordered_list2)
print(ordered_list2)
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
ordered_list3 = merge_sort(unordered_list3)
print(ordered_list3)
# Time complexity O(N*log(N)), Space complexity O(N)
# Output here will be:
"""
[125, 264, 356, 455, 569, 746, 895, 949]
[19, 113, 180, 201, 202, 268, 276, 318, 370, 373, 391, 403, 534, 543, 571, 595, 624, 677, 717, 770, 787, 795, 975]
[147, 151, 380, 387, 439, 542, 585, 743, 820, 860, 865, 924]
"""


## Quicksort splits a given list by a random pivot element and uses recursion to compare elements to the pivot and rearrange
# them in place, this helps to save on space
from random import randrange, shuffle


def quicksort(list, start, end):
    # Base case, if our sublist contains 1 or 0 elements we simply return as we have reached our base case
    if start >= end:
        return
    print("Running quicksort on {0}".format(list[start : end + 1]))
    # select random element to be the pivot and swap this element with the last element in the sub-list
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to the left of the pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(list[i], list[less_than_pointer]))
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    print("{0} successfully partitioned".format(list[start : end + 1]))
    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)


list = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) - 1))
print("POST SORT: ", list)
# Time complexity O(N^2), Space complexity O(log N)
# Output here will look like:
"""
PRE SORT:  [5, 7, 6, 1, 4, 8, 3, 2]
Running quicksort on [5, 7, 6, 1, 4, 8, 3, 2]
Selected pivot 4
Swapping 1 with 4
Swapping 2 with 4
Swapping 3 with 4
[1, 2, 3, 4, 7, 8, 6, 5] successfully partitioned
Running quicksort on [1, 2, 3]
Selected pivot 2
Swapping 1 with 2
[1, 2, 3] successfully partitioned
Running quicksort on [7, 8, 6, 5]
Selected pivot 5
[5, 8, 6, 7] successfully partitioned
Running quicksort on [8, 6, 7]
Selected pivot 6
[6, 7, 8] successfully partitioned
Running quicksort on [7, 8]
Selected pivot 7
[7, 8] successfully partitioned
None
POST SORT:  [1, 2, 3, 4, 5, 6, 7, 8]
"""
# Output will change due to the random nature of selecting the pivot


# Radix sort is non-comparison sort. It works by taking numbers in an input list, passes through those digits from least to most significant, looks at the values of those digits, buckets the input list according to those digits, renders the results from that bucketing, and repeats this process until the list is sorted.
def radix_sort(to_be_sorted):
    # storing max value to know how many iterations are required
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    # create a copy of the original list to store our sorted numbers
    being_sorted = to_be_sorted[:]
    # loop through each exponent to determine position from the end of the largest number (least to most significant digit)
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        # create a list of empty lists to store each numeral (0-9)
        digits = [[] for i in range(10)]
        # try and except block to avoid IndexErrors when numbers have fewer digits than the largest number
        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            # store reference digit as integer to then bucket the corresponding number
            digit = int(digit)
            digits[digit].append(number)
        # included print statement to show each step in example
        print(being_sorted)
        # reassign to empty list with each iteration to extend values into it from the sorted lists
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)
    # return the final sorted list
    return being_sorted


unsorted_list = [
    830,
    921,
    163,
    373,
    961,
    559,
    89,
    199,
    535,
    959,
    40,
    641,
    355,
    689,
    621,
    183,
    182,
    524,
    1,
]
print(radix_sort(unsorted_list))
# time complexity O(n) (O(wn) for n = list length, w = average number of digits/word size)
# Output here will be:
"""
[830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
[830, 40, 921, 961, 641, 621, 1, 182, 163, 373, 183, 524, 535, 355, 559, 89, 199, 959, 689]
[1, 921, 621, 524, 830, 535, 40, 641, 355, 559, 959, 961, 163, 373, 182, 183, 89, 689, 199]
[1, 40, 89, 163, 182, 183, 199, 355, 373, 524, 535, 559, 621, 641, 689, 830, 921, 959, 961]
"""
