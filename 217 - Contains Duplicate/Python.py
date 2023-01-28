def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        while len(nums) != 0:
            i = nums[0]
            nums.pop(0)
            if i in nums and len(nums) > 0:
                return True
        return False

# Case 1
print(containsDuplicate([1,2,3,1]))

# Case 2
print(containsDuplicate([1,2,3,4]))

# Case 3
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))