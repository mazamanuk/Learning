## Analyzing runtime of functions
def count(N):
    count = 0
    while N > 1:
        N = N//2
        count += 1
    return count

num_iterations_1 = 0
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))
num_iterations_2 = 1
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))
num_iterations_4 = 2
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))
num_iterations_32 = 5
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))
num_iterations_64 = 6
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))


## Finding the maximum value in a list
from linked_lists import LinkedList

def find_max(linked_list):
    print("--------------------------")
    print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
    current_node = linked_list.get_head_node()
    max_value = current_node.get_value()
    while current_node.get_next_node():
        current_node = current_node.get_next_node()
        if max_value < current_node.get_value():
            max_value = current_node.get_value()
    return max_value

# Examples, creating linked lists and running the find_max function to return the maximum value in the linked lists
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

# When traversing the linked list we require at most N searches
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))


## Sorting a linked list
from linked_lists import LinkedList

def find_max(linked_list):
  current = linked_list.get_head_node()
  maximum = current.get_value()
  while current.get_next_node():
    current = current.get_next_node()
    val = current.get_value()
    if val > maximum:
      maximum = val
  return maximum

def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  #Write Code Here!
  while linked_list.get_head_node():
    new_linked_list.insert_beginning(find_max(linked_list))
    linked_list.remove_node(find_max(linked_list))
  return new_linked_list

# Examples, creating linked lists and running the sort_linked_list function to sort the linked lists from smallest to largest values
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

# When traversing the linked list, for each element in N we call find_max which has a runtime of O(N)
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))


## Stacks vs Queues runtime
from stacks import Stack
from queue import Queue

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

# Printing the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))

# Get First Value added to Queue
first_value_added_to_queue = my_queue.dequeue()
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1"
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

# Get First Value added to Stack
while not my_stack.is_empty():
  first_value_added_to_stack = my_stack.pop()
print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "N"
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))


## HashMaps vs Linked Lists runtime
from hash_maps import HashMap
from linked_lists import LinkedList

N = 6

my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

# Get Zachary's Disease from a HashMap
hashmap_zachary_disease = my_hashmap.retrieve("Zachary")
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1"
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


# Get Zachary's Disease from a Linked List
current = my_linked_list.get_head_node()
while current.get_value()[0] != "Zachary":
  current = current.get_next_node()
linked_list_zachary_disease = current.get_value()[1]
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N"
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))