## Creating Node class, initiated with a value and a next_node with default value None
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
# Creating methods to return value and next_node and setting next_node
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

## Creating LinkedList class, initiated with a value with default value None
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
# Creating methods to return and insert a head_node
    def get_head_node(self):
        return self.head_node
  
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
# Returns a string containing all values from all nodes within the linked list
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
# Checks if the head_node contains the value to remove and if not we loop through the remaining nodes to find this value
# Then sets a new head node or restores links around the removed node
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

## Swapping elements in a linked list
# Iterating through the list looking for the node that matches val1 and and its previous node
# node1_prev and repeating for val2 and node2_prev
def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None
# Edge case: If both nodes are the same we end the method as there is no need to execute the whole function
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()
# Edge case: If no matching node for one of the inputs, the function will not run, check ends the method afterwards
    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return
# setting node1_prev and node2_prev by checking if node1_prev is None, if yes then node1 is the head
# of the list and we update the head to be node2, similarly for node2
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)
# Updating pointers from node1 and node2
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

# Example
ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 0)
print(ll.stringify_list())

## Two pointer linked list techniques
# Two pointers moving in parallel

# This is inefficient, storing values in a list requires an extra O(n) space being allocated
def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]

# Solution: completes problem in O(n) time (iterates through list once) and O(1) space complexity
# only three variables required - two pointers and a counter
def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
        else:
            current = current.get_next_node()
    return current

# Testing the nth_last_node function
def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

# Pointers at different speeds

# Using a list is also inefficient here, where we can instead use pointers moving at different speeds
# Solution: has O(n) time complexity and O(1) space complexity, always two variables - two pointers
def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Testing the middle_node function:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)

# Alternate solution
def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if count % 2 != 0:
            slow = slow.get_next_node()
        count += 1
    return slow

# Variations on the two-pointer technique can be used to:
# - Detect a cycle in a linked list
# - Rotate a linked list by k places