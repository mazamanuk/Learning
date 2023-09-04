from solution import Solution

def test_is_anagram():
    sol = Solution()

    # Given test cases
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False

    # Additional test cases
    assert sol.isAnagram("true", "false") == False
    assert sol.isAnagram("a", "a") == True
