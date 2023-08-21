def polynomial_hash(s):
	hash_value = 0
	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

def rabin_karp_algorithm_multiple(pattern, text):
	hash_dict = {}
	occurrence_dict = {}
	unique_pattern_lengths = set()
	for string in pattern:
		string_hash = polynomial_hash(string)
		hash_dict[string_hash] = string
		occurrence_dict[string] = 0
		unique_pattern_lengths.add(len(string))
	for pattern_length in unique_pattern_lengths:
		substring_hash = polynomial_hash(text[:pattern_length])
		if substring_hash in hash_dict:
			pattern = hash_dict[substring_hash]
			occurrence_dict[pattern] += 1
		for character in range(len(text) - pattern_length):
			previous_hash = substring_hash
			substring_hash = polynomial_rolling_hash(previous_hash, text[character], text[character + pattern_length], pattern_length)
			if substring_hash in hash_dict:
				pattern = hash_dict[substring_hash]
				occurrence_dict[pattern] += 1
	return occurrence_dict

patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEF'
print(rabin_karp_algorithm_multiple(patterns, text))

def rabin_karp_algorithm_2D(pattern, text):
	pass
	#Your code goes here

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))

