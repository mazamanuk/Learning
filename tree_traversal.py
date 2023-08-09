## Using BFS and DFS to traverse a tree and explore different methods of searching through nodes to find a target value
# Creating a Breadth-First Search function to search a given tree level by level until a goal value has been found,
# then returning the path to that value from the root node
# To do this, we import deque to hold our paths and to inform the function on which path to take next
from collections import deque

# bfs function initialised with a starting node, a goal value and a path frontier queue
def bfs(root_node, goal_value):

    path_queue = deque()

# Add the root node as the initial path to our path queue
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
# The function will search as long as there are paths in the queue to search through
    while path_queue:
# Setting the current path equal to the first element in the queue, and setting the current node equal to the last
# node in the current path, then we print a statement 
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

# If the goal node is found, we return the current path to the node from the root
        if current_node.value == goal_value:
            return current_path

# Otherwise we create copies of the current path for each child of the current node and append the child to the end
# We then add these new paths to our path queue and continue iterating through
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

# If goal value is not found we return None
    return None


##
from trees import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)
# Output here will be:
"""
A
├─B
   ├─D
   └─E
└─C
   ├─F
   └─G
"""

# dfs function uses recursion to return a path when a given target value has been found in a tree, using a node's children
# recursively as root nodes, we keep track of the path in a tuple, adding the current root to the tuple as we go
def dfs(root, target, path=()):
    path = path + (root,)
# If target is found, we return the path
    if root.value == target:
        return path
# For each child in the children of the root node, we recursively run the dfs function whilst adding to the path, if any
# of these calls would return None, we continue to the next node 
    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found
# If target is not found, we return None for a given path and move on
    return None

path = dfs(sample_root_node, "F")
print(path)
# Output here will be:
"""
(A, C, F)
"""