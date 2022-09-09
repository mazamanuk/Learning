from nodes import Node

## Stack class created with default stack limit set to 1000, top item instance set to None and initial size 0
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
# push method adds an item to the top of the stack and sets this item as the new head, if no more space,
# prints a statement
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value)) # example code addition
        else:
            print("No room for {}!".format(value)) # example code addition
          # print("All out of space!")
# pop method removes the top item from the stack and returns its value, if stack is empty, prints a statement
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value()) # example code addition
            return item_to_remove.get_value()
        print("All out of pizza.") # example code addition
      # print("This stack is totally empty.")
# peek method returns the value of the top item of the stack, if stack is empty, prints a statement
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")
# has_space method returns True only if current stack size is lower than the stack limit
    def has_space(self):
        return self.limit > self.size
# is_empty method returns True only if the current stack size is 0
    def is_empty(self):
        return self.size == 0

# Example
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
#pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
#pizza_stack.pop()