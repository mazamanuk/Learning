## Defining TrieNode and Trie classes
# TrieNode is an object storing reference nodes to all characters that follow this character in a stored string, whether the character is the end of a stored word and it's existence frequency as a prefix in other stored words

class TrieNode:
    def __init__(self):
        # Initialising TrieNode instance with a nodes dictionary, end_of_word boolean and freq counter
        self.nodes = {}
        self.end_of_word = False
        self.freq = 0

    def add_char(self, c):
        # If character doesn't exist in our nodes dictionary, add a key: value pair of charactr: TrieNode instance
        if c not in self.nodes:
            self.nodes[c] = TrieNode()
        # Return the reference to the TrieNode
        return self.nodes[c]

# Trie is an object that acts similarly to a Tree object, storing TrieNodes containing references to other TrieNodes, it has a root and methods used to add strings, search for strings and count the number of words an input prefix is part of

class Trie:
    def __init__(self):
        # Initialises the root of the Trie as an instance of TrieNode
        self.root = TrieNode()

    def add_string(self, string: str) -> None:
        # Sets the nxt variable to root, loops through each character in the input string and reassigns nxt as it adds references to the following character in the TrieNode's nodes dictionary
        nxt = self.root
        for char in string:
            nxt = nxt.add_char(char)
            # Increasing self.freq by 1 to track how many words this character is a prefix for
            nxt.freq += 1
        # Sets the end character of our string's end_of_word attribute to True to show a word has been added to our Trie
        nxt.end_of_word = True

    def search_string(self, string: str) -> bool:
        # Sets the nxt variable to root, loops through each character in the input string and determines whether the character exists in nxt's nodes dictionary
        # If it doesn't exist, return False, if it does, reassign nxt to a reference of that TrieNode and continue looping
        # Finally, return nxt's end_of_word to determine whether the string input has been added to the Trie
        nxt = self.root
        for char in string:
            if char not in nxt.nodes:
                return False
            nxt = nxt.nodes[char]
        return nxt.end_of_word

    def count_prefix(self, prefix: str) -> int:
        # Sets nxt variable to root, loops through each character in the prefix and determines whether the next character exists in nodes dictionary
        # If it doesn't exist, return the current node's freq, if it does, reassign nxt to a reference of that TrieNode and continue looping
        # Finally return nxt's freq to output the number of words with a prefix up to that character
        nxt = self.root
        for char in prefix:
            if char not in nxt.nodes:
                return nxt.freq
            nxt = nxt.nodes[char]
        return nxt.freq


## Using a Trie
# Using the data structure above, we will create a Trie, store words and test the class methods for adding strings, searching strings and counting prefixes


# Initialising an instance of a Trie
trie = Trie()

# Defining a list of words to be added to the Trie using the .add_string method
words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", "BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", "DRAMA", "MESS", "MAVERICK", "MAVEN", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP", "ZIP", "ZIPPER"]

for word in words:
    trie.add_string(word)
# Output here will be:
"""
AMPLE
BALLOON
BALL
DUTCH
DECK
MAVERICK
PHYSICS
PHONE
PHANTOM
PASS
ZEST
ZAP
ZIP
"""

# Defining more words to be used with the .search_string method
more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", "BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP", "MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP", "ZEBRA"]

for word in more_words:
    if trie.search_string(word):
        print(word)

# Defining prefixes to print the value of the existence of these prefixes in our Trie of words
prefixes = ["A", "AM", "B", "BALL", "BA", "C", "CA" "DUTCH", "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for prefix in prefixes:
    print(trie.count_prefix(prefix))
# Output here will be:
"""
3
2
4
2
3
0
0
1
0
0
2
6
3
1
5
2
"""