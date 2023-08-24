## Knuth-Morris_Pratt algorithm makes use of information related to the pattern itself to speed up the traditional brute force approach to pattern searching
# We do this by implementing a prefix function which looks to find a proper prefix and suffix of a partial match within our pattern, to skip some comparisons, since we know which bits are exact matches and no longer need to consider every character
# The implementation makes use of lists and some clever manipulations to reduce the running time of computing the prefix function


## Implementing the prefix function
# We map a pattern to an array of numbers, at each index the array contains the length of the longest proper suffix up to that index int he pattern
# The additional requirement is that the proper suffix must also be a proper prefix in the pattern


def inefficient_prefix_function(pattern):
    # Instantiate a list containing 0s for each character in the pattern
    pi = [0 for i in range(len(pattern))]
    # For each character from 1 to the length of the pattern, we check to see the longest proper prefix up to that character and see if it is equal to the proper suffix of the same length
    for i in range(1, len(pattern)):
        for j in range(1, i + 1):
            # Checking if proper prefix == proper suffix
            if pattern[:j] == pattern[i - j + 1: i + 1]:
                # Updating the value in our list if we find a match
                pi[i] = j
    # Return our 
    return pi

print(inefficient_prefix_function('ababac'))
# Output here will be:
"""
[0, 0, 1, 2, 3, 0]
"""


## Computing the Prefix Function Faster - Part 1
# Previous implementation requires double for loops resulting in poor run time
# Notice each consecutive value can only increase at most by 1, because each index is increasing by 1 and so each corresponding length of a valid suffix can increase by no more than 1.
# This leaves us with 3 cases: 1 - the value can increase by 1; 2 - the value can NOT increase at all i.e. stays the same; 3 - the value can actually decrease by a certain amount


def faster_prefix_function(pattern):
    pi = [0 for i in range(len(pattern))]
    for i in range(1, len(pattern)):
        # 1 - If there is a proper prefix of length pi[i - 1] + 1, that is also a proper suffix of the same length, this is the valid prefix/suffix we are looking for, update pi[i] to this length
        if (pattern[:pi[i - 1] + 1] == pattern[i - pi[i - 1]: i + 1]):
            pi[i] = pi[i - 1] + 1
        # 2 - If there is a proper prefix of length pi[i - 1], that is also a proper suffix of the same length, this is the valid prefix/suffix we are looking for, update pi[i] to this length
        elif (pattern[:pi[i - 1]] == pattern[i - pi[i - 1] + 1: i + 1]):
            pi[i] = pi[i - 1]
        # 3 - We finally check all lengths from pi[i - 1] - 1 down to 0 by looping through each length to find a proper prefix equalling a proper suffix, if there is one we update pi[i] and break out of the for loop
        # This creates another for loop, but this extra loop can add a large constant factor (as opposed to the size of the input itself) at most, so the overall running time is O(n^2)
        else:
            for j in range(pi[i - 1], -1, -1):
                if pattern[: j] == pattern[i - j + 1: i + 1]:
                    pi[i] = j
                    break
        # Finally return pi
        return pi
    

## Computing the Prefix Function Faster - Part 2
# Previously we reduced the running time of computing the prefix function to O(n^2), but we can actually reduce it to linear time
# What we want to know is, is pattern[i] == pattern[pi[i - 1]]?
# This is because pi[i - 1] can be interpreted as the length of the longest prefix that is also a proper suffix ending at i - 1
# This means, if we index pi[i - 1] into the pattern as pattern[pi[i - 1]], we are actually accessing the character next to that longest prefix
# If the next character in pattern, pattern[i], matches pattern[pi[i - 1]], this means pi[i] is longer than pi[i - 1] by 1, because we will be adding the same character pattern[i] to extend the valid suffix ending at i - 1 to form the next valid suffix ending at i
# In the opposite case that pattern[i] != pattern[pi[i - 1]], look for valid suffix of a shorter length j = pi[i - 1] - 1, index into the prefix function as pi[j] giving the length of the valid suffix ending at index j
# Index into pattern as pattern[pi[j]] giving the character next to a valid prefix, check to see if pattern[i] == pattern[pi[j]] and we can loop the entire process above from this point onwards


def prefix_function(pattern):
    # Initialise our list of 0s
    pi = [0 for i in range(len(pattern))]
    # Begin looping through the characters in our pattern
    for i in range(1, len(pattern)):
        # Initialise j to be pi[i - 1], this will be used to compute the length of the next valid suffix ending at i
        j = pi[i - 1]
        # Loop as long as our longest valid suffix is still greater than 0 and our current character is not equal to the character after the end of the longest valid suffix
        while (j > 0 and pattern[i] != pattern[j]):
            # Update j to equal the length of a shorter valid suffix i.e j = pi[j - 1]
            j = pi[j - 1]
        # If our character is equal to the longest valid suffix, then pattern[i] is part of the valid suffix ending at i, whose length is longer than the valid suffix ending at i - 1 by 1
        # increment j by 1 and store the value in our pi list
        if (pattern[i] == pattern[j]):
            j += 1
            pi[i] = j
    # Finally return pi
    return pi


## Implementing the Knuth-Morris-Pratt algorithm
# We start the algorithm by matching the pattern against the text character-by-character, if there is a mismatch, we look for a shorter valid prefix that can potentially align with an existing valid suffix among the characters that have already matched (similar to how we calculated the prefix function)
# However, unlike last time, we don't have to look for the length of a valid prefix all over again as it has been calculated and stored in the prefix function
# Finally, if at any point the number of matched characters equals the length of the pattern, we will have found an occurrence of the pattern in the text
# We can repeat the algorithm to find the next occurence by looking for a shorter valid prefix length


def kmp_algorithm(pattern, text):
    # Storing pattern and text lengths in variables along with our prefix function applied to pattern stored in pi, a variable j to store the number of characters matched so far and a variable count to store the number of occurrences of pattern in text
    pattern_length = len(pattern)
    text_length = len(text)
    pi = prefix_function(pattern)
    j = 0
    count = 0
    # Loop through each index in text
    for i in range(text_length):
        # Loops as long as number of matched characters is greater than 0 and the next character in the text isn't equal to the next character after j matches to set j to some shorter valid prefix, j = pi[j - 1] 
        while (j > 0 and text[i] != pattern[j]):
            j = pi[j - 1]
        # If our next character matches, we increment our matched character count by 1
        if text[i] == pattern[j]:
            j += 1
            # If the number of matches equals the length of our pattern we increment the occurrence count and reset j to some shorter valid suffix
            if j == pattern_length:
                count += 1
                j = pi[j - 1]
    # Finally return the number of occurrences of the pattern within the text
    return count


## Rabin-Karp vs KMP

import time

# Prefix function and KMP algorithm have been defined above so won't be redefined here

# Redefining polynomial hash, polynomial rolling hash and Rabin-Karp algorithm functions to compare speeds
def polynomial_hash(s):
	hash_value = 0
	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

def rabin_karp_algorithm(pattern, text):
	pattern_hash = polynomial_hash(pattern)
	occurrences = 0
	text_length = len(text)
	pattern_length = len(pattern)
	substring_hash = polynomial_hash(text[:pattern_length])
	if (substring_hash == pattern_hash):
		occurrences += 1
	for i in range(text_length - pattern_length):
		previous_hash = substring_hash
		substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)
		if (substring_hash == pattern_hash):
			occurrences += 1
	return occurrences


pattern = ""
for i in range(1000):
  pattern += "A"
text = ""
for i in range(100000):
	text += "A"

# smaller text with Rabin-Karp algorithm runtime: 0.5520007610321045 seconds 
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
# Output here will be:
"""
99001
"""

# smaller text with Knuth-Morris-Pratt algorithm runtime: 0.023000478744506836 seconds
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))
# Output here will be:
"""
99001
"""

pattern="ababbabbabbababbabb"
text = 100000*pattern

# larger text with Rabin-Karp algorithm runtime: 1.2552695274353027 seconds
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
# Output here will be:
"""
100000
"""


# larger text with Knuth-Morris-Pratt algorithm runtime: 0.37999892234802246 seconds
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))
# Output here will be:
"""
100000
"""
