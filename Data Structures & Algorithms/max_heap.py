## Creating a Max-Heap class to implement a heap for storing parent child relationships and tracking the maximum
# element as the element with index 1 within an internal Python list
# The class is initialised with a heap list, consisting of just None and a count beginning from 0
class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0
# Heap helper methods to quickly find the index of parent or left or right child of a given index in the list
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1
# This method checks to see if there is a child within the list and returns True or False
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count
# Add function increases the count and adds an element to the end of the list before running the heapify up
# method used to adjust the heap property
    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()
# Heapify up method saves the last element added as our index and compares it to its parent as long as its
# parent index is greater than 0, if the parent is smaller than the child, we swap the elements in the list,
# this continues until we have restored the correct order using the helper methods
    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print("swapping {0} with {1}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))
# This function returns the maximum value in the list, whilst replacing the value at that index with the 
# value at the end of the list
    def retrieve_max(self):
# If the list is empty, print a statement and return None
        if self.count == 0:
            print("No items in heap")
            return None
# Keep track of the max value as it will be in index 1 of our list
        max_value = self.heap_list[1]
        print("Removing: {0} from {1}".format(max_value, self.heap_list))
# Replacing the value at the max position with the value at the end of the list before removing the new last
# value, this causes the heap to no longer satisfy the property that all parents have larger values than
# their children, so we use the heapify down method to restore this property
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))    
        self.heapify_down()
# Returns the max value ready to be added to a sorted list
        return max_value
# Heapify down functions very similarly to the heapify up method except we begin with a root and compare its
# value to its children and replace it with the larger child recursively until we have restored the heap
# property that all parents must have values larger than their children
    def heapify_down(self):
        idx = 1
# After we initialise our beginning node, we run the get larger child idx function to replace our node with,
# we then set child and parent variables to keep track of these two values
        while self.child_present(idx):
            print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
# If parent value is less than child value, we set the values at idx and larger_child_idx accordingly
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
# Replacing the value of our idx with our larger_child_idx to continue the loop
            idx = larger_child_idx
# Printing a statement and the heap list ready to retrieve the next max value
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("") 
# This function checks to see if a right child index exists within our list, if not we print that there
# is only a left child and return the index of that child
    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
# Otherwise, we label both children ready for comparison, if the left child is larger we print a statement
# and return the left child
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
                return self.left_child_idx(idx)
# Otherwise, we print a statement and return the right child
            else:
                print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
                return self.right_child_idx(idx)