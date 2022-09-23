## Building a call stack with an interative function to demonstrate to implement how a call stack accumulates execution contexts during recursive function calls
# O(N)
def sum_to_one(n):
    result = 1
    call_stack = []
# Base case at n = 1 would simply return 1, while n > 1 we append to the call stack and print when adding new values to the current result    
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    while len(call_stack) > 0:
        return_value = call_stack[-1]
        call_stack.pop()
        print(call_stack)
        print(f'Adding {return_value["n_value"]} to {result}')
        result += return_value["n_value"]
    return result, call_stack

print(sum_to_one(4))
# Output here would be:
'''
[{'n_value': 4}]
[{'n_value': 4}, {'n_value': 3}]
[{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
BASE CASE REACHED
[{'n_value': 4}, {'n_value': 3}]
Adding 2 to 1
[{'n_value': 4}]
Adding 3 to 3
[]
Adding 4 to 6
(10, [])
'''


## Creating our sum_to_one function using recursion, base case at n = 1 where the function simply returns 1 and otherwise returns n + the recursive function call with argument n - 1
def sum_to_one(n):
  if n == 1:
    return n
  print(f"Recursing with input: {n}")
  return n + sum_to_one(n-1)

print(sum_to_one(7))
# Output here would be:
'''
Recursing with input: 7
Recursing with input: 6
Recursing with input: 5
Recursing with input: 4
Recursing with input: 3
Recursing with input: 2
28
'''


## Creating factorial function using recursion, base case n < 2 will return 1 otherwise prints n and returns n * the recursive function call with argument n - 1
# O(N)
def factorial(n):
  if n < 2:
    return 1
  print(n)
  return n * factorial(n-1)
# factorial(999) will throw up a RecursionError
print(factorial(999))


## Creating power set function to expand any given list of items into all combinations of those items, using an iterative method
# O(2^N)
def power_set(set):
  power_set_size = 2**len(set)
  result = []
 
  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result

## Creating power set function using recursive method
def power_set(my_list):
# Base case, empty list will return an empty list of lists
    if len(my_list) == 0:
        return [[]]
# Recursive step, subsets without first element to bring next iteration closer to the base case
    power_set_without_first = power_set(my_list[1:])
# Subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
# Return combination of the two
    return with_first + power_set_without_first

# Example  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)
# Output here would be:
'''
['MIT', 'UCLA', 'Stanford', 'NYU']
['MIT', 'UCLA', 'Stanford']
['MIT', 'UCLA', 'NYU']
['MIT', 'UCLA']
['MIT', 'Stanford', 'NYU']
['MIT', 'Stanford']
['MIT', 'NYU']
['MIT']
['UCLA', 'Stanford', 'NYU']
['UCLA', 'Stanford']
['UCLA', 'NYU']
['UCLA']
['Stanford', 'NYU']
['Stanford']
['NYU']
[]
'''


## Creating a flatten function to turn a list of lists into a simple list of items using a recursive method
def flatten(my_list):
  result = []
# Recursive step here checks to see if an element in the list is a list itself, proceeds to recursively flatten that list, then add to the end of the result list
  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      result += flat_list
# Base case here simple adds the item to the end of the result list
    else:
      result.append(item)
  return result

# Example
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))
# Output here would be:
'''
List found!
List found!
List found!
List found!
['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
'''


## Creating a Fibonacci function using multiple recursive calls
# O(2^N)
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  print(f'Adding {fibonacci(n-1)} + {fibonacci(n-2)}')
  return fibonacci(n-1) + fibonacci(n-2)

# Example
fibonacci(5)
# Output here would be:
'''
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
Adding 1 + 0
Adding 2 + 1
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
Adding 1 + 0
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
Adding 3 + 2
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
Adding 1 + 0
Adding 2 + 1
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
Adding 1 + 0
Adding 1 + 0
Adding 1 + 1
Adding 1 + 0
5
'''


## Using recursion to build a data structure, here we take an input list and use binary searches to construct a tree
# O(N*logN)
def build_bst(my_list):
# Base case, if the list is empty there is no node to consider 
    if len(my_list) == 0:
        return "No Child"
# Using the middle index to label the middle value of a given list/sublist to create the nodes acting in the parent/child relationships
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print("Middle index: " + str(middle_idx))
    print("Middle value: " + str(middle_value))
# Recursive step, we create a dictionary to keep track of the nodes and each child node recursively calls the build function until all nodes are tracked
    tree_node = {"data": middle_value, "left_child": build_bst(my_list[:middle_idx]), "right_child": build_bst(my_list[middle_idx+1:])}
    return tree_node

# Example
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
# Output here would be:
'''
Middle index: 2
Middle value: 14
Middle index: 1
Middle value: 13
Middle index: 0
Middle value: 12
Middle index: 1
Middle value: 16
Middle index: 0
Middle value: 15
{
    'data': 14,
    'left_child': {
        'data': 13,
        'left_child': {
            'data': 12, 
            'left_child': 'No Child', 
            'right_child': 'No Child',
        }, 
        'right_child': 'No Child',
    }, 
    'right_child': {
        'data': 16, 
        'left_child': {
            'data': 15, 
            'left_child': 'No Child', 
            'right_child': 'No Child'
        }, 
        'right_child': 'No Child'
    }
}
'''


## Examples
# Move to end function searches through an input list for a given value and moves every occurrence of that value to the end of the list recursively
def move_to_end(lst, val):
# Base case, empty list will return an empty list
    result = []
    if len(lst) == 0:
        return []
# Recursive step, if the first value in the list is the value given, recursively call the other values into a new list and add the given value to the end        
    if lst[0] == val:
        result += move_to_end(lst[1:], val)
        result.append(lst[0])
# Otherwise, keep the first value in the list and recursively call the function on the remaining values to sort
    else:
        result.append(lst[0])
        result += move_to_end(lst[1:], val)
    return result

# Example
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
# Output here would be:
'''
['Sapphire', 'Jade', 'Amber', 'Amber']
'''

# Remove node function used to search a linkedlist by index and remove the node associated with that index
from linked_lists import LinkedList, Node

def remove_node(head, i):
# Base case, if i is negative, returns head
  if i < 0:
    return head
# If head doesn't exist, returns None
  if head is None:
    return None
# If the index we are looking for is the first index, returns head node's next node
  if i == 0:
    return head.next_node
# Recursive step to search the remaining nodes to find the node at the given index
  head.next_node = remove_node(head.next_node, i-1)
  return head

# Example
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())
# Output here would be:
'''
['Amber', 'Jade', 'Pearl']
'''

# Wrap string function used to surround a given string by n number of <> 
def wrap_string(str, n):
    result = ""
# Base case, if number of wrappings required is <= 0, then simply return the string input
    if n <= 0:
        return str
# Recursive step adds the < to an empty string labelled result, before the recursive function call as n decrements to 0 before adding the > to close the wrapping
    result += "<"
    result += wrap_string(str, n-1)
    result += ">"
    return result

# Example
wrapped = wrap_string("Pearl", 3)
print(wrapped)
# Output here would be:
'''
<<<Pearl>>>
'''