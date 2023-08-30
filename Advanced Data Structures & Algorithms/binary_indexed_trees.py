## Range of Responsibility
# We create functions used to return the corresponding binary index tree value for a given element in an array of integers


arr = [1, 8, 7, 2, 5, 11, 4, 16, 7, 17, 9, 6, 12, 15, 27, 19, 22, 21, 3, 20] 

def range_of_responsibility(number):
    # Initialising a variable to store our range of responsibility to be returned from our function
    range_of_responsibility = 0
    # Convert our index into its binary representation, taking the digit values in reverse order to find the index of our rightmost 1 digit
    binary_rep = bin(number)[2:]
    for digit in range(len(binary_rep))[::-1]:
        if binary_rep[digit] == "1":
            # When we find our rightmost 1 digit, we set our r value for our range of responsibility
            r = len(binary_rep) - digit - 1
            range_of_responsibility = 2**r
            # Break out of the loop when we've found our r value as we only want one value for this
            break
    # Finally, return our range of responsibility
    return range_of_responsibility

print(range_of_responsibility(12))
# Output here will be:
"""
4
"""


def array_value(arr, number):
    # Initialise our array value to 0, using the range_of_responsibility function to determine any values we need to add from our array
    value = 0
    range_of_res = range_of_responsibility(number)
    # Our array is 1-indexed so all of our values are 1 less than we'd expect
    for index in range(number - range_of_res, number):
        value += arr[index]
    # Finally, return the binary index tree value corresponding to our index in our array
    return value

print(array_value(arr, 12))
print(array_value(arr, 15))
# Output here will be:
"""
39
27
"""

element12 = 39
element15 = 27


## Computing Range Sum Using a Binary Indexed Tree
# To calculate a range sum, we first calculate a prefix sum using a loop and some bit manipulation


binary_indexed_tree = [8, 13, 1, 4, 7, 23, -7, -7, 3, 17, 2, 23, 9]

def prefix_sum(i):
    # Initiliase our prefix sum value to be 0, to add relevant binary indexed values from our array
    prefix_sum_value = 0
    while i > 0:
        # i - 1 because in Python arrays are 0-based indexing. Element 7 is at index 6.
        prefix_sum_value += binary_indexed_tree[i - 1]
        # Bitwise and operation used to determine the next index to consider when calculating the prefix sum value
        # This logic will essentially convert the rightmost 1 digit into a 0
        i -= i&-i
    # Finally return the prefix sum value for our index i
    return prefix_sum_value

# As stated above, the range sum from i to j ([i, j]) is computed by calculating the prefix sum up to index j and subtracting the prefix sum up index i - 1
# To calculate the range sum from i = 5 to j = 10 we do prefix_sum(10) - prefix_sum(5 - 1) = prefix_sum(10) - prefix_sum(4)
print(prefix_sum(10))
print(prefix_sum(4))

range_sum = prefix_sum(10) - prefix_sum(4)
print(range_sum)
# Output here will be:
"""
10
4
6
"""


## Updating an Element in a Binary Indexed Tree
# To update an element at index i in an array, we take the difference between the new element and the old element and add this difference to all the elements in which index i is in their range of responsibility within the tree
# This operation is done in O(log n) time


binary_indexed_tree = [12, 22, -5, 24, 3, 19, 1, 42, -15, -16, -5, -10, 4, 10, 9]

def update_element(array, index, old_value, new_value):
    # Updating an array with value changes from indices in an array of integers
    binary_indexed_tree = array
    # Storing the difference in value for our initial index to add to every element within its range of responsibility
    diff = new_value - old_value
    while index <= len(binary_indexed_tree):
        binary_indexed_tree[index - 1] += diff
        index = index + (index & -index)
    return binary_indexed_tree

print(update_element(binary_indexed_tree, 1, 12, 14))
# Output here will be:
"""
[14, 24, -5, 26, 3, 19, 1, 44, -15, -16, -5, -10, 4, 10, 9]
"""
print(update_element(binary_indexed_tree, 4, 7, 3))
# Output here will be:
"""
[14, 24, -5, 22, 3, 19, 1, 40, -15, -16, -5, -10, 4, 10, 9]
"""


## Constructing a Binary Indexed Tree
# To construct a binary indexed tree in linear (O(n)) time, we go through each element and perform exactly one point update:
# that is, for an index i, we only update the immediate next index in which i is in its range of responsibility by adding the value that is at i
# We do this for every element in the binary indexed tree


arr = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]
binary_indexed_tree = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]

def binary_index_tree(array):
    # We loop through each index in our copied array and update the value accordingly
    for i in range(1, len(binary_indexed_tree) + 1):
        # Set our next index based on what falls immediately within our range of responsibility
        nxt = i + (i&-i)
        # If our next index falls outside the size of our array, we move on to the next index
        if nxt - 1 >= len(binary_indexed_tree):
            continue
        # Add our current index value to the element at our next index
        binary_indexed_tree[nxt - 1] += binary_indexed_tree[i - 1]
    # Finally, return the binary index tree for our array
    return binary_indexed_tree 

print(binary_index_tree(binary_indexed_tree))
# Output here will be:
"""
[1, 9, -13, 0, 7, 1, 12, 27, 2, -6, 16, 13]
"""
