"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            else:
                num_dict[num] = 1
        return False

# Public Case 1
print(containsDuplicate([1,2,3,1]))

# Public Case 2
print(containsDuplicate([1,2,3,4]))

# Public Case 3
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))