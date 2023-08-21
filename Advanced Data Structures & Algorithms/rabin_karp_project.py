## Implementing Rabin-Karp Algorithm using multiple pattern inputs and even a 2D grid using multiple text inputs.

def polynomial_hash(s):
	hash_value = 0
	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

# This function takes in multiple string inputs for the pattern to search a given text string for multiple patterns at the same time
# Compared to the regular algorithm, this one keeps track of the unique pattern lengths in the input, each pattern's polynomial hash value and their number of occurrences in the text
def rabin_karp_algorithm_multiple(pattern, text):
	# Initialising dictionaries to keep track of hash values and occurrences of each pattern, and a set to track the unique pattern lengths to then take appropriate substrings of our text
	hash_dict = {}
	occurrence_dict = {}
	unique_pattern_lengths = set()
	# For each pattern, we calculate the polynomial hash, store it in the hash_dict and initialise the number of occurrences of that pattern to 0
	for string in pattern:
		string_hash = polynomial_hash(string)
		hash_dict[string_hash] = string
		occurrence_dict[string] = 0
		unique_pattern_lengths.add(len(string))
	# Checking all substrings of length matching each unique pattern length for a matching hash value to the pattern values stored in hash_dict, then incrementing occurrences by 1 for each match
	for pattern_length in unique_pattern_lengths:
		substring_hash = polynomial_hash(text[:pattern_length])
		if substring_hash in hash_dict:
			pattern = hash_dict[substring_hash]
			occurrence_dict[pattern] += 1
		# Inner loop calculates rolling hash values to use for comparisons against the stored hash values in hash_dict
		for character in range(len(text) - pattern_length):
			previous_hash = substring_hash
			substring_hash = polynomial_rolling_hash(previous_hash, text[character], text[character + pattern_length], pattern_length)
			if substring_hash in hash_dict:
				pattern = hash_dict[substring_hash]
				occurrence_dict[pattern] += 1
	# Returns the occurrence_dict after looping through all possible substrings of all requires lengths
	return occurrence_dict

patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEF'
print(rabin_karp_algorithm_multiple(patterns, text))
# Output here will be:
"""
{'ABC': 1, 'BCD': 1, 'CDE': 1, 'DEF': 1}
"""


# This function uses a 2D grid of text and input patterns to search for all occurrences of this given pattern using rows and columns
# We use a modified heuristic to combine the polynomial hashes of each row of a pattern to combine them into a 2D polynomial hash and compare this value to the calculated 2D polynomial hash of all subgrids containing an equal number of columns and rows to our pattern
def rabin_karp_algorithm_2D(pattern, text):
	# Tracking all information related to the pattern and text inputs for ease of access and visibility and readability in the code
	pattern_rows = len(pattern)
	pattern_length = len(pattern[0])
	text_rows = len(text)
	text_length = len(text[0])
	pattern_hash = 0
	occurrences = 0
	# Calculating the 2D polynomial hash of our pattern by multiplying the first row by 10 and adding the second row
	# This allows us to easily implement a rolling method later but gives us enough uniqueness in the hash values to avoid collisions
	for row in range(pattern_rows):
		pattern_hash += polynomial_hash(pattern[row])*(10**(pattern_rows - row - 1))
	# Creating a hash grid containing 0s for all possible substrings to be used for calculating 2D polynomial hashes later
	all_hashes = [[0 for j in range(text_length - pattern_length + 1)] for i in range(text_rows)]
	# Calculating the initial hash values for each row to then calculate the remaining spaces in the grid
	for row in range(text_rows):
		substring_hash = polynomial_hash(text[row][:pattern_length])
		all_hashes[row][0] = substring_hash
		# Calculating the remaining hash values in the grid
		for character in range(text_length - pattern_length):
			previous_hash = substring_hash
			substring_hash = polynomial_rolling_hash(previous_hash, text[row][character], text[row][character + pattern_length], pattern_length)
			all_hashes[row][character + 1] = substring_hash
	# Calculating the initial column 2D polynomial hash to compare to our pattern hash
	for column in range(text_length - pattern_length + 1):
		column_hash = 0
		for row in range(pattern_rows):
			column_hash += all_hashes[row][column]*(10**(pattern_rows - row - 1))
		# If we find a match, increment occurrences by 1
		if column_hash == pattern_hash:
			occurrences += 1
		# For each remaining 2D subgrid, calculate the hash and compare to our pattern hash, incrementing occurrences by 1 if we find a match
		for row in range(text_rows - pattern_rows):
			previous_hash = column_hash
			column_hash = (previous_hash - all_hashes[row][column]*(10**(pattern_rows - 1)))*10 + all_hashes[row + pattern_rows][column]
			if column_hash == pattern_hash:
				occurrences += 1
	# Return occurrences at the end of the function
	return occurrences

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))
# Output here will be:
"""
2
"""
