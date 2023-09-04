from solution import Solution

def test_contains_duplicate():
    sol = Solution()

    # Given test cases
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

    # Additional test cases
    assert sol.containsDuplicate([]) == False
    assert sol.containsDuplicate([1]) == False