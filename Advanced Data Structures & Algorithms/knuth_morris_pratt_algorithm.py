## Knuth-Morris_Pratt algorithm makes use of information related to the pattern itself to speed up the traditional brute force approach to pattern searching
# We do this by implementing a prefix function which looks to find a proper prefix and suffix of a partial match within our pattern, to skip some comparisons, since we know which bits are exact matches and no longer need to consider every character
# The implementation makes use of lists and some clever manipulations to reduce the running time of computing the prefix function


## Implementing the prefix function
# We map a pattern to an array of numbers, at each index the array contains the length of the longest proper suffix up to that index int he pattern
# The additional requirement is that the proper suffix must also be a proper prefix in the pattern


def prefix_function(pattern):
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

print(prefix_function('ababac'))
# Output here will be:
"""
[0, 0, 1, 2, 3, 0]
"""


## Computing the Prefix Function Faster - Part 1
# Previous implementation requires double for loops resulting in poor run time
# Notice each consecutive value can only increase at most by 1, because each index is increasing by 1 and so each corresponding length of a valid suffix can increase by no more than 1.
# This leaves us with 3 cases: 1 - the value can increase by 1; 2 - the value can NOT increase at all i.e. stays the same; 3 - the value can actually decrease by a certain amount


def prefix_function(pattern):
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
  pi = [0 for i in range(len(pattern))]
  for i in range(1, len(pattern)):
    j = pi[i - 1]
    while (j > 0 and pattern[i] != pattern[j]):
      j = pi[j - 1]
    if (pattern[i] == pattern[j]):
      j += 1
      pi[i] = j
  return pi
