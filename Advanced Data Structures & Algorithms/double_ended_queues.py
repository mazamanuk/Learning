# A deque, which stands for double-ended queue, is a data structure that allows users to insert and delete items at both ends of the queue.
# Because we can insert and delete from both ends, a deque is considered both a a queue and a stack.


class Deque:
    # Initialise deque using a list to store elements
    def __init__(self):
        self.elements = []

    # Adds an item to the front of the deque, time complexity is O(1)
    def add_first(self, item):
        self.elements.append(item)

    # Adds an item to the rear of the deque, time complexity is O(1)
    def add_last(self, item):
        self.elements.insert(0, item)

    # Removes (and returns) the item in the front of the deque, time complexity is O(1)
    def remove_first(self):
        item = self.elements.pop()
        return item

    # Removes (and returns) the item in the rear of the deque, time complexity is O(1)
    def remove_last(self):
        item = self.elements.pop(0)
        return item

    # Returns True if the deque is empty and False otherwise
    def is_empty(self):
        # Implement here (remove pass)
        return len(self.elements) == 0

    # Returns the size of the deque (number of elements)
    def size(self):
        # Implement here (remove pass)
        return len(self.elements)

    # Allows us to view the front or rear items in the deque without removing them
    def peek_first(self):
        return self.elements[-1]

    def peek_last(self):
        return self.elements[0]

    # Displays the deque separated by spaces and |
    def display_deque(self):
        print("\t | \t".join(str(item) for item in self.elements))


deque = Deque()
deque.add_first(5)
deque.add_first(20)
deque.add_last(42)
popped_front = deque.remove_first()
print("Popped value: " + str(popped_front))
popped_rear = deque.remove_last()
print("Popped value: " + str(popped_rear))
# Test deque method below
print(deque.is_empty())
print(deque.size())
deque.remove_first()
print(deque.is_empty())
print(deque.size())
deque.display_deque()

# Output here will be:
"""
Popped value: 20
Popped value: 42
False
1
True
0
"""
