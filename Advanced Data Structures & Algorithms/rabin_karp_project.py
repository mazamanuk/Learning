def polynomial_hash(s):
	hash_value = 0
	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

def rabin_karp_algorithm_multiple(pattern, text):
	#Your code goes here
	pass

patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEF'
print(rabin_karp_algorithm_multiple(patterns, text))

def rabin_karp_algorithm_2D(pattern, text):
	pass
	#Your code goes here

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))

