## Implementing a tree using a TreeNode class and methods to add child, remove child and traverse a tree

from collections import deque

# TreeNode class initialised with a root node value and a reference to any children it has
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
# Creating the parent-child relationship, we print a statement and append the child node to the list of children of the parent node
    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node) 
# Removing the parent-child relationship, we print a statement and set the list of children to only include child nodes that don't
# match the node we are trying to remove
    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]
# Traverses the tree, beginning at a node and printing all values belonging to the node and its children, we label a nodes_to_visit
# variable to track the nodes that we have yet to travel "down" to, which also tells the function when to stop running, when we
# clear a node, we remove it from our list of nodes to visit and add its children to the list as we continue
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

# Creating a print tree function to visualise any tree with varying levels
def print_tree(root):
    stack = deque()
    stack.append([root, 0])
    level_str = "\n"
    prev_level = 0
    level = 0
    while len(stack) > 0:
        prev_level = level
        node, level = stack.pop()
    
        if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
            level_str += "   "*(level-1)+ "├─"
        elif level > 0:
            level_str += "   "*(level-1)+ "└─"
        level_str += str(node.value)
        level_str += "\n"
        level+=1
        for child in node.children:
            stack.append([child, level])

    print(level_str)
# Print path function prints every node in a given path to visualise traversal
def print_path(path):
    # If path is None, no path was found
    if path == None:
        print("No paths found!")

    # If a path was found, print path
    else:  
        print("Path found:")
        for node in path:
            print(node.value)

# Setting up an example tree    
sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]