class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create pointers at the left and right ends of the string
        left, right = 0, len(s) - 1
        # Run as long as there are characters in the string to consider
        while left < right:
            # If the left pointer is at a non-alphanumeric character, increment
            while left < right and not self.alphaNum(s[left]):
                left += 1
            # If the right pointer is at a non-alphanumeric character, decrement
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            # If the left pointer and right pointer characters are ever not equal, return False
            if s[left].lower() != s[right].lower():
                return False
            # Increment left, decrement right
            left, right = left + 1, right - 1
        # If we haven't returned False after looping through every character, we must have a palindrome, return True
        return True

    def alphaNum(self, c):
        # Returns True or False depending on whether a given character is alphanumeric or not
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
