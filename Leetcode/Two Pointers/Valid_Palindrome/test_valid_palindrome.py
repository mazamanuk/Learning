from valid_palindrome import Solution

def test_is_palindrome():
    sol = Solution()

    # Given test cases
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car") == False
    assert sol.isPalindrome(" ") == True

    # Additional test cases
    assert sol.isPalindrome("! ! ! !") == True
