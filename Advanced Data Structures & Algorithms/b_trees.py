## A B-tree is a balanced search tree designed to be an efficient data structure when working on physical storage devices like discs.
# When storing large amounts of data, we can distribute that data across many disk blocks, and while it may be quick to search a single block, new data structures are needed to search across the many blocks being used.
# A B-tree can have more than one key per node. It can also have more than two children. This essentially makes each block a node, as we can search the node for a value, and then know the best path to other nodes (current node's children) if that value is not at our current node.


## B-Tree Nodes
# Representing B-trees and B-tree nodes as Python objects, we have some important characteristics:
# Nodes can have multiple keys
# Nodes can have multiple children
# The maximum amount of keys ina  node is 2t - 1 where t is the "branching factor"


class BTreeNode():
    def __init__(self, t):
        # Initialising keys and children as empty lists, leaf as True and t as t
        self.keys = []
        self.children = []
        self.leaf = True
        self.t = t

    @property
    def _is_leaf(self):
        # Returns boolean value depending on if a node has 0 children
        return len(self.children) == 0

    @property
    def _is_full(self):
        # Returns boolean based on whether keys is equal to the maximum number of keys in a node
        return self._size == 2 * self.t - 1

    @property
    def _size(self):
        # Returns the number of keys contained in a node's keys list
        return len(self.keys)
    
    def add_key(self, value):
        # Inserting a value in our list of keys if we can find another key to compare our value to
        for i in range(len(self.keys)):
            if value < self.keys[i]:
                self.keys.insert(i, value)
        # If our value is larger than our other keys, we append to the end of the list
        else:
            self.keys.append(value)
    
    def split(self, parent, value):
        # Create a new node with the same branching factor and store the middle value in our keys in a variable
        new_node = BTreeNode(self.t)
        split_key = self.keys[self._size // 2]
        # Add the middle value to our parent node
        parent.add_key(split_key)
        # Splitting the right half of our children and key values into the new node
        # New node at the same level as the old node
        new_node.children = self.children[self._size // 2 + 1:]
        new_node.keys = self.keys[self._size // 2 + 1:]
        # Splitting the left half of our children and key values into the existing node
        # Not plus 1 as that goes to the parent
        self.children = self.children[:self._size // 2]
        self.keys = self.keys[:self._size // 2]
        # Adding the new node as a child of our parent node
        parent.childen = parent.add_child(new_node)
        # If the value added is greater than our middle key, return the newly created child, otherwise return the existing child node
        if value < split_key:
            return self
        return new_node

    def add_child(self, new_node):
        # Given a node as a parameter, this function will locate the correct place to add the child node based on the key values
        # When comparing key values, the important keys to compare are the first keys in the child nodes
        new_node_first_key = new_node.keys[0]
        for i in range(len(self.children)):
            if new_node_first_key < self.children[i].keys[0]:
                return self.children[:i] + [new_node] + self.children[i:]
        return self.children + [new_node]

class BTree:
    def __init__(self, t):
        # Initialising t as t and root as a BTreeNode holding the branching factor t
        self.t = t
        self.root = BTreeNode(t)

    def find_correct_child_node(self, node, value):
        # Loop until a suitable child is found
        i = 0
        while i < node._size and value > node.keys[i]:
            i += 1
        return node.children[i]

    def insert(self, value):
        # We begin at the root node and traverse down until we find a suitable node to store the new value
        node = self.root
        # If root is full, create a new root
        if node._is_full:
            new_root = BTreeNode(self.t)
            # The new root will have the old root as a child
            new_root.children.append(node)
            # Splitting the old root
            node = node.split(new_root, value)
            # Setting the new root
            self.root = new_root

        # Finding a spot for the new value
        while node._is_leaf is False:
            child_node = self.find_correct_child_node(node, value)
            # Split ahead of time
            if child_node._is_full:
                node = child_node.split(node, value)
            else:
                node = child_node
        # Finally add the value as a key to our stored node
        node.add_key(value)

    def search(self, value, node=None):
        # If our node is None, set node to the root
        if node == None:
            node = self.root
        
        # If our value is in our node's keys list, return True
        if value in node.keys:
            return True
        
        # If we've reached a leaf, we can't go any deeper in our tree so the value doesn't exist
        elif node._is_leaf:
            return False
        
        # Recursive step, using a different node to check for our search value
        else:
            child_node = self.find_correct_child_node(node, value)
            return self.search(value, child_node)


## Insert Part 1: Intro
# When inserting a new value, we first check if the root has space
# If so, and the root is a leaf, we can insert the value into the root
# To insert a value into a node, we need to make sure the keys stay in order, and this we inset in order (don't append and then sort)


## Insert Part 2: Splitting nodes to children
# If the current node we are at is full, we begin by finding the appropriate child node to traverse down.
# A node will have a maximum number of keys; the children will have 2t - 1 keys and 2t children
# Since the keys are ordered, the appropriate child to choose when traversing down the tree is the one "in-between" the keys the value is in between, for example.
# If the value we are inserting is 5 and the keys are [1, 2, 4, 7, 8], the appropriate child to traverse down would be the 3rd child, which is "in-between" keys 4 and 7


## Insert Part 3: Finish up
# We now focus on implementing the logic of traversing the BTree when trying to insert, including when to split and add new children if necessary


## Search
# The idea is similar to insert, for each node we encounter, check the keys to see if the target value is present
# If not, using the keys, find the correct child node to traverse down
# Continue this until we find the target value or until we find a leaf with no children, signalling the target value does not exist


## Testing


btree = BTree(3)
btree.insert(2)
btree.insert(3)
btree.insert(4)
btree.insert(5)
btree.insert(6)
btree.insert(1)
print(btree.root.keys)
print(btree.root.children)
print(btree.search(2))
# Output here will be:
"""
[4]
[<__main__.BTreeNode object at 0x7ff1cab74f28>, <__main__.BTreeNode object at 0x7ff1cab74f98>]
True
"""

node1 = BTreeNode(5)
node1.keys = [1, 4, 29]

node2 = BTreeNode(5)
node2.keys = [2,3]

node3 = BTreeNode(5)
node3.keys = [5,6]
node1.children = [node2, node3]
node4 = BTreeNode(5)
node4.keys = [30]
node1.add_child(node4)
