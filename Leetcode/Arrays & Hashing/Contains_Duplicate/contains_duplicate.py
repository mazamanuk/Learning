class Solution:
    def containsDuplicate(self, nums):
        # Create a set to store the elements
        unique_elements = set()

        # Iterate through the list of nums
        for num in nums:
            # If the element is already in the set, return True
            if num in unique_elements:
                return True
            # Otherwise, add the element to the set
            else:
                unique_elements.add(num)

        # If we reach this point, it means that every element in the list was unique, so return False
        return False