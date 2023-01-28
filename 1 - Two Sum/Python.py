"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        This is code I wrote based off of the code given below.
        For my original solution, please reference this files history
        """

        dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], i]
            dict[num] = i
            
# Public Case 1
print(twoSum([2,7,11,15], 9))

# Public Case 2
print(twoSum([3,2,4], 6))

# Public Case 3
print(twoSum([3,3], 6))






"""
    Code I found that has the fastest runtime:

    # Create a dictionary to store the elements of the array and their corresponding indices
    element_indices = {}

    # Loop through the array
    for i in range(len(nums)):
        # If the target minus the current element exists in the dictionary, return the indices of the two elements
        if target - nums[i] in element_indices:
            return [element_indices[target - nums[i]], i]

        # Otherwise, add the current element and its index to the dictionary
        element_indices[nums[i]] = i

    # If no such elements are found, return an empty list
    return []
"""