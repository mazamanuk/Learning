## Creating a function to apply a binary search on a sorted list, attempting to locate a target value by trimming down
# the input list into smaller input lists in a recursive and interative approach
# This function is initialised with a sorted list to search through, a left and right pointer to eliminate the need to
# store smaller versions of our list and a target value to search for using a recursive method
def binary_search(sorted_list, left_pointer, right_pointer, target):
# Base case: if our sub-list is "empty" then we haven't found our value
    if left_pointer >= right_pointer:
        return "value not found"
	
# Calculating the middle index and middle value of our search list
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
# If our middle value is the target value we are searching for, simple return the middle index
    if mid_val == target:
        return mid_idx
# If not, we can check to see if our middle value is greater or lesser than our target value and recursively run our
# binary search function on an adjusted search list
    if mid_val > target:
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)

# Example  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))
# Output here will be:
"""
element 288 is located at index 4
"""

# This function is initialised with a search list and a target value using an iterative approach
def binary_search(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)
  
# This works similarly to the base case, keeping the function going as long as we have a sublist to search through
    while left_pointer < right_pointer:
# Calculating the middle index and middle value of the search list
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
# If the middle value is equal to our target we simple return the middle index
        if mid_val == target:
            return mid_idx
# If our target is greater or lesser than our middle value we can adjust our search list by changing the values of our
# pointers as the while loops runs
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1
# Continuation of the "base case" where with no sublist to search through, we haven't found out target  
    return "Value not in list"

# Examples
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))
# Output here will be:
"""
4
Value not in list
3
Value not in list
1
"""


## Implementing a binary search tree class, initialised with a value and depth for its root node, with pointers to
# a left and right child node, complete with methods for node insertion, node retrieval and for depth first
# traversal, all using iterative methods
import random

class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
# Insert method method initialised with a value, which will be compared iteratively to a node and its children until
# the correct location for the new node is found within the tree
    def insert(self, value):
# If our new value is less than our current node, we check to see if a left child already exists, if it does not we
# can just add our new node as a BinarySearchTree instance as our current node's left child, otherwise we recursively
# call this insert method to apply the same logic one step down
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
# Similarly to the lower value, we check to see if our value is greater than or equal to our current node, then can
# decide if we need to add a new tree one level below or further with recursion
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)
# This function takes a value as an input and recursively searches the tree until we either find the value or have
# exhausted all nodes in the tree        
    def get_node_by_value(self, value):
# If the node we are searching has a value that matches our target, we simply return the node
        if (self.value == value):
            return self
# Otherwise, if a left child exists and our target is lower than our node's value, we recursively call the function
# on our left child
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
# Similarly, if a right child exists and our target is greater than our node's value, we recursively call the
# function on our right child
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
# If we have exhausted all options and we have not found a matching node for our target, we return None
        else:
            return None
# This function uses depth-first search to traverse our tree using inline traversal, this exhausts all left children,
# before returning to traverse the parent and right sibling of each node, this way we return all nodes in ascending
# order of value 
    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if (self.right is not None):
            self.right.depth_first_traversal()

# Example
print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
    tree.insert(random.randint(0, 100))
  
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
# Output here will be:
"""
Creating Binary Search Tree rooted at value 15:
Tree node 89 added to the right of 15 at depth 2
Tree node 11 added to the left of 15 at depth 2
Tree node 9 added to the left of 11 at depth 3
Tree node 61 added to the left of 89 at depth 3
Tree node 27 added to the left of 61 at depth 4
Tree node 54 added to the right of 27 at depth 5
Tree node 38 added to the left of 54 at depth 6
Tree node 82 added to the right of 61 at depth 4
Tree node 13 added to the right of 11 at depth 3
Tree node 94 added to the right of 89 at depth 3
Printing the inorder depth-first traversal:
Depth=3, Value=9
Depth=2, Value=11
Depth=3, Value=13
Depth=1, Value=15
Depth=4, Value=27
Depth=6, Value=38
Depth=5, Value=54
Depth=3, Value=61
Depth=4, Value=82
Depth=2, Value=89
Depth=3, Value=94
"""