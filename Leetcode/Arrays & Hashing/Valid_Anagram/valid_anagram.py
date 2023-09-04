class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If input strings aren't equal in length, return False
        if len(s) != len(t):
            return False 

        # Creating a hash map to store values related to each character in each string
        def hash_map(string):
            hash = {}
            for char in string:
                if char in hash:
                    hash[char] += 1
                else:
                    hash[char] = 1
            return hash
        
        # Return True if the hash maps of each string are equal, and False otherwise
        s_hash = hash_map(s)
        t_hash = hash_map(t)
        return s_hash == t_hash
