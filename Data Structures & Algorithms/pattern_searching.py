## Building a naive pattern searching algorithm which searches through a string of text character by character to find a given pattern by counting the number of
# matching characters that appear in a row within the text
def pattern_search(text, pattern):
    print("Input Text:", text, "Input Pattern:", pattern)
# Looping through each index of the text to begin the comparison, initialized with a match_count variable set to 0 which we use to count the number of consecutive
# characters that match our given pattern
    for index in range(len(text)):
        print("Text Index:", index)
        match_count = 0
# Looping through each index of the pattern and incrementing our match_count if the text index+character matches our pattern index and breaking otherwise
        for char in range(len(pattern)):
            print("Pattern Index:", char)
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break
# if our match_count variable is equal to the length of the given pattern for any index, we print a statement as we have found our pattern within the text
        if match_count == len(pattern):
            print(pattern, "found at index", index)

# Examples
text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
#pattern_search(text, pattern)
text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
#pattern_search(text2, pattern2)
text3 = "This   still      works with    spaces"
pattern3 = "works"
#pattern_search(text3, pattern3)
text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"
pattern_search(text4, pattern4)


## Modified pattern_search function to include case sensitivity check and a way to replace a pattern with a given string
# fixed_text variable is created to serve as a placeholder for the completed text containing all replacements being made
def pattern_search(text, pattern, replacement, case_sensitive=True):
    fixed_text = ''
    num_skips = 0
    for index in range(len(text)):
# Decrementing our num_skips counter to account for the replacement of the pattern and loop further through the text indices
        if num_skips > 0:
            num_skips -= 1
            continue
        match_count = 0
# Changing the condition check to account for case sensitivity
        for char in range(len(pattern)): 
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
                match_count += 1
            else:
                break
# When the replacement is found, we append it to the fixed_text variable and replace the value of num_skips to account for
# the change in the text, otherwise we add the original character from the text
        if match_count == len(pattern):
            print(pattern, "found at index", index)
            fixed_text += replacement
            num_skips = len(pattern) - 1
        else:
            fixed_text += text[index]
    return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")