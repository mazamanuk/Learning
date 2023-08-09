## Creating HashMap class, initiated with array_size and an array filled with values None
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]
# Creating a hashing method, accounting for collisions
    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions
# Creating a compressor which reduces the hashed value to within array size limits
    def compressor(self, hash_code):
        return hash_code % self.array_size
# Creating an assign method which runs through hashing and compressing and looks for an index to assign a given key value pair to
# If given index has no key/correct key associated with it, assigns the key-value pair to the index
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision!
# If index contains a different key, we rehash and compress to repeat the assignment function
        number_collisions = 1

        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return
# If reassignment is not possible we increment the collision count by 1 and attempt to repeat
            number_collisions += 1
# Once the entire process is complete we return
        return
# Creating a retrieve method to return a value froma a given input key
# If given index has no key/correct key associated with it, returns None or the value respectively
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]
# Accounting for collisions, if given index does not return given key, rehash and compress to repeat the retrive function
        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]
# If retrieval is not possible, increment collision count by 1 and repeat
            retrieval_collisions += 1
# Once the entire process is complete we return
        return

# Example creation of a hashmap and assignment and retrival functionality
hash_map = HashMap(16)
hash_map.assign("gabbro","igneous")
hash_map.assign("sandstone","sedimentary")
hash_map.assign("gneiss","metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))