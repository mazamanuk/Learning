## Importing Node and LinkedList classes from linked_list for use with separate chaining methods
from linked_lists import Node, LinkedList
## Importing flower definitions for use within the example
from blossom_lib import flower_definitions

## Recreating HashMap class with initial array size and array consisting of LinkedLists
class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(self.array_size)]
# Standard hashing function, encoding the key and summing
    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code
# Compression function to use hash codes within array bounds
    def compress(self, hash_code):
        return hash_code % self.array_size
# Assign method used to check whether a given key exists within the linked list
# Array position determined using the compressor and hash methods
# If key exists within the linked list at the array index, the method replaces the current value with the input value
# If key doesn't exist we insert a Node with value containing the key value pair (insert head method)
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                item[1] == value
                return
        list_at_array.insert(payload)
# Retrieve method used to return a value from the array using a given key
# Array position determined using the compressor and hash methods
# If key exists within the linked list at the array index, the method returns the current value
# If the key doesn't exist we simply return None
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                return item[1]
        return None

## Example HashMap usage with flower definitions
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(flower_definitions)
print(blossom.retrieve("daisy"))