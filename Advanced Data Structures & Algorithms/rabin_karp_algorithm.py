prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

## Revisiting naive pattern-matching
# steps: iterate over the entire string to find all substrings equal in length to the pattern that we are trying to match
# iterate over each substring, and check to see if this matches the pattern


def naive_pattern_matching(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    occurrences = 0
    # Loop through for the start of each substring matching our pattern length
    for i in range(text_length - pattern_length + 1):
        # Initialise a variable to True, assuming there exists a string that matches our pattern
        pattern_match = True
        # Loop through the length of our pattern to match characters to our substring
        for j in range(pattern_length):
            # If the pattern doesn't match at any point, set variable to False and break out of this loop
            if pattern[j] != text[i + j]:
                pattern_match = False
                break
        # Increase count if variable is still true after looping through each character
        if pattern_match == True:
            occurrences += 1
    return occurrences


# Example: takes ~9 seconds to loop through
pattern = "A" * 1000
text = "A" * 100000

print(naive_pattern_matching(pattern, text))
# Output here will be:
"""
99001
"""


## Revisiting hashing
# Function used to map characters to numerical values to make comparisons simpler

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_values = dict()
for c in uppercase:
    ascii_values[c] = ord(c)
print(ascii_values)
# Output here will be:
"""
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}
"""


def ascii_hash(s):
    # Simple hashing function that multiplies ascii values together to return a hash value
    hash_value = 1
    for char in s:
        hash_value *= ascii_values[char]
    return hash_value


# Calculating and storing hash values for all substrings of uppercase variable of length 4
ascii_hash_values = {}
for char in range(len(uppercase) - 3):
    substring = uppercase[char : char + 4]
    hash_value = ascii_hash(substring)
    ascii_hash_values[substring] = hash_value
print(ascii_hash_values)
# Output here will be:
"""
{'ABCD': 19545240, 'BCDE': 20748024, 'CDEF': 22005480, 'DEFG': 23319240, 'EFGH': 24690960, 'FGHI': 26122320, 'GHIJ': 27615024, 'HIJK': 29170800, 'IJKL': 30791400, 'JKLM': 32478600, 'KLMN': 34234200, 'LMNO': 36060024, 'MNOP': 37957920, 'NOPQ': 39929760, 'OPQR': 41977440, 'PQRS': 44102880, 'QRST': 46308024, 'RSTU': 48594840, 'STUV': 50965320, 'TUVW': 53421480, 'UVWX': 55965360, 'VWXY': 58599024, 'WXYZ': 61324560}
"""

# Issues like this can occur where multiple strings can have the same hash value, so collisions occur when hashing
string1 = "AT"
string2 = "NF"
colliding_hash_values = {string1: ascii_hash(string1), string2: ascii_hash(string2)}
print(colliding_hash_values)
# Output here will be:
"""
{'AT': 5460, 'NF': 5460}
"""


## Hashing collision
# Attempting to reduce the number of collisions by using prime values when hashing so prime factors are no longer an issue with strings containing different characters

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def prime_value(c):
    return prime_numbers[ord(c) - ord("A")]


# Creating a prime value dictionary for each character in uppercase, using the prime value function defined above
prime_values = {char: prime_value(char) for char in uppercase}
print(prime_values)
# Output here will be:
"""
{'A': 2, 'C': 5, 'B': 3, 'E': 11, 'D': 7, 'G': 17, 'F': 13, 'I': 23, 'H': 19, 'K': 31, 'J': 29, 'M': 41, 'L': 37, 'O': 47, 'N': 43, 'Q': 59, 'P': 53, 'S': 67, 'R': 61, 'U': 73, 'T': 71, 'W': 83, 'V': 79, 'Y': 97, 'X': 89, 'Z': 101}
"""


def prime_hash(s):
    # Simple prime hashing function that removes the issue of different characters in strings having the same prime factors, and therefore the same hash value
    hash_value = 1
    for c in s:
        hash_value *= prime_value(c)
    return hash_value


# Calculating and storing hash values for all substrings of length 4 of the original uppercase variable using the prime hash function defined above
prime_hash_values = {}
for char in range(len(uppercase) - 3):
    substring = uppercase[char : char + 4]
    hash_value = prime_hash(substring)
    prime_hash_values[substring] = hash_value
print(prime_hash_values)
# Output here will be:
"""
{'ABCD': 210, 'JKLM': 1363783, 'UVWX': 42600829, 'KLMN': 2022161, 'BCDE': 1155, 'OPQR': 8965109, 'HIJK': 392863, 'FGHI': 96577, 'WXYZ': 72370439, 'LMNO': 3065857, 'QRST': 17120443, 'IJKL': 765049, 'PQRS': 12780049, 'MNOP': 4391633, 'DEFG': 17017, 'EFGH': 46189, 'STUV': 27433619, 'TUVW': 33984931, 'RSTU': 21182921, 'CDEF': 5005, 'NOPQ': 6319667, 'VWXY': 56606581, 'GHIJ': 215441}
"""


# Collision issues can still occur when the strings are reversed
string1 = "AB"
string2 = "BA"
colliding_hash_values = {string1: prime_hash(string1), string2: prime_hash(string2)}
print(colliding_hash_values)
# Output here will be:
"""
{'AB': 6, 'BA': 6}
"""


## Rolling hash
# We can bypass some of the calculations when computing the hash value of all substrings.
# After calculating the rolling hash of "ABCD", we no longer need to calculate the hash of "BCD" for the next iteration, as we can simply divide by the hash of the character being removed and multiply by the hash of the character being added.

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

prime_values = {}
for c in uppercase:
    prime_values[c] = prime_value(c)
print(prime_values)
# Output here will be:
"""
{'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13, 'G': 17, 'H': 19, 'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47, 'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71, 'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97, 'Z': 101}
"""

# Demonstrating how a rolling hash can be calculated.
# Divide a given prime hash by the hash value of the character being replaced ("A") and multiply by the hash of the character being added ("E")
prime_hash_ABCD = prime_hash("ABCD")
rolling_hash_BCDE = prime_hash_ABCD // prime_hash("A") * prime_hash("E")
prime_hash_BCDE = prime_hash("BCDE")
print(rolling_hash_BCDE)
print(prime_hash_BCDE)
# Output here will be:
"""
1155
1155
"""


def prime_rolling_hash(s, p, c):
    # A simple rolling hash function that takes a given substring, the prime hash value of that substring and the next character to be included and returns a rolling hash value
    rolling_hash = p // prime_hash(s[0]) * prime_hash(c)
    return rolling_hash


# Set up initial string and prime hash to be added to a rolling hash value dictionary
s = "ABCD"
p = prime_hash(s)
prime_rolling_hash_values = {s: p}

# Loop through every other character in uppercase variable to add rolling hash values to dictionary
for c in uppercase[4:]:
    p = prime_rolling_hash(s, p, c)
    s = s[1:] + c
    prime_rolling_hash_values[s] = p

print(prime_rolling_hash_values)
# Output here will be:
"""
{'ABCD': 210, 'BCDE': 1155, 'CDEF': 5005, 'DEFG': 17017, 'EFGH': 46189, 'FGHI': 96577, 'GHIJ': 215441, 'HIJK': 392863, 'IJKL': 765049, 'JKLM': 1363783, 'KLMN': 2022161, 'LMNO': 3065857, 'MNOP': 4391633, 'NOPQ': 6319667, 'OPQR': 8965109, 'PQRS': 12780049, 'QRST': 17120443, 'RSTU': 21182921, 'STUV': 27433619, 'TUVW': 33984931, 'UVWX': 42600829, 'VWXY': 56606581, 'WXYZ': 72370439}
"""


## Polynomial hash function
# Implementing a polynomial hash function that makes use of sums and products together to calculate a hash value and and is therefore almost entirely immune to hash values colliding

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def polynomial_hash(s):
    # Initialise a hash value to 0 and add each character of the substring's ascii value multiplied by the alphabet size raised to the power of the number of remaining characters
    hash_value = 0
    pattern_length = len(s)
    for char in range(pattern_length):
        hash_value += ord(s[char]) * 26 ** (pattern_length - (char + 1))
    return hash_value


polynomial_hash_values = dict()

# Loop through all substrings of length 4 in our uppercase variable, pass the value into the polynomial_hash function and store the value in the polynomial_hash_values dictionary
for char in range(len(uppercase) - 3):
    substring = uppercase[char : char + 4]
    hash_value = polynomial_hash(substring)
    polynomial_hash_values[substring] = hash_value

print(polynomial_hash_values)
# Output here will be:
"""
{'ABCD': 1188866, 'BCDE': 1207145, 'CDEF': 1225424, 'DEFG': 1243703, 'EFGH': 1261982, 'FGHI': 1280261, 'GHIJ': 1298540, 'HIJK': 1316819, 'IJKL': 1335098, 'JKLM': 1353377, 'KLMN': 1371656, 'LMNO': 1389935, 'MNOP': 1408214, 'NOPQ': 1426493, 'OPQR': 1444772, 'PQRS': 1463051, 'QRST': 1481330, 'RSTU': 1499609, 'STUV': 1517888, 'TUVW': 1536167, 'UVWX': 1554446, 'VWXY': 1572725, 'WXYZ': 1591004}
"""


## Exploiting the "rolling" property again
# We want to be able to use a calculated value to create the next value in the hashing function, rather than recalculate every time, so we implement the rolling property with our polynomial hash function

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Calculating the polynomial rolling hash value (incorrectly) using previous rules
polynomial_hash_ABCD = polynomial_hash("ABCD")
rolling_hash_BCDE = polynomial_hash_ABCD - polynomial_hash("A") + polynomial_hash("E")
polynomial_hash_BCDE = polynomial_hash("BCDE")
print(rolling_hash_BCDE, polynomial_hash_BCDE)
# Output here will be:
"""
1188870
1207145
"""

# Correctly calculating the polynomial rolling hash by dividing by the correct factor of the removed character, "shifting" the remaining characters by multiplying by 26, and finally adding the correct value of the added character
rolling_hash_BCDE = (polynomial_hash_ABCD - ord("A") * (26**3)) * 26 + ord("E")
print(rolling_hash_BCDE, polynomial_hash_BCDE)
# Output here will be:
"""
1207145
1207145
"""


def polynomial_rolling_hash(s, H, c):
    # Implementing the correct rolling hash method to a given string, its hash value and the next character in the sequence
    H = (H - ord(s[0]) * 26 ** (len(s) - 1)) * 26 + ord(c)
    return H


# Calculating the polynomial rolling hash value for all 4 character substrings of our variable uppercase
s = "ABCD"
H = polynomial_hash(s)

# Initialise a dictionary containing the hash value for "ABCD", to use the values while iterating
polynomial_rolling_hash_values = {s: H}

for char in uppercase[4:]:
    # Calculating the polynomial rolling hash of the next substring
    H = polynomial_rolling_hash(s, H, char)
    # Shifting the string to create the next substring
    s = s[1:] + char
    # Storing the new string: hash as a key: value pair in our dictionary
    polynomial_rolling_hash_values[s] = H

print(polynomial_rolling_hash_values)
# Output here will be:
"""
{'ABCD': 1188866, 'BCDE': 1207145, 'CDEF': 1225424, 'DEFG': 1243703, 'EFGH': 1261982, 'FGHI': 1280261, 'GHIJ': 1298540, 'HIJK': 1316819, 'IJKL': 1335098, 'JKLM': 1353377, 'KLMN': 1371656, 'LMNO': 1389935, 'MNOP': 1408214, 'NOPQ': 1426493, 'OPQR': 1444772, 'PQRS': 1463051, 'QRST': 1481330, 'RSTU': 1499609, 'STUV': 1517888, 'TUVW': 1536167, 'UVWX': 1554446, 'VWXY': 1572725, 'WXYZ': 1591004}
"""
